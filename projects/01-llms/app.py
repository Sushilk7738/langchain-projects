from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
import os

load_dotenv()

llm = ChatGoogleGenerativeAI(model = "gemini-2.5-flash")


EXPLAIN_PROMPT = "Explain {} in simple terms."

SUMMARIZE_PROMPT="Summarize the following text in simple language: \n\n{}"

TRANSLATE_PROMPT = "Translate the following text into {}:\n\n{}"

INTERVIEW_PROMPT = "GENERATE 10 {} interview questions with answer for a beginner."



def ask_ai(prompt):

    try:
        response = llm.invoke(prompt)
        return response.content
    except Exception as e:
        return f"Error: {e}"

print("=" * 40)
print("        AI Utility Hub")
print("      Powered by Gemini")
print("=" * 40)
while True:
    print("\n============== AI Utility Hub ==============")
    
    print("1. Explain a concept")
    print("2. Summarize Text")
    print("3. Translate Text")
    print("4. Generate Interview Questions")
    print("5. Exit")
        
    
    choice = input("\nEnter your choice: ")

    
    if choice == "1":
        topic = input("\nEnter a topic: ")
        print("\nAI: ", ask_ai(EXPLAIN_PROMPT.format(topic)))

    elif choice == "2":
        text = input("\nEnter the text: ")
        print("\nAI: ", ask_ai(SUMMARIZE_PROMPT.format(text)))


    elif choice == "3":
        language = input("\nEnter target language: ")
        text = input("Enter the text: ")

        print("\nAI: ", ask_ai(TRANSLATE_PROMPT.format(language, text)))
        
    elif choice == "4":
        topic = input("\nEnter topic: ")

        print(f"\nAI: {ask_ai(INTERVIEW_PROMPT.format(topic))}")

    elif choice == "5":
        print("\nThank you for using AI Utility Hub!")    
        break

    else:
        print("\n ❌ Invalid choice! Please enter a number between 1 to 5.")

    