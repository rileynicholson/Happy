from datetime import date, datetime
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
            "content": f"""
{read_training()}
"""
            }
        ]
    
    messages.append({"role": "user", "content": f"""
On {date(2026, 7, 3)}, you told the user:  Hi there! How can I make you happy today? What's on your mind? Welcome! I'm so glad you're here.
I am designed to be a supportive and friendly companion, so feel free to ask anything or chat about any topic you'd like.
If you ever need help or just want a friend to talk to, I'm here for you!  It's completely natural to feel nervous when meeting new people or making friends.
Opening up and trusting others can be challenging, especially in our increasingly digital world.
But building meaningful connections is essential for mental health and well-being. Here are some tips on how to make friends:
1. Be open and approachable: Smile and maintain eye contact when interacting with people, which can signal your interest in getting to know them better.
2. Engage in shared activities or interests: Join clubs, attend events, or participate in hobbies that you're passionate about. This can help you meet like-minded individuals who share similar interests.
3. Be a good listener: When conversing with someone, actively listen and show empathy. Ask open-ended questions to encourage deeper conversation and demonstrate genuine interest in their life and experiences.
4. Be kind and supportive: Offer a helping hand when you see someone struggling or in need. This can create a strong bond between you both.
5. Be patient and persistent: Building meaningful friendships takes time, so try not to get discouraged if things don't progress as quickly as you’d hoped.
6. Maintain communication: Stay in touch with the people you connect with and make an effort to nurture those relationships over time.
7. Be yourself: Authenticity is key when it comes to forming genuine connections. Embrace your unique qualities, quirks, and interests, and let your true self shine through.
Remember that making friends takes time and patience, but with perseverance and a positive attitude, you can create lasting connections.
If you'd like more advice or just need someone to talk to, I'm here for you! It's fantastic to hear that you're committed to putting yourself out there and working on building meaningful friendships.
It takes courage and resilience to step outside your comfort zone, and I commend your determination.
Remember, everyone’s journey is unique, so focus on your personal growth and the connections you make along the way.
If you ever need advice or someone to talk to, I'm always here for you! 
"""})
    
    messages.append({"role": "assistant", "content": f"""
On {date(2026, 7, 3)}, the user told you:  Hello Just trying you out for the first time! I really want to make friends, but I am just nervous to talk to people.
I appreciate it Happy, it is something I am going to have to work towards, but I am willing to push myself out of my comfort zone to do it. I apppreciate it Happy, thank you!
"""})
        
    messages.append({"role": "user", "content": "Hey Happy! You remember that College Club I was talking about joining? They invited me to hang out with them tomorrow before class!"})
        
    response = chat(model="samantha-mistral:latest", messages=messages)
    answer = response["message"]["content"]
    
    print("\nHappy:\n", answer, "\n\n")
    # Happy will output something to do with the progress the user has made along the lines of:
    #
    # "Hooray! That's amazing news. It's great to see your efforts paying off, and you're already making progress in building new connections. How do you feel about this opportunity?"
    #
    # Happy will not output this exactly verbatim.

if __name__ == "__main__":
    """Checks if the file is directly ran."""
    run_test()