from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(
    model = "llama-3.3-70b-versatile"
)


SYSTEM_PROMPT = """
You're a helpful AI assistant.
Always be consice and direct.
Always answer politely
"""

SYSTEM_MESSAGE = SystemMessage(content=SYSTEM_PROMPT)
messages = []
while True:
    user_input = input("\nYou: ")
    
    if user_input.lower() == "exit":
        print("\nGoodbye!")
        break

    elif user_input.lower() == '/clear':
        messages = [SYSTEM_MESSAGE]
        print("Conversation cleared.")
        continue

    elif user_input.lower() == '/history':
        print('\n' + '='*45)
        print("      Conversation History")
        print('='*45)
        for message in messages:
            if isinstance(message, HumanMessage):
                print(F"🙍 You: {message.content}")
            elif isinstance(message, AIMessage):
                print(f"🤖 AI: {message.content}")
        
    messages.append(
        HumanMessage(content=user_input)
    )

    response = llm.invoke(messages)

    ai_response = response.content
    print("\nAI: ",ai_response)
    
    messages.append(
        AIMessage(content=ai_response)
    )
    

