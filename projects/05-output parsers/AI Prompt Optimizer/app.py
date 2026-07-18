from langchain_core.messages import SystemMessage, HumanMessage
from llm import get_structured_llm
from prompt import SYSTEM_PROMPT


def main():
    print("=" * 60)
    print("✨ PromptForge AI")
    print("=" * 60)


    user_prompt = input("\n\nEnter your prompt:\n>")

    llm = get_structured_llm()

    response = llm.invoke(
        [
            SystemMessage(content=SYSTEM_PROMPT),
            HumanMessage(content=user_prompt)
        ]
    )
    
    
    print("\n"+ "="*60)
    print("📊 PROMPT ANALYSIS")
    print("=" * 60)

    print(f"\n⭐ Prompt Score       : {response.score}/100")
    print(f"📌 Prompt Type          : {response.prompt_type}")
    print(f"📈 Complexity           : {response.complexity}")
    print(f"🤖 Recommended Model    : {response.recommended_model}")
    print(f"🎯 Expected Quality     : {response.expected_quality}%")


    print("\n❌ Missing Information")
    print("-"*60)

    for item in response.missing_information:
        print(f"💠 {item}")
        
    print("\n❌ Potential Problems")
    print("-"*60)
    
    for item in response.potential_problems:
        print(f"💀 {item}")
    
    print("\n❌ Optimized Prompt")
    print("-"*60)
    
    print(response.improved_prompt)

    print("\n" + "="*60)
    

if __name__ == "__main__":
    main()