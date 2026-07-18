from dotenv import load_dotenv
from pydantic import BaseModel, Field
from langchain_groq import ChatGroq


class Product(BaseModel):
    name: str = Field(description="Product name")
    price: int = Field(description="Product price")
    features: list[str] = Field(description="Main Features")

load_dotenv()

llm = ChatGroq(model = "llama-3.3-70b-versatile")

structred_llm = llm.with_structured_output(Product)


response = structred_llm.invoke(
    "Generate details about iphone 17."
)


print(response)
print(type(response))
print(response.name)
print(response.price)
print(response.features)