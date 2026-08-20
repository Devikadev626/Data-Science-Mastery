"""
Module Description: Centralized configuration management module for the Enterprise Multi-LLM Playground.
                   Provides dataclasses and global constants for Ollama endpoints, default paths,
                   UI metrics, and runtime settings.
Author: IPCS AI Engineering Team
Project Name: Enterprise Multi-LLM Playground (AIE-P04)
"""

import os
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class OllamaConfig:
    """Configuration settings for Ollama local server connection and execution."""

    BASE_URL: str = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
    API_TAGS_ENDPOINT: str = f"{BASE_URL}/api/tags"
    API_GENERATE_ENDPOINT: str = f"{BASE_URL}/api/generate"
    API_SHOW_ENDPOINT: str = f"{BASE_URL}/api/show"
    DEFAULT_TIMEOUT: float = 120.0  # seconds per inference request
    CONCURRENT_MAX_WORKERS: int = 5  # Max async parallel workers


@dataclass(frozen=True)
class PathConfig:
    """Centralized filesystem directory and file path configurations."""

    BASE_DIR: Path = Path(__file__).resolve().parent
    ASSETS_DIR: Path = BASE_DIR / "assets"
    SCREENSHOTS_DIR: Path = BASE_DIR / "screenshots"
    STYLES_DIR: Path = BASE_DIR / "styles"
    
    # File Paths
    CSS_FILE: Path = STYLES_DIR / "style.css"
    MODELS_JSON_FILE: Path = BASE_DIR / "models.json"


@dataclass(frozen=True)
class UIConfig:
    """Visual theme constants, default parameters, and display limitations."""

    PAGE_TITLE: str = "Enterprise Multi-LLM Playground"
    PAGE_ICON: str = "⚡"
    LAYOUT: str = "wide"
    INITIAL_SIDEBAR_STATE: str = "expanded"
    
    # Text Input Limits
    MAX_PROMPT_LENGTH: int = 4096
    
    # Chart & Color Theme Settings
    THEME_PRIMARY_COLOR: str = "#00D2FF"
    THEME_SECONDARY_COLOR: str = "#0072FF"
    THEME_BG_DARK: str = "#0E1117"
    THEME_CARD_BG: str = "#1E222D"
    
    # Default Inference Parameters
    DEFAULT_TEMPERATURE: float = 0.7
    DEFAULT_TOP_P: float = 0.9
    DEFAULT_MAX_TOKENS: int = 512


@dataclass(frozen=True)
class ExportConfig:
    """Settings for benchmarking report exports."""

    DEFAULT_CSV_FILENAME: str = "llm_benchmark_results.csv"
    DEFAULT_JSON_FILENAME: str = "llm_benchmark_results.json"


# Instantiate globally accessible singletons
OLLAMA_CONFIG = OllamaConfig()
PATH_CONFIG = PathConfig()
UI_CONFIG = UIConfig()
EXPORT_CONFIG = ExportConfig()