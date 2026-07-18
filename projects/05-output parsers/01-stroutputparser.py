from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq


load_dotenv()

llm =  ChatGroq(
    model = 'llama-3.3-70b-versatile'
)

prompt = PromptTemplate(
    template="Generate a professional email subject for: {topic}",
    input_variables=['topic']
)

parser = StrOutputParser()

chain = prompt | llm | parser

response = chain.invoke({
    "topic": "Python interview job offer letter"
})


# print(response)

# print(type(response))

# print(isinstance(response, str))

# res = response.upper()
# print(res)

without_parser = (prompt | llm).invoke(
    {
        "topic": "Python interview job offer letter"
    }
)

print(type(without_parser))
print(without_parser)














"""
What is StrOutputParser?

StrOutputParser converts the LLM's response object into a plain Python string.

"""

