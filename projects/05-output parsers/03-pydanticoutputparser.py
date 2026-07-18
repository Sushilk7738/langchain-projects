from dotenv import load_dotenv
from pydantic import BaseModel, Field
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser


load_dotenv()

class Product(BaseModel):
    name: str = Field(description="Name of the product")
    price: int = Field(description = "Price of the product in INR")
    features: list[str] = Field(description="Main features")

parser = PydanticOutputParser(pydantic_object=Product)

llm = ChatGroq(
    model= 'llama-3.3-70b-versatile'
)


prompt = PromptTemplate(
    template="""
    
    Generate product details.
    {format_instructions}

    Product:
    {product}
    """,
    
    input_variables=["product"],
    partial_variables= {
        "format_instructions": parser.get_format_instructions()
    }
)

chain = prompt | llm | parser

response = chain.invoke({
    "product": "iPhone 17"
})


print(response)
print(type(response))


print(response.name)
print(response.price)
print(response.features)
