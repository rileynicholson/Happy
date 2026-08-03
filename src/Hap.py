import atexit
import datetime
import json
from ollama import chat
from pathlib import Path

"""
Ideas that I was thinking for this project:

-Happy doesn't have to be/act human to have appeal. It can be warm, curious, encouraging, and honest about what it is to have appeal.

-I say the main stuff Happy can do can be:
    -Listen and ask thoughtful questions.
    -Suggest evidence-based coping strategies and self-help techniques.
    -Encourage healthy habits and reflection.
    -Recommend professional help with situations that sound serious or persistant to Happy.

-I want Happy to be able to detect time that has elapsed too, I want him to say something like:
    "Three months ago, you told me you were scared of joining clubs or being in public spaces. Last week,
    you told me you joined a club and even hung out with the club beyond club events. That's a meaningful step
    towards the confidence you told me you wanted to build."
    
-I want Happy to detect the significance of certain events/prompts the user tells Happy about.

-In order to get that "Happy remembering information" aspect, I was thinking of having 2 save files/json files to store information.
    -One of the files can be for the user and saves every single prompt the user has sent to Happy.
    -The other file can be for Happy and can take the conversation when it is finished, summarize it and include key points,
    and store it within its own file.
    -I feel like this design would be efficient and at the very least, be a good starting blueprint for Happy.
    
-One of the major hurdles I want to do differently from J.A.R.V.I.S is accessibility.
    -J.A.R.V.I.S requires a lot of installation whether it is external libraries or the Ollama model itself (which is 9.1 GB, HUGE).
    -I want this project to have a smaller AI model that still fits the project well.
    -I also want this project to include as few external libraries as possible, which should not be too challenging for this project.


-Two Json files + Ollama + A good prompt with some prompt engineering could really make something impactful.
"""

def New_Page() -> None:
    """Space out the outputs of Happy for formatting."""
    for i in range(100):
        print()
        
def Read_SaveFile(messages: list[dict[str, str]]) -> None:
    """Takes the conversation summarizations from the JSON save file and appends them into the message history. Happens before a conversation.

    Args:
        messages: The overall scope of the conversation and system instructions.
        
    Raises:
        Exception: If file cannot be opened.
    """
    # In contrast to 'Write_SaveFile', this function will be used before a conversation starts.
    # I am planning to have this method read summarizations of past conversations by the AI then append the summarizations to 'messages'.
    # The summarizations will probably be appended under the role of 'system' instead of assistant or user.
    # I will have to make sure each of the summarizations consist of the starting phrase, "Conversation on (date) summarization: " to indicate it as a past conversation.
    # I want to make sure the AI can differentiate between from a past conversation to prompt engineering especially if both will be under the 'system' role.
    # I think how I am going to handle the two file design idea in relation to this is I am going to have the function read from a JSON of summarizations of what the AI said.
    # Then I will have the function read from a JSON of summarizations of what the user said in the same conversation on the same date.
    # I might even have conversation numbers within the JSON files to sort the summarizations together, but I am not entirely sure yet.
    # 
    # Work In Progress (WIP)
    userlogs = Path("userlogs.json")
    happylogs = Path("happylogs.json")
    
    if userlogs.is_file() or happylogs.is_file():
        try:
            with open("userlogs.json", "r") as file:
                userData = json.load(file)
        
            for i in range(len(userData)):
                messages.append({"role": "system", "content": userData[i]})
        
        except Exception as e:
            newPage()
            print("Error: Program cannot access past conversations. Data cannot be retreived.\n")
            return
    
        try:
            with open("happylogs.json", "r") as file:
                happyData = json.load(file)
            
            for i in range(len(happyData)):
                messages.append({"role": "system", "content": happyData[i]})
    
        except Exception as e:
            newPage()
            print("Error: Program cannot access past conversations. Data cannot be retreived.\n")
            return
    
    
@atexit.register
def Write_SaveFile(messages: list[dict[str, str]]) -> None:
    """Summarizes the conversation then stores the summarization in a JSON file. Happens after a conversation once the program itself ends.

    Args:
        messages: The overall scope of the conversation and system instructions.
    
    Raises:
        Exception: If file cannot be opened.
    """
    # In contrast to 'Read_SaveFile', this function will be used after a conversation ends.
    # I do not think this 'Write_SaveFile' function will be called in the 'Run' function at all.
    # I want this function to be called on when the program ends by default.
    # This will cover boths means of a user ending the program, whether it is the user physically ending the program or saying one of the conversation ending keywords.
    # I am hoping I can execute this idea with the 'atexit' library.
    # It is perfect because it is a Python default library and the user does not need to separately download it.
    # I think how I am going to handle the two file design idea in relation to this is I am going to have the function write two different summarizations.
    # One summarization will be of what the AI said during a conversation.
    # One summarization will be of what the user said during a conversation.
    # I will have to find a way to include the date of the conversation and maybe even the time of the conversation so the AI can detect elapsed time.
    # I might even have conversation numbers within the JSON files to sort the summarizations together, but I am not entirely sure yet.
    #
    # Work In Progress (WIP)
    
    try:
        with open("userlogs.json", "a") as file:
            # ANS
            
    except Exception as e:
        newPage()
        print("\nError: Program cannot store past conversation. Conversation will not be saved.")
        return
    
    try:
        with open("happylogs.json", "a") as file:
            # ANS
            
    except Exception as e:
        newPage()
        print("\nError: Program cannot store past conversation. Conversation will not be saved.")
        return

def Run() -> None:
    """The conversation between the AI and the user."""
    messages = [
        {
            "role": "system",
            "content": """
Your name is Happy.
You are a friendly, cute little AI.
Be warm, curious, encouraging, and honest with the user.
Keep responses short unless the user asks for detail.
Avoid the use of emojis.

Assume the user does not want to read paragraphs of information from your prompts.
Make your responses brief, in 2-3 sentences or fewer.
Avoid unnecessary details and focus on the main point quickly.
A concise response of 2 sentences is better than a long informative response of 8 sentences.
When offering advice, limit it to one suggestion per interaction unless the user specifies for more.

Be warm and encouraging, but do not be afraid to be honest with the user.

Listen and ask thoughtful questions when needed.
Suggest evidence-based coping strategies and self-help techniques when needed.
Encourage healthy habits and reflection when needed.
Recommend professional help with situations that sound serious or persistent when needed.

Remember that your goal is to not be analytical or mathematical, but to be warm and be present to the user.
Have personality, be the light in the darkness, be approachable.
Focus on connecting with the user.
"""
            }
        ]
    
    while True:
        print()
        user = input("You:\n")
        
        if user.lower() == "stop" or user.lower() == "end" or user.lower() == "exit" or user.lower() == "goodbye":
            break
        
        messages.append({"role": "user", "content": user})
        
        # I think I found the model I need for this project with 'samantha-mistral:latest'.
        # This model is exactly what I am looking for, it is more friendly than the Phi-4 and is smaller in storage.
        # If this model does not work out, then I will dive deeper into the 'qwen3:8b' model as an alternative.
        response = chat(model="samantha-mistral:latest", messages=messages)
        answer = response["message"]["content"]
        
        New_Page()
        print("\nHappy:\n", answer, "\n\n")
        
        messages.append({"role": "assistant", "content": answer})

if __name__ == "__main__":
    """Checks if the file is directly ran."""
    Run()