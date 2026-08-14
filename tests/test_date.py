from datetime import datetime
import json
from ollama import chat
import sys

def read_training() -> str:
    """Loads Happy's prompt training.

    This function makes it more efficient for testing compared to changing
    each individual testing section in each test file when prompt engineering
    changes are made.
    
    Returns:
        A string containing all of Happy's prompt training from the 'happy.json' file.
        
    Raises:
        Exception: If json file cannot be opened.
    """
    happyTraining = ""
    
    try:
        with open("happy.json", "r") as file:
            happyTraining = json.load(file)
            
    except Exception as e:
        print("\nError: Test cannot be executed because Happy's prompt training file cannot be located.")
        sys.exit()
    
    return happyTraining

def run_test() -> None:
    """The test function for the AI."""
    messages = [
        {
            "role": "system",
            "content": """
{read_training()}
"""
            }
        ]
    
    print()
        
    messages.append({"role": "user", "content": f"Display the current date and time today to the user using {datetime.now()}"})
        
    response = chat(model="samantha-mistral:latest", messages=messages)
    answer = response["message"]["content"]
    
    print("\nHappy:\n", answer, "\n\n")
    # Happy will output:
    #
    # "Hello! Today is (Current day of the week), (Month) (Day), (Year). The current time is (Current time). What would you like to talk about today?"
    #
    # Happy will not output this exactly verbatim.
        
    messages.append({"role": "assistant", "content": answer})


if __name__ == "__main__":
    """Checks if the file is directly ran."""
    run_test()