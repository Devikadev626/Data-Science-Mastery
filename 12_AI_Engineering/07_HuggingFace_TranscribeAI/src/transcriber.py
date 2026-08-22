import time
from pathlib import Path

import torch
from transformers import (
    AutoModelForSpeechSeq2Seq,
    AutoProcessor,
    pipeline,
)

from src.config import DEFAULT_MODEL
from src.utils import validate_audio_file


class WhisperTranscriber:

    def __init__(
        self,
        model_name=DEFAULT_MODEL,
    ):
        """
        Initialize the Whisper transcriber.
        """

        self.model_name = model_name
        self.device = self._get_device()

        self.dtype = (
            torch.float16
            if self.device == "cuda"
            else torch.float32
        )

        self.pipe = None

    def _get_device(self):
        """
        Detect GPU or CPU.
        """

        if torch.cuda.is_available():

            print(
                f"GPU detected: "
                f"{torch.cuda.get_device_name(0)}"
            )

            return "cuda"

        print("GPU not detected. Using CPU.")

        return "cpu"

    def load_model(self):
        """
        Load Whisper model and processor.
        """

        print("\nLoading Whisper model...")
        print(f"Model: {self.model_name}")
        print(f"Device: {self.device}")

        start_time = time.time()

        model = AutoModelForSpeechSeq2Seq.from_pretrained(
            self.model_name,
            torch_dtype=self.dtype,
            low_cpu_mem_usage=True,
        )

        model.to(self.device)

        processor = AutoProcessor.from_pretrained(
            self.model_name
        )

        pipeline_device = (
            0
            if self.device == "cuda"
            else -1
        )

        self.pipe = pipeline(
            task="automatic-speech-recognition",
            model=model,
            tokenizer=processor.tokenizer,
            feature_extractor=processor.feature_extractor,
            torch_dtype=self.dtype,
            device=pipeline_device,
        )

        load_time = time.time() - start_time

        print(
            f"Model loaded successfully "
            f"in {load_time:.2f} seconds!"
        )

    def transcribe(
        self,
        audio_path,
        language=None,
    ):
        """
        Transcribe an audio file.
        """

        if self.pipe is None:
            raise RuntimeError(
                "Model is not loaded. "
                "Call load_model() first."
            )

        audio_path = validate_audio_file(
            audio_path
        )

        print("\nTranscribing audio...")
        print(f"File: {audio_path.name}")

        start_time = time.time()

        generate_kwargs = {
            "task": "transcribe"
        }

        # Optional language specification
        if language:
            generate_kwargs["language"] = language

        result = self.pipe(
            str(audio_path),
            generate_kwargs=generate_kwargs,
        )

        transcription_time = (
            time.time() - start_time
        )

        transcript = result["text"].strip()

        return {
            "text": transcript,
            "model": self.model_name,
            "device": self.device,
            "audio_file": audio_path.name,
            "transcription_time": round(
                transcription_time,
                2,
            ),
        }