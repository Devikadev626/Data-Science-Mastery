import os
import tempfile
import textwrap
from pathlib import Path

import streamlit as st

# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="TranscribeAI",
    page_icon="🎙️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# =========================================================
# CUSTOM CSS (BLACK & GOLD PREMIUM THEME)
# =========================================================

st.markdown(
    textwrap.dedent("""
    <style>
    /* ---------------- GLOBAL STYLES ---------------- */
    .stApp {
        background-color: #0b0d11;
        color: #e2e8f0;
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }

    .block-container {
        max-width: 1200px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    /* Headings */
    h1, h2, h3, h4, h5, h6 {
        color: #f1f5f9 !important;
        font-weight: 700 !important;
    }

    p, span, label, div {
        color: #cbd5e1;
    }

    hr {
        border-color: #1e293b !important;
    }

    /* ---------------- HEADER ---------------- */
    .app-header {
        padding: 1.5rem 0 2rem 0;
        border-bottom: 1px solid #1e293b;
        margin-bottom: 2rem;
    }

    .app-title {
        font-size: 2.75rem;
        font-weight: 800;
        letter-spacing: -0.04em;
        background: linear-gradient(135deg, #fbbf24 0%, #d97706 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 0;
    }

    .app-subtitle {
        color: #94a3b8;
        font-size: 1.05rem;
        margin-top: 0.5rem;
    }

    /* ---------------- SIDEBAR ---------------- */
    [data-testid="stSidebar"] {
        background-color: #0f1218 !important;
        border-right: 1px solid #1e293b !important;
    }

    [data-testid="stSidebar"] * {
        color: #94a3b8 !important;
    }

    [data-testid="stSidebar"] h2, 
    [data-testid="stSidebar"] h3 {
        color: #fbbf24 !important;
    }

    /* Selectbox styling in sidebar */
    div[data-baseweb="select"] > div {
        background-color: #161b22 !important;
        border: 1px solid #334155 !important;
        color: #f8fafc !important;
        border-radius: 8px !important;
    }

    div[data-baseweb="select"] * {
        color: #f8fafc !important;
    }

    /* ---------------- BUTTONS ---------------- */
    div.stButton > button {
        width: 100%;
        background: linear-gradient(135deg, #d97706 0%, #b45309 100%);
        color: #ffffff !important;
        border: 1px solid #f59e0b;
        border-radius: 8px;
        padding: 0.75rem 1rem;
        font-weight: 600;
        letter-spacing: 0.02em;
        transition: all 0.2s ease-in-out;
        box-shadow: 0 4px 12px rgba(217, 119, 6, 0.25);
    }

    div.stButton > button:hover {
        background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%);
        color: #ffffff !important;
        box-shadow: 0 6px 16px rgba(245, 158, 11, 0.4);
        border-color: #fbbf24;
    }

    /* ---------------- UPLOADER ---------------- */
    [data-testid="stFileUploader"] {
        border: 1px dashed #334155;
        border-radius: 12px;
        padding: 1.25rem;
        background-color: #11151c;
        transition: border-color 0.2s ease;
    }

    [data-testid="stFileUploader"]:hover {
        border-color: #d97706;
    }

    [data-testid="stFileUploader"] section {
        background-color: transparent !important;
    }

    /* ---------------- METRIC CARDS ---------------- */
    [data-testid="stMetric"] {
        background-color: #11151c;
        border: 1px solid #1e293b;
        border-radius: 12px;
        padding: 1.25rem;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.4);
    }

    [data-testid="stMetricLabel"] {
        color: #94a3b8 !important;
        font-size: 0.875rem !important;
    }

    [data-testid="stMetricValue"] {
        color: #fbbf24 !important;
        font-weight: 700 !important;
    }

    /* ---------------- TEXTAREA / INPUTS ---------------- */
    textarea {
        background-color: #11151c !important;
        color: #f8fafc !important;
        border-radius: 10px !important;
        border: 1px solid #1e293b !important;
        font-family: monospace;
    }

    textarea:focus {
        border-color: #d97706 !important;
        box-shadow: 0 0 0 1px #d97706 !important;
    }

    /* ---------------- DOWNLOAD BUTTON ---------------- */
    [data-testid="stDownloadButton"] > button {
        width: 100%;
        background-color: #161b22;
        color: #fbbf24 !important;
        border: 1px solid #d97706;
        border-radius: 8px;
        font-weight: 600;
        transition: all 0.2s ease;
    }

    [data-testid="stDownloadButton"] > button:hover {
        background-color: #d97706;
        color: #ffffff !important;
    }

    /* ---------------- AUDIO PLAYER ---------------- */
    audio {
        border-radius: 8px;
        width: 100%;
        filter: invert(0.9) hue-rotate(180deg);
    }

    /* ---------------- ALERTS ---------------- */
    .stAlert {
        background-color: #11151c;
        border: 1px solid #1e293b;
        color: #cbd5e1;
        border-radius: 10px;
    }
    </style>
    """),
    unsafe_allow_html=True,
)

# =========================================================
# MODEL CONFIGURATION
# =========================================================

MODEL_OPTIONS = {
    "tiny": "openai/whisper-tiny",
    "base": "openai/whisper-base",
    "small": "openai/whisper-small",
}

MODEL_INFO = {
    "tiny": {
        "description": "Fastest model for quick testing",
        "accuracy": "Basic",
    },
    "base": {
        "description": "Best balance between speed and accuracy",
        "accuracy": "Recommended",
    },
    "small": {
        "description": "Better accuracy with slower processing",
        "accuracy": "High",
    },
}

# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:
    st.markdown("## TranscribeAI")
    st.caption("AI-powered audio transcription")
    st.divider()

    st.markdown("### Model Settings")
    selected_model = st.selectbox(
        "Whisper Model",
        options=list(MODEL_OPTIONS.keys()),
        index=1,
    )

    info = MODEL_INFO[selected_model]
    st.caption(info["description"])

    st.divider()

    st.markdown("### Project Stack")
    st.caption("• OpenAI Whisper")
    st.caption("• Hugging Face Transformers")
    st.caption("• PyTorch")
    st.caption("• Streamlit")

    st.divider()
    st.caption("AI Audio Intelligence Platform")

# =========================================================
# HEADER
# =========================================================

st.markdown(
    """
<div class="app-header">
    <h1 class="app-title">TranscribeAI</h1>
    <p class="app-subtitle">
        Upload audio, select an AI model, and generate high-precision transcripts instantly.
    </p>
</div>
""",
    unsafe_allow_html=True,
)

# =========================================================
# LOAD MODEL
# =========================================================

@st.cache_resource
def load_transcriber(model_name):
    from src.transcriber import WhisperTranscriber

    transcriber = WhisperTranscriber(model_name=model_name)
    transcriber.load_model()
    return transcriber

# =========================================================
# STEP 1 — UPLOAD
# =========================================================

st.markdown("### 1. Upload Audio")
st.caption("Supported formats: MP3, WAV, M4A, FLAC, OGG, and AAC.")

uploaded_file = st.file_uploader(
    "Upload audio file",
    type=["mp3", "wav", "m4a", "flac", "ogg", "aac"],
    label_visibility="collapsed",
)

# =========================================================
# EMPTY STATE
# =========================================================

if uploaded_file is None:
    st.info("Upload an audio file to begin transcription.")

# =========================================================
# AUDIO FILE UPLOADED
# =========================================================

else:
    st.divider()

    info_col, action_col = st.columns([3, 1], vertical_alignment="bottom")

    with info_col:
        st.markdown("### 2. Review Audio")
        st.caption(f"File: **{uploaded_file.name}**")

    with action_col:
        transcribe_button = st.button("Generate Transcript", type="primary")

    st.audio(uploaded_file)

    # =================================================
    # TRANSCRIPTION
    # =================================================

    if transcribe_button:
        temp_audio_path = None

        try:
            suffix = Path(uploaded_file.name).suffix

            with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as temp_file:
                temp_file.write(uploaded_file.getvalue())
                temp_audio_path = temp_file.name

            progress = st.progress(0)
            status = st.empty()

            status.write("Loading AI transcription model...")
            progress.progress(25)

            model_name = MODEL_OPTIONS[selected_model]
            transcriber = load_transcriber(model_name)

            progress.progress(60)
            status.write("Analyzing audio...")

            result = transcriber.transcribe(temp_audio_path)

            progress.progress(100)
            status.empty()

            st.success("Transcription completed successfully.")
            st.divider()

            # ------------------------------------------
            # RESULT HEADER
            # ------------------------------------------

            st.markdown("### 3. Transcription Result")

            result_col, details_col = st.columns([3, 1], gap="large")

            with result_col:
                st.text_area(
                    "Transcript",
                    value=result["text"],
                    height=350,
                )

                st.download_button(
                    label="Download Transcript (.txt)",
                    data=result["text"],
                    file_name=f"{Path(uploaded_file.name).stem}_transcript.txt",
                    mime="text/plain",
                )

            with details_col:
                st.markdown("#### Details")

                st.metric("Model", selected_model.upper())
                st.metric("Device", result["device"].upper())
                st.metric("Processing Time", f"{result['transcription_time']} sec")
                st.metric("Characters", len(result["text"]))

        except Exception as error:
            st.error("Transcription failed.")
            st.exception(error)

        finally:
            if temp_audio_path is not None and os.path.exists(temp_audio_path):
                os.remove(temp_audio_path)

# =========================================================
# FOOTER
# =========================================================

st.divider()
st.caption("TranscribeAI · AI Audio Intelligence · OpenAI Whisper + Hugging Face")