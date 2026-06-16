from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    app_name: str = "JAI Core"

    llm_provider: str
    embedding_provider: str
    vectorstore_provider: str

    groq_api_key: str

    class Config:
        env_file = ".env"


settings = Settings()