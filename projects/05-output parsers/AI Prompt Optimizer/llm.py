from dotenv import load_dotenv
from langchain_groq import ChatGroq
from models import PromptAnalysis

load_dotenv()

def get_structured_llm():
    llm = ChatGroq(
        model = "llama-3.3-70b-versatile",
        temperature= 0 
    )
    
    structured_llm = llm.with_structured_output(
        PromptAnalysis
    )
    
    return structured_llm


