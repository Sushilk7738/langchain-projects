from dotenv import load_dotenv
from langchain_groq import ChatGroq


load_dotenv()

llm = ChatGroq(model = "llama-3.3-70b-versatile")


retry_llm = llm.with_retry(
    stop_after_attempt=3
)


response = retry_llm.invoke(
    "Explain langchain in one sentence."
)


print(response.content)