import streamlit as st
from ollama import chat

# Step 2: Configure the Streamlit Page
st.set_page_config(
    page_title="AI Smart Email Generator",
    page_icon="📧",
    layout="wide"
)

# --- CUSTOM CSS STYLING (Professional UI Enhancement) ---
st.markdown("""
    <style>
    /* Main Background & Font */
    .stApp {
        background-color: #f8fafc;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    /* Gradient Header Container */
    .main-header {
        background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%);
        padding: 2.5rem;
        border-radius: 12px;
        color: white;
        margin-bottom: 2rem;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }
    .main-header h1 {
        color: white !important;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }
    .main-header p {
        color: #e2e8f0 !important;
        font-size: 1.1rem;
    }

    /* Card Containers for Inputs */
    .input-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.05);
        margin-bottom: 1.5rem;
    }

    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background-color: #0f172a;
        color: #f8fafc;
    }
    [data-testid="stSidebar"] h2, [data-testid="stSidebar"] label {
        color: #f8fafc !important;
    }

    /* Custom Button Styling */
    .stButton button {
        background: linear-gradient(135deg, #2563eb 0%, #1d4ed8 100%);
        color: white;
        font-weight: 600;
        border-radius: 8px;
        padding: 0.6rem 1.5rem;
        border: none;
        box-shadow: 0 4px 6px -1px rgba(37, 99, 235, 0.2);
        transition: all 0.3s ease;
    }
    .stButton button:hover {
        background: linear-gradient(135deg, #1d4ed8 0%, #1e40af 100%);
        box-shadow: 0 6px 8px -1px rgba(37, 99, 235, 0.3);
    }

    /* Footer Style */
    .footer {
        text-align: center;
        margin-top: 4rem;
        color: #64748b;
        font-size: 0.85rem;
        border-top: 1px solid #e2e8f0;
        padding-top: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

# --- HEADER SECTION ---
st.markdown("""
    <div class="main-header">
        <h1>AI Smart Email Generator</h1>
        <p>Generate professional business communications instantly using advanced prompt engineering and local language models.</p>
    </div>
""", unsafe_allow_html=True)

# --- STEP 4: CREATE THE SIDEBAR ---
with st.sidebar:
    st.header("Email Configuration")
    st.markdown("---")
    
    email_type = st.selectbox(
        "Email Type",
        [
            "Leave Request",
            "Job Application",
            "Meeting Invitation",
            "Thank You",
            "Complaint",
            "Business Proposal"
        ]
    )

    tone = st.selectbox(
        "Tone",
        [
            "Professional",
            "Friendly",
            "Formal",
            "Persuasive"
        ]
    )

    length = st.selectbox(
        "Email Length",
        [
            "Short",
            "Medium",
            "Long"
        ]
    )
    
    st.markdown("---")
    st.info("Provide specific instructions in the text area for more customized and accurate results.")

# --- STEP 5: CREATE USER INPUTS ---
st.markdown("### Input Details")
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        recipient = st.text_input("Recipient Name", placeholder="e.g., Jane Doe")
        company = st.text_input("Company Name", placeholder="e.g., Acme Corp")
    with col2:
        sender = st.text_input("Sender Name", placeholder="e.g., John Smith")
        
    instructions = st.text_area(
        "Additional Instructions", 
        placeholder="e.g., Mention the meeting scheduled for next Tuesday at 10 AM..."
    )

st.markdown("<br>", unsafe_allow_html=True)

# --- STEP 6, 7, 8, 9, 10: GENERATE BUTTON & AI PIPELINE ---
col_btn, col_space = st.columns([1, 4])
with col_btn:
    generate = st.button("Generate Email", use_container_width=True)

if generate:
    # Validation check
    if not recipient or not sender:
        st.warning("Please fill in at least the Recipient and Sender names before generating.")
    else:
        # Step 7: Prompt Engineering
        prompt = f"""
You are a professional business communication expert.
Write a professional email.

Email Type: {email_type}
Recipient: {recipient}
Sender: {sender}
Company: {company}
Tone: {tone}
Length: {length}
Additional Instructions: {instructions}

Generate only the email.
"""

        # Step 8: Call Ollama
        with st.spinner("Crafting your professional email..."):
            response = chat(
                model="llama3.2",
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )

        # Step 9: Display the Email inside a clean container card
        st.markdown("<br>", unsafe_allow_html=True)
        st.success("Email Generated Successfully")
        
        email_content = response["message"]["content"]
        
        with st.container():
            st.markdown("### Output Result")
            st.markdown(
                f"""<div style="background: white; padding: 20px; border-radius: 8px; border: 1px solid #cbd5e1; color: #0f172a;">
                {email_content.replace('\n', '<br>')}
                </div>""", 
                unsafe_allow_html=True
            )
        
        st.markdown("<br>", unsafe_allow_html=True)

        # Step 10: Download Button
        st.download_button(
            label="Download Email (.txt)",
            data=email_content,
            file_name="generated_email.txt",
            mime="text/plain"
        )

# --- FOOTER ---
st.markdown("""
    <div class="footer">
        <p>AI Smart Email Generator &bull; Built with Streamlit and Ollama (Llama 3.2)</p>
    </div>
""", unsafe_allow_html=True)