"""
providers.py

Handles communication with multiple AI providers.

Supported Providers
-------------------
1. OpenAI
2. Google Gemini
3. Groq
4. Anthropic Claude

Author: IPCS AI Engineering Program
"""

import google.generativeai as genai
from openai import OpenAI
from anthropic import Anthropic
from groq import Groq

from config import (
    OPENAI_API_KEY,
    GEMINI_API_KEY,
    GROQ_API_KEY,
    ANTHROPIC_API_KEY
)


class AIProvider:
    """Unified interface for multiple AI providers."""

    def __init__(self):

        if OPENAI_API_KEY:
            self.openai = OpenAI(api_key=OPENAI_API_KEY)
        else:
            self.openai = None

        if GEMINI_API_KEY:
            genai.configure(api_key=GEMINI_API_KEY)

        if GROQ_API_KEY:
            self.groq = Groq(api_key=GROQ_API_KEY)
        else:
            self.groq = None

        if ANTHROPIC_API_KEY:
            self.claude = Anthropic(api_key=ANTHROPIC_API_KEY)
        else:
            self.claude = None

    ######################################################
    # OPENAI
    ######################################################

    def ask_openai(
        self,
        model,
        system_prompt,
        prompt,
        temperature,
        max_tokens
    ):

        response = self.openai.chat.completions.create(

            model=model,

            messages=[
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],

            temperature=temperature,

            max_tokens=max_tokens
        )

        return {
            "response": response.choices[0].message.content,
            "input_tokens": response.usage.prompt_tokens,
            "output_tokens": response.usage.completion_tokens,
            "total_tokens": response.usage.total_tokens
        }

    ######################################################
    # GEMINI
    ######################################################

    def ask_gemini(
        self,
        model,
        system_prompt,
        prompt,
        temperature,
        max_tokens
    ):

        model = genai.GenerativeModel(model)

        response = model.generate_content(
            f"{system_prompt}\n\n{prompt}"
        )

        return {

            "response": response.text,

            "input_tokens": 0,

            "output_tokens": 0,

            "total_tokens": 0

        }

    ######################################################
    # GROQ
    ######################################################

    def ask_groq(
        self,
        model,
        system_prompt,
        prompt,
        temperature,
        max_tokens
    ):

        response = self.groq.chat.completions.create(

            model=model,

            messages=[
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],

            temperature=temperature,

            max_tokens=max_tokens

        )

        return {

            "response": response.choices[0].message.content,

            "input_tokens": response.usage.prompt_tokens,

            "output_tokens": response.usage.completion_tokens,

            "total_tokens": response.usage.total_tokens

        }

    ######################################################
    # ANTHROPIC
    ######################################################

    def ask_claude(
        self,
        model,
        system_prompt,
        prompt,
        temperature,
        max_tokens
    ):

        response = self.claude.messages.create(

            model=model,

            max_tokens=max_tokens,

            temperature=temperature,

            system=system_prompt,

            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]

        )

        return {

            "response": response.content[0].text,

            "input_tokens": response.usage.input_tokens,

            "output_tokens": response.usage.output_tokens,

            "total_tokens": response.usage.input_tokens
            + response.usage.output_tokens

        }

    ######################################################
    # COMMON FUNCTION
    ######################################################

    def generate(
        self,
        provider,
        model,
        system_prompt,
        prompt,
        temperature,
        max_tokens
    ):

        if provider == "OpenAI":
            return self.ask_openai(
                model,
                system_prompt,
                prompt,
                temperature,
                max_tokens
            )

        elif provider == "Google Gemini":
            return self.ask_gemini(
                model,
                system_prompt,
                prompt,
                temperature,
                max_tokens
            )

        elif provider == "Groq":
            return self.ask_groq(
                model,
                system_prompt,
                prompt,
                temperature,
                max_tokens
            )

        elif provider == "Anthropic":
            return self.ask_claude(
                model,
                system_prompt,
                prompt,
                temperature,
                max_tokens
            )

        else:
            raise ValueError("Unsupported Provider")