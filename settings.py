from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os 

load_dotenv()

class Settings(BaseSettings):
    GROQ_API_KEY: str = os.getenv("GROQ_API")
    MODEL_NAME: str = os.getenv("MODEL_NAME")
    TAVILY_API: str = os.getenv("TAVILY_API")