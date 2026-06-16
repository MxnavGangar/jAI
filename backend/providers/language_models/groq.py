from groq import Groq

from core.settings import settings
from providers.language_models.base import (
    LLMProvider
)


class GroqProvider(LLMProvider):

    def __init__(self):

        self.client = Groq(
            api_key=settings.groq_api_key
        )

    def generate(
        self,
        system_prompt: str,
        user_prompt: str
    ):

        response = (
            self.client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[
                    {
                        "role": "system",
                        "content": system_prompt
                    },
                    {
                        "role": "user",
                        "content": user_prompt
                    }
                ],
                temperature=0.2
            )
        )

        return (
            response
            .choices[0]
            .message
            .content
        )