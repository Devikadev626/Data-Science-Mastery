from pathlib import Path
import sys


# Add project root to Python path
PROJECT_ROOT = Path(__file__).resolve().parent.parent

sys.path.append(
    str(PROJECT_ROOT)
)


from src.transcriber import WhisperTranscriber
from src.config import (
    AUDIO_DIR,
    TRANSCRIPT_DIR,
    LOG_DIR,
)
from src.utils import (
    setup_logger,
    save_transcript,
    generate_timestamp,
)


def main():

    # Setup logger
    logger = setup_logger(
        LOG_DIR / "transcribeai.log"
    )

    logger.info(
        "Starting TranscribeAI"
    )

    print("=" * 60)
    print("TRANSCRIBEAI")
    print("Whisper Audio Transcription System")
    print("=" * 60)

    # Find audio files
    audio_files = list(
        AUDIO_DIR.glob("*")
    )

    audio_files = [
        file
        for file in audio_files
        if file.is_file()
    ]

    if not audio_files:

        print(
            f"\nNo audio files found in:\n"
            f"{AUDIO_DIR}"
        )

        print(
            "\nAdd an audio file and run again."
        )

        return

    # Use first audio file
    audio_path = audio_files[0]

    print(
        f"\nAudio selected: "
        f"{audio_path.name}"
    )

    try:

        # Create transcriber
        transcriber = WhisperTranscriber(
            model_name="openai/whisper-base"
        )

        # Load model
        transcriber.load_model()

        # Transcribe
        result = transcriber.transcribe(
            audio_path
        )

        print("\n" + "=" * 60)
        print("TRANSCRIPTION RESULT")
        print("=" * 60)

        print(result["text"])

        print("=" * 60)

        print(
            f"\nModel: "
            f"{result['model']}"
        )

        print(
            f"Device: "
            f"{result['device']}"
        )

        print(
            f"Transcription time: "
            f"{result['transcription_time']} seconds"
        )

        # Save transcript
        timestamp = generate_timestamp()

        output_file = (
            TRANSCRIPT_DIR
            / f"transcript_{timestamp}.txt"
        )

        metadata = {
            "Audio File":
                result["audio_file"],
            "Model":
                result["model"],
            "Device":
                result["device"],
            "Transcription Time":
                f"{result['transcription_time']} seconds",
        }

        saved_path = save_transcript(
            transcript=result["text"],
            output_path=output_file,
            metadata=metadata,
        )

        print(
            f"\nTranscript saved to:\n"
            f"{saved_path}"
        )

        logger.info(
            "Transcription completed successfully"
        )

    except Exception as error:

        logger.exception(
            "Transcription failed"
        )

        print(
            "\nERROR:"
        )

        print(error)


if __name__ == "__main__":
    main()