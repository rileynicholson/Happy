from datetime import date, datetime
from ollama import chat

def run_test() -> None:
    """The test function for the AI."""
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
    
    messages.append({"role": "system", "content": f"""
On {date(2026, 8, 3)}, you told the user:  That sounds like fun! What are you most looking forward to at the party?  It's exciting when a large group of friends can get together for a celebration.
 The energy and atmosphere will be contagious. John sounds like a lucky guy to have so many people celebrating his birthday with him.
 What do you admire most about your friend John?
 That's wonderful! It's always a delight to be around someone who values kindness, empathy, and genuine connections with others.
 I'm sure John will have an amazing time with all of his friends there to celebrate him.  I've always enjoyed classic arcade games as well.
 There's something exciting about playing a game with your friends in real time, right there on the spot. It makes for great memories.
"""})
    
    messages.append({"role": "system", "content": f"""
On {date(2026, 8, 3)}, the user told you:  Hey! I am going to a pizza place for a Birthday Party later! I am looking forward to seeing everyone!
 A lot of people are going to be there, I think 22 people? I know! I am super excited! It's for my friend John.
 He's just a cool dude, and he cares about the people around him, he is a great guy.
 Yeah! And there are arcade games at the Pizza Place too! They have all of the games you can imagine!
 I love Galaga and Pacman!
"""})
        
    messages.append({"role": "user", "content": "Hey! Do you remember what I did yesterday?"})
        
    response = chat(model="samantha-mistral:latest", messages=messages)
    answer = response["message"]["content"]
    
    print("\nHappy:\n", answer, "\n\n")
    # Happy will output something to do with the Birthday Party along the lines of:
    #
    # "Hi! Yes, I remember. You told me about your plans to go to a pizza place for a birthday party and how excited you were for the arcade games. It sounds like fun!"
    #
    # Happy will not output this exactly verbatim.

if __name__ == "__main__":
    """Checks if the file is directly ran."""
    run_test()