from langchain_groq import ChatGroq
from settings import Settings

settings = Settings() 

class GroqModel:
    def __init__(self, tools=None) -> None:
        self.model_name = settings.MODEL_NAME
        self.api_key = settings.GROQ_API_KEY
        self.tavily_api = settings.TAVILY_API
        self.tools = tools

        self.model = self._init_model()

    def _init_model(self) -> ChatGroq:
        return ChatGroq(
            model=self.model_name,
            api_key=self.api_key,
            temperature=0.1,
            max_retries=2,
        )
    