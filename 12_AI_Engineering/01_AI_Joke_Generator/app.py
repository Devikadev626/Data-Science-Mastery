import streamlit as st
from ollama import chat

# -----------------------------
# Configure Streamlit Page
# -----------------------------
st.set_page_config(
    page_title="The Retro Comedy Stage",
    page_icon="🎤",
    layout="centered",
    initial_sidebar_state="expanded"
)

# -----------------------------
# 🎨 Custom Retro Pop-Art Theme Styling
# -----------------------------
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@500;700;900&family=Plus+Jakarta+Sans:wght@400;600&display=swap');

        html, body, [class*="css"] {
            font-family: 'Plus Jakarta Sans', sans-serif;
        }

        h1, h2, h3, h4 {
            font-family: 'Montserrat', sans-serif;
        }

        /* Rich dark stage background with a hint of warm purple */
        .stApp {
            background: linear-gradient(135deg, #1b122c 0%, #29183b 100%);
            color: #f3f0ff;
        }

        /* Sidebar Styling */
        [data-testid="stSidebar"] {
            background-color: #150e21;
            border-right: 2px solid rgba(255, 107, 107, 0.2);
        }

        /* Hero Container matching the image vibe */
        .hero-container {
            background: linear-gradient(135deg, #ff6b6b 0%, #ff8e53 50%, #9c27b0 100%);
            padding: 2rem;
            border-radius: 24px;
            text-align: center;
            box-shadow: 0 10px 30px rgba(255, 107, 107, 0.25);
            margin-bottom: 2rem;
            border: 2px solid rgba(255, 255, 255, 0.2);
        }

        .hero-container h1 {
            color: #ffffff;
            font-weight: 900;
            font-size: 2.5rem;
            margin-bottom: 0.2rem;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
        }

        .hero-container p {
            color: #fff5f5;
            font-size: 1.1rem;
            font-weight: 600;
            margin: 0;
        }

        /* Input Card */
        .input-card {
            background: rgba(35, 24, 53, 0.8);
            backdrop-filter: blur(10px);
            border: 2px solid rgba(0, 240, 255, 0.2);
            padding: 25px;
            border-radius: 20px;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
            margin-bottom: 1.5rem;
        }

        /* Electric Teal & Coral Button */
        .stButton > button {
            width: 100%;
            background: linear-gradient(135deg, #00f0ff 0%, #7000ff 100%);
            color: white;
            font-family: 'Montserrat', sans-serif;
            font-weight: 700;
            font-size: 1.1rem;
            padding: 0.75rem 1.5rem;
            border-radius: 14px;
            border: none;
            box-shadow: 0 6px 20px rgba(0, 240, 255, 0.3);
            transition: all 0.3s ease;
        }

        .stButton > button:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 25px rgba(0, 240, 255, 0.5);
            background: linear-gradient(135deg, #33f3ff 0%, #8022ff 100%);
            color: white;
        }

        /* Joke Output Card */
        .joke-card {
            background: rgba(35, 24, 53, 0.95);
            border: 2px solid rgba(255, 107, 107, 0.3);
            padding: 25px;
            border-radius: 20px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.4);
            margin-top: 1.5rem;
            border-left: 8px solid #ff6b6b;
        }

        .joke-item {
            font-size: 1.1rem;
            color: #f3f0ff;
            line-height: 1.7;
            margin-bottom: 12px;
            padding-bottom: 12px;
            border-bottom: 1px solid rgba(255, 255, 255, 0.08);
        }

        /* Form Inputs */
        .stTextInput input {
            background-color: #150e21 !important;
            border: 2px solid rgba(0, 240, 255, 0.2) !important;
            border-radius: 12px !important;
            color: #00f0ff !important;
            font-weight: 600;
        }
        
        .stTextInput input:focus {
            border-color: #00f0ff !important;
            box-shadow: 0 0 0 3px rgba(0, 240, 255, 0.2) !important;
        }

        [data-testid="stSidebar"] label, [data-testid="stSidebar"] span {
            color: #f3f0ff !important;
            font-weight: 600 !important;
        }
    </style>
""", unsafe_allow_html=True)

# -----------------------------
# Hero Banner with Local Image Integration
# -----------------------------
col_img, col_text = st.columns([1, 2], gap="medium")

with col_img:
    try:
        st.image("images/malvarrosadesigns-ai-generated-8229806.png")
    except Exception:
        st.warning("Could not load local image. Please check the file path.")

with col_text:
    st.markdown("""
        <div class="hero-container" style="height: 100%; display: flex; flex-direction: column; justify-content: center; margin-bottom: 0;">
            <h1>The Retro Stage</h1>
            <p>Grab the virtual mic! Instant, vibrant, feel-good comedy powered by your local AI.</p>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)

# -----------------------------
# Sidebar Configuration
# -----------------------------
with st.sidebar:
    st.markdown("### 🎙️ Show Settings")
    st.markdown("Tune your live performance mood:")
    
    style = st.selectbox(
        "Joke Style",
        [
            "Random Mix",
            "Programming & Tech",
            "Classic Dad Jokes",
            "Clever One-Liners",
            "Knock-Knock Jokes"
        ]
    )

    count = st.slider(
        "Number of Jokes",
        min_value=1,
        max_value=5,
        value=3
    )
    
    st.markdown("---")
    st.markdown("💡 **Stage Tip:** Try quirky topics like *retro vinyl records*, *neon lights*, or *midnight snacking* for peak performance.")

# -----------------------------
# Main Input Section
# -----------------------------
st.markdown("<div class='input-card'>", unsafe_allow_html=True)

# Quick Mood Presets
st.markdown("<p style='font-weight: 600; color: #00f0ff; margin-bottom: 8px;'>✨ Quick Mood Shortcuts:</p>", unsafe_allow_html=True)
col_btn1, col_btn2, col_btn3, col_btn4 = st.columns(4)

# Initialize session state for topic if not present
if "selected_topic" not in st.session_state:
    st.session_state.selected_topic = ""

if col_btn1.button("☕ Coffee"):
    st.session_state.selected_topic = "Coffee"
if col_btn2.button("🐱 Cats"):
    st.session_state.selected_topic = "Cats"
if col_btn3.button("🍕 Pizza"):
    st.session_state.selected_topic = "Pizza"
if col_btn4.button("💻 Coding"):
    st.session_state.selected_topic = "Coding"

topic_input = st.text_input(
    label="🎯 What's the spotlight on today?",
    value=st.session_state.selected_topic,
    placeholder="e.g., retro music, Monday mornings, space travel..."
)

# Update session state if user manually types something new
if topic_input != st.session_state.selected_topic:
    st.session_state.selected_topic = topic_input

st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)
generate_btn = st.button("Take the Mic & Perform!")

st.markdown("</div>", unsafe_allow_html=True)

# -----------------------------
# AI Integration & Output Display
# -----------------------------
if generate_btn:
    if not topic_input.strip():
        st.warning("⚠️ The stage is waiting! Please enter or select a topic first.")
    else:
        prompt = f"""
        Generate exactly {count} {style.lower()} style jokes about {topic_input}.
        Guidelines:
        1. Number each joke clearly.
        2. Use extremely simple English, easy words, and direct sentences so anyone can understand instantly.
        3. Avoid complex wordplay, difficult puns, or idioms.
        4. Keep each joke under 30 words.
        5. Make it family-friendly, lively, upbeat, and genuinely funny.
        6. Do not include any intro text or explanations.
        """

        with st.spinner("🎤 Tuning up the instruments and writing punchlines..."):
            try:
                response = chat(
                    model="llama3.2",
                    messages=[
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ]
                )
                
                joke_content = response["message"]["content"]
                
                st.markdown("<div class='joke-card'>", unsafe_allow_html=True)
                st.markdown("<h3 style='color: #00f0ff; margin-top: 0; margin-bottom: 15px;'>🌟 Live from the Stage:</h3>", unsafe_allow_html=True)
                
                jokes = joke_content.strip().split('\n')
                for joke in jokes:
                    if joke.strip():
                        st.markdown(f"<div class='joke-item'>{joke.strip()}</div>", unsafe_allow_html=True)
                        
                st.markdown("</div>", unsafe_allow_html=True)
                st.success("🎉 Encore! That was a stellar performance.")

            except Exception as e:
                st.error("Oops! The microphone disconnected.")
                st.info("Make sure your Ollama application is running locally in the background.")

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #a0aec0; font-size: 0.85rem; margin-top: 2rem;'>"
    "Live from the Retro Comedy Lounge | Powered locally by Llama 3.2"
    "</div>", 
    unsafe_allow_html=True
)