from langchain_groq import ChatGroq
from dotenv import load_dotenv
from pydantic import BaseModel


load_dotenv()

llm = ChatGroq(
    model = "llama-3.3-70b-versatile"
)


class Job(BaseModel):
    role: str
    location: str
    skills : list[str]
    experience: int

structured_llm = llm.with_structured_output(Job)


jd = input("Paste your job description here: \n")


response = structured_llm.invoke(jd)


# response = structured_llm.invoke("""

# Python Backend Developer

# Location: Mumbai

# Skills: 
# Python
# Django
# SQL
# Git
# Docker
# React
# Django DRF


# Experience: 2
# """)


print(response)

# print(type(response))

print(response.role)