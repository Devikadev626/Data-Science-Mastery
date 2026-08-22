import logging
from pathlib import Path
from datetime import datetime


SUPPORTED_AUDIO_FORMATS = {
    ".mp3",
    ".wav",
    ".m4a",
    ".flac",
    ".ogg",
    ".aac",
}


def setup_logger(log_file: Path):
    """
    Create and configure project logger.
    """

    logger = logging.getLogger("TranscribeAI")

    # Prevent duplicate handlers
    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # File handler
    file_handler = logging.FileHandler(
        log_file,
        encoding="utf-8"
    )
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger


def validate_audio_file(audio_path):
    """
    Validate whether the audio file exists
    and has a supported extension.
    """

    audio_path = Path(audio_path)

    if not audio_path.exists():
        raise FileNotFoundError(
            f"Audio file not found: {audio_path}"
        )

    if audio_path.suffix.lower() not in SUPPORTED_AUDIO_FORMATS:
        raise ValueError(
            f"Unsupported audio format: {audio_path.suffix}\n"
            f"Supported formats: "
            f"{', '.join(sorted(SUPPORTED_AUDIO_FORMATS))}"
        )

    return audio_path


def save_transcript(
    transcript,
    output_path,
    metadata=None,
):
    """
    Save transcription result as a TXT file.
    """

    output_path = Path(output_path)

    output_path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    with open(
        output_path,
        "w",
        encoding="utf-8"
    ) as file:

        file.write("=" * 60 + "\n")
        file.write("TRANSCRIBEAI TRANSCRIPTION\n")
        file.write("=" * 60 + "\n\n")

        if metadata:

            file.write("METADATA\n")
            file.write("-" * 60 + "\n")

            for key, value in metadata.items():
                file.write(
                    f"{key}: {value}\n"
                )

            file.write("\n")

        file.write("TRANSCRIPTION\n")
        file.write("-" * 60 + "\n")
        file.write(transcript)

        file.write("\n\n")
        file.write("=" * 60 + "\n")

    return output_path


def generate_timestamp():
    """
    Generate timestamp for output file names.
    """

    return datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )