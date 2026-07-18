from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(model="llama-3.3-70b-versatile")

template = PromptTemplate(
    template="""

    You're a professional email writing assistant.
    
    Write a {tone} email.
    
    Sender: {sender}
    Recipient: {recipient}
    Purpose: {purpose}

    Maximum_words: {word_limit}

    Instructions: 
    - Keep the email within the given word limit.
    - Use an appropriate subject line.
    - Use a professional greeting.
    - Do not invent unnecessary details.
    - End with:
    Regards,
    {sender}
    
    """,
    
    input_variables= ["tone", "purpose", "recipient", "word_limit"],
    partial_variables= {
        'sender': "Meta"
    }
)

recipient = input("Enter recipient: ")
purpose = input("Enter purpose: ")
tone = input("Enter tone: ")
word_limit = input("Maximum words: ")




prompt = template.invoke({
    "recipient" : recipient,
    "purpose": purpose,
    "tone": tone,
    "word_limit": word_limit
})


response = llm.invoke(prompt)
print(response.content)
