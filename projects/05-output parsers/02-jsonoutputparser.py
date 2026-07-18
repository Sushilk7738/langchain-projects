from dotenv import load_dotenv
from langchain_core.output_parsers import JsonOutputParser
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm = ChatGroq(
    model = "llama-3.3-70b-versatile"
)

parser = JsonOutputParser()

prompt = PromptTemplate(
    template="""
Generate ONLY the following fields.

- product_name
- price
- features

{format_instructions}

Product:
{product}
""",
    input_variables=['product'],
    partial_variables= {
        "format_instructions": parser.get_format_instructions()
    },
)


chain = prompt | llm | parser

response = chain.invoke({
    "product": "iphone 17"
})

print(response)
print(type(response))
