# TranscribeAI — AI Audio Transcription Platform

TranscribeAI is an AI-powered audio transcription application built with **OpenAI Whisper, Hugging Face Transformers, PyTorch, and Streamlit**.

The application allows users to upload an audio file, select a Whisper model, generate a transcript, review the transcription, and download the result as a `.txt` file.

## Demo

### Streamlit Application

![TranscribeAI Streamlit Application](screenshots/streamlit_transcribeai.png)

## Project Overview

TranscribeAI provides a simple web interface for converting speech from audio files into text using OpenAI Whisper models available through Hugging Face Transformers.

The application is designed as a practical AI engineering project demonstrating:

- Speech-to-text transcription
- Hugging Face model integration
- Whisper model selection
- Streamlit application development
- Temporary audio file handling
- Model caching
- Transcription performance tracking
- Downloadable transcription output

## Features

- Upload audio files directly through the Streamlit interface
- Support multiple audio formats
- Select different Whisper models
- Generate speech-to-text transcripts
- Play uploaded audio before transcription
- Display transcription results in the application
- Download transcripts as `.txt` files
- Display model information
- Display processing device
- Display transcription processing time
- Display transcript character count
- Cache the loaded transcription model for improved application performance
- Premium dark-themed Streamlit interface

## Supported Audio Formats

TranscribeAI currently supports:

- MP3
- WAV
- M4A
- FLAC
- OGG
- AAC

## Available Whisper Models

The application currently provides three Whisper model options:

| Model | Hugging Face Model | Description |
|---|---|---|
| Tiny | `openai/whisper-tiny` | Fastest model for quick testing |
| Base | `openai/whisper-base` | Recommended balance between speed and accuracy |
| Small | `openai/whisper-small` | Better accuracy with slower processing |

The `base` model is selected as the default model in the application.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Application development |
| Streamlit | Web application interface |
| OpenAI Whisper | Speech recognition |
| Hugging Face Transformers | Model loading and inference |
| PyTorch | Deep learning framework |
| pathlib | File and path handling |
| tempfile | Temporary audio file management |

## Project Structure

```text
07_HuggingFace_TranscribeAI/
│
├── app.py
├── model_comparison.py
├── requirements.txt
├── README.md
├── .gitignore
├── .env.example
│
├── src/
│   ├── config.py
│   ├── transcriber.py
│   └── utils.py
│
├── tests/
│   └── test_transcription.py
│
├── screenshots/
│   └── streamlit_transcribeai.png
│
├── audio/
├── data/
├── outputs/
├── results/
└── logs/
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Devikadev626/Data-Science-Mastery.git
```

### 2. Navigate to the project

```bash
cd Data-Science-Mastery/12_AI_Engineering/07_HuggingFace_TranscribeAI
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

#### Windows PowerShell

```powershell
.\.venv\Scripts\Activate.ps1
```

#### Windows Command Prompt

```cmd
.venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

## Running the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your browser.

## How to Use

### Step 1 — Select a Whisper Model

Use the sidebar to select one of the available models:

```text
Tiny
Base
Small
```

### Step 2 — Upload Audio

Upload an audio file using the file uploader.

Supported formats include:

```text
MP3
WAV
M4A
FLAC
OGG
AAC
```

### Step 3 — Review Audio

The application displays the uploaded filename and provides an audio player.

### Step 4 — Generate Transcript

Click:

```text
Generate Transcript
```

The application loads the selected Whisper model and processes the audio.

### Step 5 — Review the Result

The generated transcript is displayed in the application.

The application also displays:

- Selected model
- Processing device
- Transcription processing time
- Number of transcript characters

### Step 6 — Download Transcript

Use:

```text
Download Transcript (.txt)
```

to save the generated transcription as a text file.

## Application Workflow

```text
Audio File
    │
    ▼
Streamlit File Upload
    │
    ▼
Select Whisper Model
    │
    ▼
Temporary Audio File
    │
    ▼
Hugging Face Transformers
    │
    ▼
OpenAI Whisper
    │
    ▼
Speech-to-Text Transcription
    │
    ▼
Transcript
    │
    ├── Display in Streamlit
    │
    └── Download as .txt
```

## Model Loading

The application uses Streamlit resource caching to avoid unnecessarily loading the same Whisper model repeatedly during application interaction.

```python
@st.cache_resource
def load_transcriber(model_name):
    from src.transcriber import WhisperTranscriber

    transcriber = WhisperTranscriber(model_name=model_name)
    transcriber.load_model()

    return transcriber
```

## Model Comparison

The project also contains:

```text
model_comparison.py
```

which can be used to compare the available Whisper models based on transcription performance.

The project can therefore be extended to evaluate the trade-off between:

- Model size
- Processing speed
- Transcription quality
- Hardware requirements

## Testing

Unit tests are maintained inside:

```text
tests/
```

The main transcription test file is:

```text
tests/test_transcription.py
```

Run the test suite using:

```bash
pytest
```

## Practical AI Engineering Concepts Demonstrated

This project demonstrates several practical AI engineering concepts:

1. Hugging Face model integration
2. Transformer-based speech recognition
3. Model selection and comparison
4. Streamlit application development
5. Model caching
6. File upload handling
7. Temporary file management
8. AI inference pipeline development
9. Application-level error handling
10. Performance measurement
11. Automated testing
12. Git and GitHub project management

## Future Improvements

Potential improvements include:

- Speaker diarization
- Timestamped transcription
- Multi-language transcription
- Translation support
- Subtitle generation
- SRT/VTT export
- Batch audio transcription
- GPU acceleration
- Advanced transcription analytics
- Word-level timestamps
- Audio preprocessing
- Docker deployment
- Hugging Face Spaces deployment
- Cloud deployment
- REST API integration

## Learning Objective

The primary objective of TranscribeAI is to demonstrate how a pretrained speech recognition model can be integrated into a practical AI application.

The project combines:

```text
Pretrained AI Model
        +
Hugging Face Transformers
        +
PyTorch
        +
Streamlit
        +
Software Engineering Practices
        =
Practical AI Engineering Application
```

## Author

**Devika M.**

Data Science | AI Engineering | Machine Learning

GitHub:

`https://github.com/Devikadev626`