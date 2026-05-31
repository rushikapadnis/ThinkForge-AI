from dotenv import load_dotenv
import os

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_MODEL = "llama-3.3-70b-versatile"

MAX_REVISIONS = 2
MAX_SUBTOPICS = 4


def get_llm():
    from langchain_groq import ChatGroq
    
    return ChatGroq(
        model=GROQ_MODEL,
        groq_api_key=GROQ_API_KEY,
        temperature=0.3,
    )