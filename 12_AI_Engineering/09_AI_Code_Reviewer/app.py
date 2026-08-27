import streamlit as st
import ollama

# Page Configuration
st.set_page_config(
    page_title="CODELENS AI",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling (Black Background + High-Contrast Golden/White Text for Textarea)
st.markdown("""
<style>
    /* Main Background & Base Text */
    .stApp {
        background-color: #0b0d10 !important;
        color: #ffffff !important;
    }
    
    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background-color: #12151c !important;
        border-right: 1px solid #262b36 !important;
    }

    /* Headings Accent - Warm Gold */
    h1, h2, h3, label {
        color: #d4af37 !important;
        font-weight: 600 !important;
    }
    
    /* Fix Text Area Input & Font Visibility */
    .stTextArea textarea {
        background-color: #161a23 !important;
        color: #ffffff !important;
        font-family: 'Courier New', Courier, monospace !important;
        font-size: 14px !important;
        border: 1px solid #d4af37 !important;
        border-radius: 6px !important;
    }

    /* Text Area Focus State (Ensures copy-paste highlight is clear) */
    .stTextArea textarea:focus {
        border-color: #e5c158 !important;
        box-shadow: 0 0 5px rgba(212, 175, 55, 0.5) !important;
        color: #ffffff !important;
    }

    /* Metric Cards */
    .metric-card {
        background-color: #12151c;
        border: 1px solid #262b36;
        border-radius: 6px;
        padding: 12px;
        text-align: center;
    }
    .metric-value {
        font-size: 18px;
        font-weight: 700;
        color: #d4af37;
    }
    .metric-label {
        font-size: 11px;
        color: #9499a8;
        text-transform: uppercase;
        letter-spacing: 0.8px;
    }

    /* Primary Golden Button */
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

    /* Section Sub-headers */
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

# Top Header Banner
st.title("CODELENS AI")
st.caption("Automated Code Inspection & Refactoring Platform")
st.divider()

# Sidebar Setup
with st.sidebar:
    st.markdown('<div class="section-header">Control Panel</div>', unsafe_allow_html=True)
    
    model_name = st.selectbox(
        "Execution Model",
        ["llama3.2", "codellama:7b"],
        help="Select the active local Ollama model instance."
    )
    
    language = st.selectbox(
        "Programming Language",
        ["Python", "JavaScript", "TypeScript", "C++", "Java", "Go", "Rust", "SQL"]
    )
    
    analysis_depth = st.radio(
        "Inspection Mode",
        ["Standard Audit", "Security Vulnerabilities", "Performance & Memory"],
        index=0
    )

# Main Application Layout
col_left, col_right = st.columns([1, 1], gap="medium")

with col_left:
    st.markdown('<div class="section-header">Source Input</div>', unsafe_allow_html=True)
    user_code = st.text_area(
        label="Source Input Area",
        label_visibility="collapsed",
        height=460,
        placeholder=f"Paste your {language} source code here..."
    )
    
    btn_col1, btn_col2 = st.columns([1, 1])
    with btn_col1:
        run_btn = st.button("Analyze Code", type="primary", use_container_width=True)
    with btn_col2:
        clear_btn = st.button("Reset Input", use_container_width=True)

if clear_btn:
    st.rerun()

# Execution & Analysis Column
with col_right:
    st.markdown('<div class="section-header">Analysis Output</div>', unsafe_allow_html=True)
    
    if run_btn:
        if not user_code.strip():
            st.warning("Input required. Please paste code to evaluate.")
        else:
            with st.spinner("Processing analysis pipeline..."):
                prompt = f"""
                You are a Senior Software Architect conducting a formal code review.
                Target Language: {language}
                Evaluation Focus: {analysis_depth}
                
                Code Snippet:
                ```{language}
                {user_code}
                ```

                Provide your report strictly formatted as follows:
                ### 1. Executive Summary
                Concise overview of overall code quality and maintainability.

                ### 2. Bugs & Security Analysis
                Detailed list of logic flaws, security vulnerabilities, or edge-case handling issues.

                ### 3. Optimization Recommendations
                Specific actions to optimize performance, memory efficiency, and style adherence.

                ### 4. Refactored Implementation
                Complete production-ready code snippet wrapped in a standard Markdown code block.
                """

                try:
                    response = ollama.generate(model=model_name, prompt=prompt)
                    output_text = response['response']

                    # Status Metrics Overview
                    m1, m2, m3 = st.columns(3)
                    with m1:
                        st.markdown('<div class="metric-card"><div class="metric-value">Active</div><div class="metric-label">Status</div></div>', unsafe_allow_html=True)
                    with m2:
                        st.markdown(f'<div class="metric-card"><div class="metric-value">{language}</div><div class="metric-label">Language</div></div>', unsafe_allow_html=True)
                    with m3:
                        st.markdown(f'<div class="metric-card"><div class="metric-value">{model_name}</div><div class="metric-label">Engine</div></div>', unsafe_allow_html=True)

                    st.markdown("<br>", unsafe_allow_html=True)
                    
                    # Markdown Output Display Container
                    with st.container(border=True):
                        st.markdown(output_text)
                        
                except Exception as e:
                    st.error(f"Execution Error: {str(e)}")
    else:
        st.info("Initiate analysis by selecting settings and clicking 'Analyze Code'.")