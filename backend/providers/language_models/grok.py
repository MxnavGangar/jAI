from openai import OpenAI

from providers.language_models.base import LLMProvider
from core.settings import settings


class GrokProvider(LLMProvider):

    def __init__(self):
        self.client = OpenAI(
            api_key=settings.grok_api_key,
            base_url="https://api.x.ai/v1"
        )

    def generate(self, prompt: str) -> str:

        response = self.client.chat.completions.create(
            model="grok-3-mini",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response.choices[0].message.content