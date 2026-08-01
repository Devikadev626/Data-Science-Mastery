# AI Smart Email Generator

A professional AI-powered Email Generator developed using **Python**, **Streamlit**, and **Ollama (Llama 3.2)**. This project demonstrates Prompt Engineering concepts by generating professional emails locally using a Large Language Model (LLM) without relying on cloud APIs.

---

## Project Overview

The AI Smart Email Generator allows users to generate different types of professional emails by selecting the email category, tone, language, and length. The application builds a structured prompt and sends it to a locally running Llama 3.2 model through Ollama.

This project is part of the **AI Engineering Lab Series**, focusing on Prompt Engineering and Local LLM Integration.

---

## Features

- Professional Streamlit User Interface
- Local AI using Ollama
- Powered by Llama 3.2
- Prompt Engineering Demonstration
- Multiple Email Types
- Multiple Tone Selection
- Language Selection
- Adjustable Email Length
- Prompt Preview
- Download Generated Email
- Input Validation

---

## Technologies Used

- Python
- Streamlit
- Ollama
- Llama 3.2
- Prompt Engineering

---

## Project Structure

```
02_AI_Smart_Email_Generator
│
├── app.py
├── README.md
├── requirements.txt
├── .gitignore
│
├── assets
├── docs
├── images
└── prompts
```

---

## Application Workflow

```
User Input
      │
      ▼
Prompt Construction
      │
      ▼
Ollama
      │
      ▼
Llama 3.2
      │
      ▼
AI Generated Email
      │
      ▼
Display Output
      │
      ▼
Download Email
```

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/yourusername/02_AI_Smart_Email_Generator.git
```

Navigate to the project directory.

```bash
cd 02_AI_Smart_Email_Generator
```

---

## Create a Virtual Environment

```bash
python -m venv .venv
```

### Activate the Virtual Environment

Windows

```bash
.venv\Scripts\activate
```

---

## Install Required Packages

```bash
pip install -r requirements.txt
```

---

## Install Ollama

Verify installation.

```bash
ollama --version
```

Download the required model.

```bash
ollama pull llama3.2
```

Verify the downloaded model.

```bash
ollama list
```

---

## Run the Project

Open the project directory.

Activate the virtual environment.

Run the application.

```bash
streamlit run app.py
```

The application will open in your browser.

```
http://localhost:8501
```

---

## Example Usage

1. Select the Email Type.
2. Select the Tone.
3. Select the Language.
4. Choose the Email Length.
5. Enter the Recipient Name.
6. Enter the Sender Name.
7. Enter the Company Name.
8. Add Additional Instructions.
9. Click **Generate Email**.
10. Download the generated email if required.

---

## Screenshots

### Home Page

```
images/home_page.png
```

### Sidebar

```
images/sidebar.png
```

### Prompt Preview

```
images/prompt_preview.png
```

### Generated Email

```
images/generated_email.png
```

---

## Learning Outcomes

After completing this project, learners will be able to:

- Build AI-powered web applications using Streamlit.
- Integrate local Large Language Models using Ollama.
- Design effective prompts using Prompt Engineering.
- Understand prompt construction and AI response generation.
- Build user-friendly interfaces for AI applications.
- Download AI-generated content.
- Apply input validation and error handling.

---

## Future Improvements

- Email Templates
- PDF Export
- DOCX Export
- Copy to Clipboard
- Email History
- Dark and Light Themes
- Voice Input
- Cloud Deployment
- Multi-language Support
- OpenAI API Integration

---

## Requirements

- Python 3.10+
- Ollama
- Llama 3.2 Model
- Streamlit
- Internet connection (only for initial package/model download)

---

## Author

**AI Engineering Lab Series**

Project developed for learning **Generative AI**, **Prompt Engineering**, **Local LLM Integration**, and **AI Application Development** using Python, Streamlit, and Ollama.

---

## License

This project is intended for educational and learning purposes.