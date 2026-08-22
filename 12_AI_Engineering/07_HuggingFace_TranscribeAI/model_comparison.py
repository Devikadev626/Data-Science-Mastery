import sys
import time
import csv
from pathlib import Path


# Add project folder to Python path
PROJECT_ROOT = Path(__file__).resolve().parent
sys.path.append(str(PROJECT_ROOT))


from src.transcriber import WhisperTranscriber
from src.config import AUDIO_DIR, AVAILABLE_MODELS


# ---------------------------------------------------------
# CONFIGURATION
# ---------------------------------------------------------

MODEL_KEYS = [
    "tiny",
    "base",
    "small",
]


RESULTS_DIR = PROJECT_ROOT / "results"
RESULTS_FILE = RESULTS_DIR / "model_comparison.csv"


# ---------------------------------------------------------
# GET AUDIO FILE
# ---------------------------------------------------------

def get_audio_file():

    supported_formats = [
        ".mp3",
        ".wav",
        ".m4a",
        ".flac",
        ".ogg",
        ".aac",
    ]

    audio_files = [
        file
        for file in AUDIO_DIR.iterdir()
        if file.is_file()
        and file.suffix.lower() in supported_formats
    ]

    if not audio_files:
        raise FileNotFoundError(
            f"No supported audio file found in:\n"
            f"{AUDIO_DIR}"
        )

    return audio_files[0]


# ---------------------------------------------------------
# COMPARE MODELS
# ---------------------------------------------------------

def compare_models(audio_path):

    results = []

    print("\n" + "=" * 70)
    print("WHISPER MODEL COMPARISON")
    print("=" * 70)

    print(f"\nAudio File: {audio_path.name}")

    for model_key in MODEL_KEYS:

        model_name = AVAILABLE_MODELS[model_key]

        print("\n" + "-" * 70)
        print(f"TESTING: Whisper {model_key.upper()}")
        print(f"Model: {model_name}")
        print("-" * 70)

        try:

            # Measure total time
            total_start_time = time.time()

            # Create transcriber
            transcriber = WhisperTranscriber(
                model_name=model_name
            )

            # Load model
            transcriber.load_model()

            # Transcribe
            result = transcriber.transcribe(
                audio_path
            )

            total_time = (
                time.time()
                - total_start_time
            )

            # Store result
            result_data = {
                "model_key": model_key,
                "model_name": model_name,
                "device": result["device"],
                "transcription_time": result[
                    "transcription_time"
                ],
                "total_time": round(
                    total_time,
                    2
                ),
                "transcript_length": len(
                    result["text"]
                ),
                "transcript": result["text"],
                "status": "SUCCESS",
            }

            results.append(result_data)

            print("\nRESULT")

            print(
                f"Transcription Time: "
                f"{result['transcription_time']} seconds"
            )

            print(
                f"Total Time: "
                f"{total_time:.2f} seconds"
            )

            print(
                f"Transcript Length: "
                f"{len(result['text'])} characters"
            )

            print("\nTranscript:")

            print(result["text"])

            # Free model before next comparison
            del transcriber

            # Clear GPU memory
            try:
                import torch

                if torch.cuda.is_available():
                    torch.cuda.empty_cache()

            except Exception:
                pass

        except Exception as error:

            print(
                f"\nERROR testing {model_name}:"
            )

            print(error)

            results.append({
                "model_key": model_key,
                "model_name": model_name,
                "device": "N/A",
                "transcription_time": "N/A",
                "total_time": "N/A",
                "transcript_length": 0,
                "transcript": "",
                "status": "FAILED",
            })

    return results


# ---------------------------------------------------------
# SAVE RESULTS TO CSV
# ---------------------------------------------------------

def save_results(results):

    RESULTS_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    fieldnames = [
        "model_key",
        "model_name",
        "device",
        "transcription_time",
        "total_time",
        "transcript_length",
        "transcript",
        "status",
    ]

    with open(
        RESULTS_FILE,
        "w",
        newline="",
        encoding="utf-8",
    ) as file:

        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames,
        )

        writer.writeheader()

        writer.writerows(
            results
        )

    print("\n" + "=" * 70)
    print("RESULTS SAVED")
    print("=" * 70)

    print(
        f"\nFile:\n{RESULTS_FILE}"
    )


# ---------------------------------------------------------
# DISPLAY SUMMARY
# ---------------------------------------------------------

def display_summary(results):

    print("\n" + "=" * 70)
    print("MODEL COMPARISON SUMMARY")
    print("=" * 70)

    print(
        f"{'MODEL':<10}"
        f"{'DEVICE':<10}"
        f"{'TRANSCRIBE':<15}"
        f"{'TOTAL':<12}"
        f"{'STATUS':<10}"
    )

    print("-" * 70)

    for result in results:

        print(
            f"{result['model_key']:<10}"
            f"{str(result['device']):<10}"
            f"{str(result['transcription_time']):<15}"
            f"{str(result['total_time']):<12}"
            f"{result['status']:<10}"
        )

    print("=" * 70)


# ---------------------------------------------------------
# MAIN
# ---------------------------------------------------------

def main():

    print("\nSTARTING WHISPER MODEL COMPARISON")

    try:

        # Get audio
        audio_path = get_audio_file()

        # Compare models
        results = compare_models(
            audio_path
        )

        # Display results
        display_summary(
            results
        )

        # Save results
        save_results(
            results
        )

        print(
            "\nModel comparison completed successfully!"
        )

    except Exception as error:

        print(
            "\nMODEL COMPARISON FAILED"
        )

        print(
            f"Error: {error}"
        )


if __name__ == "__main__":
    main()