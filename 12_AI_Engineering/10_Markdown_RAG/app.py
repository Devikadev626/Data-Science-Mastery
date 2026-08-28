import os
import streamlit as st
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings, ChatOllama
from langchain_classic.chains import create_retrieval_chain
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate

# Page Configuration
st.set_page_config(
    page_title="CODELENS RAG | Workspace Q&A",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Dark Black & Golden CSS Theme
st.markdown("""
<style>
    .stApp {
        background-color: #0b0d10 !important;
        color: #ffffff !important;
    }
    section[data-testid="stSidebar"] {
        background-color: #12151c !important;
        border-right: 1px solid #262b36 !important;
    }
    h1, h2, h3, label {
        color: #d4af37 !important;
        font-weight: 600 !important;
    }
    .stTextInput input {
        background-color: #161a23 !important;
        color: #ffffff !important;
        border: 1px solid #d4af37 !important;
        border-radius: 6px !important;
    }
    div.stButton > button[kind="primary"] {
        background-color: #d4af37 !important;
        color: #0b0d10 !important;
        border: none !important;
        font-weight: 600 !important;
    }
    div.stButton > button[kind="primary"]:hover {
        background-color: #e5c158 !important;
        color: #000000 !important;
    }
    .section-header {
        font-size: 14px;
        font-weight: 600;
        color: #d4af37;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 12px;
    }
</style>
""", unsafe_allow_html=True)

st.title("WORKSPACE KNOWLEDGE BASE RAG")
st.caption("Semantic Documentation Search & Q&A Assistant")
st.divider()

PERSIST_DIR = os.path.abspath("./chroma_db")
# Targets local workspace folder to keep context focused
WORKSPACE_PATH = os.path.abspath("./")

# Sidebar Controls
with st.sidebar:
    st.markdown('<div class="section-header">Vector Engine</div>', unsafe_allow_html=True)
    
    embedding_model = st.selectbox("Embedding Model", ["nomic-embed-text"])
    llm_model = st.selectbox("LLM Engine", ["llama3.2", "codellama:7b"])
    
    st.divider()
    index_btn = st.button("Index / Reload Vector Store", type="primary", use_container_width=True)

# Safe Markdown Directory Loader
def load_markdown_files(root_dir):
    documents = []
    for root, dirs, files in os.walk(root_dir):
        if ".venv" in root or "chroma_db" in root:
            continue
        for file in files:
            if file.endswith(".md"):
                full_path = os.path.join(root, file)
                try:
                    loader = TextLoader(full_path, encoding="utf-8")
                    documents.extend(loader.load())
                except Exception:
                    pass
    return documents

# Indexing Action
if index_btn:
    with st.spinner("Scanning Markdown files and creating embeddings..."):
        try:
            raw_docs = load_markdown_files(WORKSPACE_PATH)
            
            if not raw_docs:
                st.sidebar.error("No `.md` files found in the current workspace path.")
            else:
                text_splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=30)
                splits = text_splitter.split_documents(raw_docs)
                
                embeddings = OllamaEmbeddings(model=embedding_model)
                vectorstore = Chroma.from_documents(
                    documents=splits,
                    embedding=embeddings,
                    persist_directory=PERSIST_DIR
                )
                st.session_state["vectorstore_ready"] = True
                st.sidebar.success(f"Indexed {len(raw_docs)} file(s) into {len(splits)} text chunks!")
        except Exception as e:
            st.sidebar.error(f"Indexing Failed: {str(e)}")

# Main Query Section
col_left, col_right = st.columns([1, 1], gap="medium")

with col_left:
    st.markdown('<div class="section-header">Ask Workspace Knowledge Base</div>', unsafe_allow_html=True)
    query = st.text_input("Enter your question:", placeholder="How to set up local Ollama embeddings?")
    run_query = st.button("Search & Answer", type="primary")

with col_right:
    st.markdown('<div class="section-header">Retrieved Context & Answer</div>', unsafe_allow_html=True)
    
    if run_query:
        if not query.strip():
            st.warning("Please enter a question first.")
        elif not os.path.exists(PERSIST_DIR) and "vectorstore_ready" not in st.session_state:
            st.warning("Please click 'Index / Reload Vector Store' in the sidebar first!")
        else:
            with st.spinner("Retrieving semantic matches & running LLM synthesis..."):
                try:
                    embeddings = OllamaEmbeddings(model=embedding_model)
                    vectorstore = Chroma(persist_directory=PERSIST_DIR, embedding_function=embeddings)
                    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
                    
                    llm = ChatOllama(model=llm_model, temperature=0)
                    
                    system_prompt = (
                        "You are a technical assistant answering questions using project documentation context.\n"
                        "Answer strictly based on the context snippets provided below. "
                        "If the answer cannot be found in the context, explicitly state: "
                        "'The provided documentation does not contain information about this topic.' "
                        "Do not speculate or guess.\n\n"
                        "{context}"
                    )
                    prompt = ChatPromptTemplate.from_messages([
                        ("system", system_prompt),
                        ("human", "{input}"),
                    ])
                    
                    question_answer_chain = create_stuff_documents_chain(llm, prompt)
                    rag_chain = create_retrieval_chain(retriever, question_answer_chain)
                    
                    response = rag_chain.invoke({"input": query})
                    
                    with st.container(border=True):
                        st.markdown("### Answer")
                        st.markdown(response["answer"])
                    
                    st.markdown("<br>", unsafe_allow_html=True)
                    st.markdown('<div class="section-header">Source Citations</div>', unsafe_allow_html=True)
                    
                    for idx, doc in enumerate(response["context"]):
                        source = doc.metadata.get("source", "Workspace Document")
                        with st.container(border=True):
                            st.caption(f"**Citation {idx+1} Source:** `{source}`")
                            st.code(doc.page_content, language="markdown")
                            
                except Exception as e:
                    st.error(f"Execution Error: {str(e)}")