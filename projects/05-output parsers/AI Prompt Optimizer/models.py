from pydantic import BaseModel, Field


class PromptAnalysis(BaseModel):
    score: int = Field(description= "Prompt quality score from 0 to 100")
    prompt_type: str = Field(
        description="Category of the prompt"
    )
    complexity : str = Field(
        description="Complexity level such as Beginner, Intermediate, or Advanced"
    )
    
    missing_information : list[str] = Field(
        description="Important details missing from the prompt"
    )
    
    potential_problems: list[str] = Field(
        description= "Possible issues that may reduce output quality"
    )
    
    improved_prompt : str = Field(description="Optimized and rewritten prompt")

    recommended_model : str = Field( description="Most suitable AI model for this prompt")

    expected_quality : int = Field(
        description="Expected output quality after optimization from 0 to 100"
    )