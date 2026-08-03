# Project 03 – AI Document Summarizer

An enterprise-grade AI-powered Document Summarization application built using **Python, Streamlit, Ollama, and Llama 3.2**.

This project enables users to upload or paste documents and generate structured AI summaries using a locally running Large Language Model.

It is designed following modern AI Engineering practices with a clean, professional UI and modular architecture.

---

# Project Overview

The AI Document Summarizer helps users quickly understand lengthy documents by generating concise and structured summaries.

Users can:

- Upload PDF documents
- Upload DOCX documents
- Upload TXT files
- Upload Markdown files
- Paste text manually
- Generate AI-powered summaries
- Download generated summaries

---

# Learning Objectives

After completing this project, students will be able to:

- Build AI-powered document processing applications
- Integrate Local LLMs using Ollama
- Design professional Streamlit applications
- Process multiple document formats
- Generate structured summaries using Prompt Engineering
- Create portfolio-ready AI applications

---

# Technologies Used

- Python
- Streamlit
- Ollama
- Llama 3.2
- LangChain (Optional)
- PyPDF2
- python-docx
- Markdown
- CSS

---

# Features

### Document Upload

- PDF
- DOCX
- TXT
- Markdown

### Manual Text Input

Paste text directly into the application.

### AI Summary Modes

- Executive Summary
- Bullet Summary
- Technical Summary
- Business Summary

### Document Statistics

- Characters
- Words
- Estimated Tokens
- Reading Time

### Professional UI

- Enterprise Dashboard
- Dark Theme
- Responsive Layout
- Modular Components

### Export

- Copy Summary
- Download Markdown
- Download Text

---

# Project Structure

```
03_AI_Document_Summarizer/

│── app.py
│── requirements.txt
│── README.md
│── .gitignore

├── assets/
│   ├── theme.css
│   ├── logo.png
│   └── icons/

├── components/
│   ├── header.py
│   ├── sidebar.py
│   ├── upload.py
│   ├── statistics.py
│   ├── output.py
│   └── footer.py

├── utils/
│   ├── file_loader.py
│   ├── summarizer.py
│   ├── prompt_builder.py
│   └── token_counter.py

├── screenshots/
│   ├── home.png
│   ├── upload.png
│   ├── summary.png
│   └── dashboard.png

└── docs/
    ├── Topic_03_LLM_Architectures.pdf
    └── Lab_03_Project_03_AI_Document_Summarizer.pdf
```

---

# Installation

Clone the repository

```bash
git clone https://github.com/Devikadev626/Data-Science-Mastery.git
```

Navigate to the project

```bash
cd "12_AI_Engineering/03_AI_Document_Summarizer"
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate

Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# Run the Application

```bash
streamlit run app.py
```

---

# Workflow

```
Upload Document

↓

Extract Text

↓

Build Prompt

↓

Send to Llama 3.2

↓

Generate Summary

↓

Display Results

↓

Download Summary
```

---

# Supported File Formats

| Format | Supported |
|---------|-----------|
| PDF | Yes |
| DOCX | Yes |
| TXT | Yes |
| Markdown | Yes |

---

# Learning Outcomes

This project demonstrates:

- AI Engineering
- Local LLM Integration
- Prompt Engineering
- Streamlit Development
- Document Processing
- UI Design
- Modular Python Architecture

---

# Future Improvements

- Multi-document summarization
- Chat with uploaded document
- Keyword extraction
- Named Entity Recognition
- Translation
- Audio summary
- Mind Map generation
- Export to PDF
- RAG integration
- Citation generation

---

# Screenshots

```
screenshots/

home.png

upload.png

summary.png

dashboard.png
```

---

# AI Engineering Project Series

| Project | Status |
|----------|--------|
| Project 01 – AI Joke Generator | Completed |
| Project 02 – AI Smart Email Generator | Completed |
| **Project 03 – AI Document Summarizer** | Completed |
| Project 04 – Prompt Playground | Coming Soon |
| Project 05 – AI Chat Assistant | Coming Soon |
| Project 06 – Chat with PDF (RAG) | Coming Soon |

---

# Skills Demonstrated

- Python
- Streamlit
- Ollama
- Llama 3.2
- Prompt Engineering
- Local LLM Integration
- Document Processing
- UI Development
- AI Application Development

---

# Author

**Devika M**

AI Engineer | Data Scientist | Technical Trainer

GitHub

https://github.com/Devikadev626

LinkedIn

(Add your LinkedIn Profile)

---

# License

This project is developed for educational and portfolio purposes as part of the AI Engineering Learning Series.