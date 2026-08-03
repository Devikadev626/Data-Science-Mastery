import streamlit as st
import time
import requests
from openai import OpenAI

# ---------------------------------------------------------
# 1. PAGE CONFIG & INDUSTRY-STANDARD BLUE/BLACK ANIMATED THEME
# ---------------------------------------------------------
st.set_page_config(
    page_title="Enterprise AI Synthesis Studio",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for Pure Black, Neon Blue Accents, Animations & Micro-Interactions
st.markdown("""
<style>
    /* Keyframe Animations */
    @keyframes pulseGlow {
        0% { box-shadow: 0 0 10px rgba(0, 210, 255, 0.2); }
        50% { box-shadow: 0 0 25px rgba(0, 210, 255, 0.5); }
        100% { box-shadow: 0 0 10px rgba(0, 210, 255, 0.2); }
    }

    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }

    /* Global System Styles */
    .stApp {
        background-color: #000000;
        background-image: 
            radial-gradient(circle at 15% 15%, rgba(0, 102, 255, 0.08) 0%, transparent 40%),
            radial-gradient(circle at 85% 85%, rgba(0, 210, 255, 0.05) 0%, transparent 40%);
        color: #93c5fd;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    }

    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background-color: #030712;
        border-right: 1px solid rgba(0, 162, 255, 0.25);
    }

    /* Headings */
    h1, h2, h3, h4 {
        color: #38bdf8 !important;
        font-weight: 700 !important;
        letter-spacing: -0.02em;
        text-shadow: 0 0 12px rgba(56, 189, 248, 0.3);
    }

    /* Subtitles and Labels */
    .stCaption, p, label {
        color: #60a5fa !important;
    }

    /* Interactive Cards / Containers */
    .telemetry-card {
        background: rgba(3, 7, 18, 0.8);
        border: 1px solid rgba(56, 189, 248, 0.3);
        border-radius: 8px;
        padding: 16px;
        text-align: center;
        backdrop-filter: blur(10px);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        animation: fadeIn 0.6s ease-out;
    }

    .telemetry-card:hover {
        border-color: #00d2ff;
        transform: translateY(-3px);
        box-shadow: 0 8px 20px rgba(0, 210, 255, 0.25);
    }

    .telemetry-label {
        font-size: 0.75rem;
        color: #38bdf8;
        text-transform: uppercase;
        letter-spacing: 0.1em;
        font-weight: 600;
    }

    .telemetry-value {
        font-size: 1.6rem;
        font-weight: 800;
        color: #60a5fa;
        margin-top: 4px;
        text-shadow: 0 0 10px rgba(96, 165, 250, 0.4);
    }

    /* Form Controls & Input Styling */
    textarea, input, div[data-baseweb="select"] {
        background-color: #030712 !important;
        color: #93c5fd !important;
        border: 1px solid rgba(56, 189, 248, 0.3) !important;
        border-radius: 8px !important;
        transition: all 0.3s ease !important;
    }

    textarea:focus, input:focus {
        border-color: #00d2ff !important;
        box-shadow: 0 0 12px rgba(0, 210, 255, 0.4) !important;
    }

    /* Custom Button Overrides */
    .stButton>button {
        background: linear-gradient(135deg, #030712 0%, #0b1528 100%);
        color: #38bdf8 !important;
        border: 1px solid #38bdf8 !important;
        border-radius: 8px;
        font-weight: 600;
        letter-spacing: 0.03em;
        padding: 0.6rem 1rem;
        transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
    }

    .stButton>button:hover {
        background: #38bdf8 !important;
        color: #000000 !important;
        box-shadow: 0 0 20px rgba(56, 189, 248, 0.6);
        transform: scale(1.02);
    }

    /* Primary Button Glow Animation */
    div[data-testid="stButton"] button[kind="primary"] {
        background: linear-gradient(135deg, #0284c7 0%, #0369a1 100%);
        color: #ffffff !important;
        border: 1px solid #38bdf8 !important;
        animation: pulseGlow 3s infinite ease-in-out;
    }

    div[data-testid="stButton"] button[kind="primary"]:hover {
        background: #00d2ff !important;
        color: #000000 !important;
    }

    /* Output Container Box */
    .output-container {
        background: rgba(3, 7, 18, 0.9);
        border: 1px solid rgba(56, 189, 248, 0.4);
        border-radius: 8px;
        padding: 20px;
        min-height: 300px;
        font-size: 0.95rem;
        line-height: 1.7;
        color: #93c5fd;
        box-shadow: inset 0 0 15px rgba(0, 102, 255, 0.05);
        animation: fadeIn 0.5s ease-in-out;
    }

    /* Status Widget */
    .status-badge {
        padding: 12px;
        background-color: rgba(3, 7, 18, 0.9);
        border-radius: 8px;
        border: 1px solid rgba(56, 189, 248, 0.3);
        backdrop-filter: blur(8px);
    }
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# 2. STATE MANAGEMENT & API CALL FUNCTIONS
# ---------------------------------------------------------
if "document_text" not in st.session_state:
    st.session_state.document_text = ""
if "synthesized_output" not in st.session_state:
    st.session_state.synthesized_output = ""

def load_sample_doc():
    st.session_state.document_text = (
        "Enterprise Architecture Assessment Report - Q3\n\n"
        "1. Overview:\n"
        "The shift towards decentralized cloud infrastructure has reduced overall operational latency "
        "by 24 percent. However, multi-cloud API security boundaries require immediate auditing due to "
        "inconsistent telemetry coverage across regions.\n\n"
        "2. Key Findings:\n"
        "- Microservice degradation in Cluster B caused minor SLA breaches.\n"
        "- Token usage costs grew 15 percent due to unoptimized prompt lengths in production agents.\n"
        "- Recommended strategy: Implement local model routing for routine tasks and reservation-based LLM endpoints."
    )

def clear_workspace():
    st.session_state.document_text = ""
    st.session_state.synthesized_output = ""

# API Connector Functions
def call_openai_api(api_key, model_name, prompt, system_instruction, temperature, max_tokens):
    client = OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model=model_name,
        messages=[
            {"role": "system", "content": system_instruction},
            {"role": "user", "content": prompt}
        ],
        temperature=temperature,
        max_tokens=max_tokens
    )
    return response.choices[0].message.content

def call_ollama_api(endpoint_url, model_name, prompt, system_instruction, temperature):
    payload = {
        "model": model_name,
        "prompt": f"System: {system_instruction}\n\nUser: {prompt}",
        "stream": False,
        "options": {
            "temperature": temperature
        }
    }
    response = requests.post(f"{endpoint_url}/api/generate", json=payload, timeout=60)
    if response.status_code == 200:
        return response.json().get("response", "")
    else:
        raise Exception(f"Ollama Server Error {response.status_code}: {response.text}")

# ---------------------------------------------------------
# 3. SIDEBAR: CONFIGURATION AND CONTROL
# ---------------------------------------------------------
with st.sidebar:
    st.markdown("### Engine Control")
    st.caption("Configure live LLM backend connections.")
    
    # Provider Selection
    provider = st.radio("Inference Provider", options=["OpenAI API", "Local Ollama"], index=0)
    
    st.markdown("---")
    
    if provider == "OpenAI API":
        api_key = st.text_input("OpenAI API Key", type="password", help="Enter your sk-... key")
        selected_model = st.selectbox(
            "Model Target",
            options=["gpt-4o", "gpt-4o-mini", "gpt-3.5-turbo"],
            index=0
        )
    else:
        ollama_url = st.text_input("Ollama Endpoint", value="http://localhost:11434")
        selected_model = st.selectbox(
            "Model Target",
            options=["llama3.2", "mistral", "llama3.1", "phi3"],
            index=0
        )
    
    # Analysis Mode Selector
    analysis_type = st.selectbox(
        "Synthesis Task",
        options=[
            "Executive Summary",
            "Key Insights and Takeaways",
            "Action Item Extraction",
            "Risk and Vulnerability Scan",
            "Technical Refactoring Notes"
        ],
        index=0
    )
    
    # Hyperparameters
    st.markdown("#### Hyperparameters")
    temperature = st.slider("Temperature", min_value=0.0, max_value=1.0, value=0.2, step=0.05)
    max_tokens = st.select_slider("Max Target Tokens", options=[256, 512, 1024, 2048, 4096], value=1024)
    
    st.markdown("---")
    
    st.markdown(f"""
    <div class="status-badge">
        <strong style="color: #38bdf8;">Backend Mode:</strong> <span style="color: #60a5fa;">{provider}</span><br/>
        <small style="color: #38bdf8; opacity: 0.8;">Target: {selected_model}</small>
    </div>
    """, unsafe_allow_html=True)


# ---------------------------------------------------------
# 4. MAIN WORKSPACE (2-COLUMN RESPONSIVE CANVAS)
# ---------------------------------------------------------
st.title("AI Synthesis and Intelligence Studio")
st.caption("Ingest documents, execute live model transformation, and extract enterprise insights.")

col_input, col_output = st.columns([1, 1], gap="large")

# ---------------------------------------------------------
# COLUMN 1: INPUT WORKSPACE
# ---------------------------------------------------------
with col_input:
    st.markdown("### Input Workspace")
    
    # File Uploader
    uploaded_file = st.file_uploader(
        "Upload Source Document",
        type=["txt", "md", "pdf"],
        help="Supports Plain Text, Markdown, and PDF file parsing."
    )
    
    if uploaded_file is not None:
        try:
            if uploaded_file.name.endswith(('.txt', '.md')):
                st.session_state.document_text = uploaded_file.read().decode("utf-8")
            else:
                st.session_state.document_text = f"[Binary PDF File Loaded: '{uploaded_file.name}']"
        except Exception as e:
            st.error(f"Error reading file: {e}")

    # Primary Input Text Area
    st.session_state.document_text = st.text_area(
        "Document Text Payload",
        value=st.session_state.document_text,
        height=320,
        placeholder="Paste text payload here or upload a document above...",
    )
    
    # Action Toolbar
    btn_col1, btn_col2, btn_col3 = st.columns([1, 1, 1])
    with btn_col1:
        st.button("Sample Doc", on_click=load_sample_doc, use_container_width=True)
    with btn_col2:
        st.button("Clear", on_click=clear_workspace, use_container_width=True)
    with btn_col3:
        run_synthesis = st.button("Synthesize", type="primary", use_container_width=True)


# ---------------------------------------------------------
# COLUMN 2: SYNTHESIZED OUTPUT & TELEMETRY
# ---------------------------------------------------------
with col_output:
    st.markdown("### Synthesized Output")
    
    # Execute Live API Invocations
    if run_synthesis:
        if not st.session_state.document_text.strip():
            st.warning("Please provide input text or load a sample document first.")
        else:
            system_prompt = f"You are an enterprise AI assistant. Perform a detailed '{analysis_type}' on the following text."
            
            with st.spinner(f"Inferencing via {provider} ({selected_model})..."):
                try:
                    if provider == "OpenAI API":
                        if not api_key:
                            st.error("Please provide a valid OpenAI API Key in the sidebar.")
                        else:
                            st.session_state.synthesized_output = call_openai_api(
                                api_key, selected_model, st.session_state.document_text, 
                                system_prompt, temperature, max_tokens
                            )
                    else:
                        st.session_state.synthesized_output = call_ollama_api(
                            ollama_url, selected_model, st.session_state.document_text, 
                            system_prompt, temperature
                        )
                except Exception as e:
                    st.error(f"Inference Error: {str(e)}")

    # Render Output Container Box
    output_text = st.session_state.synthesized_output
    if output_text:
        st.markdown(f'<div class="output-container">{output_text}</div>', unsafe_allow_html=True)
    else:
        st.markdown(
            '<div class="output-container" style="color: #38bdf8; opacity: 0.6; font-style: italic;">'
            'Synthesized intelligence output will appear here after executing a task.'
            '</div>', 
            unsafe_allow_html=True
        )

    st.markdown("<br/>", unsafe_allow_html=True)
    
    # Export Utility
    if output_text:
        st.download_button(
            label="Export Output (.md)",
            data=output_text,
            file_name=f"synthesis_{analysis_type.lower().replace(' ', '_')}.md",
            mime="text/markdown",
            use_container_width=True
        )
    
    # Real-Time Telemetry Metrics Grid
    st.markdown("---")
    st.markdown("#### Input Telemetry")
    
    raw_text = st.session_state.document_text
    char_count = len(raw_text)
    word_count = len(raw_text.split()) if raw_text else 0
    estimated_tokens = int(char_count / 4) if char_count > 0 else 0
    
    m_col1, m_col2, m_col3 = st.columns(3)
    
    with m_col1:
        st.markdown(f"""
        <div class="telemetry-card">
            <div class="telemetry-label">Words</div>
            <div class="telemetry-value">{word_count:,}</div>
        </div>
        """, unsafe_allow_html=True)
        
    with m_col2:
        st.markdown(f"""
        <div class="telemetry-card">
            <div class="telemetry-label">Characters</div>
            <div class="telemetry-value">{char_count:,}</div>
        </div>
        """, unsafe_allow_html=True)
        
    with m_col3:
        st.markdown(f"""
        <div class="telemetry-card">
            <div class="telemetry-label">Est. Tokens</div>
            <div class="telemetry-value">{estimated_tokens:,}</div>
        </div>
        """, unsafe_allow_html=True)