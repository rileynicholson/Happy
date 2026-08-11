import atexit
from datetime import datetime
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
    -One of the files can be for the user and and can take the conversation when it is finished, summarize it and include key points,
    and store it within its own file.
    -The other file can be for Happy and can take the conversation when it is finished, summarize it and include key points,
    and store it within its own file.
    -I feel like this design would be efficient and at the very least, be a good starting blueprint for Happy.
    
-One of the major hurdles I want to do differently from J.A.R.V.I.S is accessibility.
    -J.A.R.V.I.S requires a lot of installation whether it is external libraries or the Ollama model itself (which is 9.1 GB, HUGE).
    -I want this project to have a smaller AI model that still fits the project well.
    -I also want this project to include as few external libraries as possible, which should not be too challenging for this project.


-Two Json files + Ollama + A good prompt with some prompt engineering could really make something impactful for someone.
"""

def new_page() -> None:
    """Space out the outputs of Happy for formatting."""
    for i in range(100):
        print()
        
def read_saveFile(messages: list[dict[str, str]], happyData: list[str], userData: list[str]) -> None:
    """Takes the conversation summarizations from the JSON save file and appends them into the message history. Happens before a conversation.

    Args:
        messages: The overall scope of the conversation and system instructions.
        
    Raises:
        Exception: If file cannot be opened.
    """
    # Work In Progress (WIP)
    happylogs = Path("happylogs.json")
    userlogs = Path("userlogs.json")

    if userlogs.is_file():
        try:
            with open(userlogs, "r") as file:
                userData.extend(json.load(file))

                for i in range(len(userData)):
                    messages.append({"role": "system", "content": userData[i]})
        
        except Exception as e:
            new_page()
            print("Error: Program cannot access past conversations. Old data cannot be retreived.\n")
            return

    if happylogs.is_file():
        try:
            with open(happylogs, "r") as file:
                happyData.extend(json.load(file))

                for i in range(len(happyData)):
                    messages.append({"role": "system", "content": happyData[i]})
    
        except Exception as e:
            new_page()
            print("Error: Program cannot access past conversations. Old data cannot be retreived.\n")
            return

def find_messages(messages: list[dict[str, str]], role: str) -> str:
    """Finds the amount of messages a certain role has.

    Args:
        messages: The overall scope of the conversation and system instructions.
        role: The type of user whose messages the function looks for.
        
    Returns:
        A string containing all messages from specified role.
    """
    totalMessages = ""
    
    for i in range(len(messages)):
        if messages[i]["role"] == role:
            totalMessages += " " + messages[i]["content"]

    return totalMessages

def write_saveFile(messages: list[dict[str, str]], happyData: list[str], userData: list[str]) -> None:
    """Summarizes the conversation then stores the summarization in a JSON file. Happens after a conversation once the program itself ends.

    Args:
        messages: The overall scope of the conversation and system instructions.
    
    Raises:
        Exception: If file cannot be opened.
    """
    # Work In Progress (WIP)
    happyMessages = f"On {datetime.now()}, you told the user:"
    userMessages = f"On {datetime.now()}, the user told you:"

    userMessageCount = 0
    for i in range(len(messages)):
        if messages[i]["role"] == "user":
            userMessageCount += 1
    
    if userMessageCount > 1:
        happyMessages += find_messages(messages, "assistant")
        userMessages += find_messages(messages, "user")
        
        happyData.append(happyMessages)
        userData.append(userMessages)
        
        try:
            with open("userlogs.json", "w") as file:
                json.dump(userData, file)

            with open("happylogs.json", "w") as file:
                json.dump(happyData, file)
            
        except Exception as e:
            new_page()
            print("\nError: Program cannot store the conversation. Current conversation will not be saved.")
            return

def run() -> None:
    """The conversation between the AI and the user."""
    happyData = []
    userData = []
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
    
    atexit.register(write_saveFile, messages, happyData=happyData, userData=userData)
    read_saveFile(messages, happyData, userData)
    
    while True:
        print()
        user = input("You:\n")
        
        if user.lower() == "stop" or user.lower() == "end" or user.lower() == "exit" or user.lower() == "goodbye":
            break
        
        messages.append({"role": "user", "content": user})
        
        response = chat(model="samantha-mistral:latest", messages=messages)
        answer = response["message"]["content"]
        
        new_page()
        print("Happy:\n", answer, "\n\n")
        
        messages.append({"role": "assistant", "content": answer})

    def getMessages() -> list[dict[str, str]]:
        return messages


if __name__ == "__main__":
    """Checks if the file is directly ran."""
    run()