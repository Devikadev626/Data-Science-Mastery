"""
config.py

Loads application configuration and environment variables.
"""

from dotenv import load_dotenv
import os

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")

APP_NAME = "Enterprise AI API Integration Assistant"

DEFAULT_PROVIDER = "OpenAI"

SUPPORTED_PROVIDERS = [
    "OpenAI",
    "Google Gemini",
    "Groq",
    "Anthropic"
]