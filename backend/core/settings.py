from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    llm_provider: str = "grok"
    embedding_provider: str = "bge"
    vectorstore_provider: str = "chroma"

    grok_api_key: str

    class Config:
        env_file = ".env"


settings = Settings()