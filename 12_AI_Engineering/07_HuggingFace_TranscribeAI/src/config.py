from pathlib import Path
import os


# Project root directory
BASE_DIR = Path(__file__).resolve().parent.parent


# Data directories
DATA_DIR = BASE_DIR / "data"
AUDIO_DIR = DATA_DIR / "audio"


# Output directories
OUTPUT_DIR = BASE_DIR / "outputs"
TRANSCRIPT_DIR = OUTPUT_DIR / "transcripts"


# Log directory
LOG_DIR = BASE_DIR / "logs"


# Create directories automatically
for directory in [
    AUDIO_DIR,
    TRANSCRIPT_DIR,
    LOG_DIR,
]:
    directory.mkdir(parents=True, exist_ok=True)


# Hugging Face Whisper models
AVAILABLE_MODELS = {
    "tiny": "openai/whisper-tiny",
    "base": "openai/whisper-base",
    "small": "openai/whisper-small",
}


# Default model
DEFAULT_MODEL = os.getenv(
    "WHISPER_MODEL",
    "openai/whisper-base"
)


# Default task
DEFAULT_TASK = "transcribe"