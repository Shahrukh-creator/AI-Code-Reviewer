import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI


load_dotenv()


class LLMService:
    def __init__(self):
        self.llm = ChatOpenAI(
            model="gpt-5.6-sol",
            api_key=os.getenv("OPENAI_API_KEY"),
            temperature=0,
        )

    def get_llm(self):
        return self.llm