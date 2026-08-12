from datetime import date, datetime
from ollama import chat

def run_test() -> None:
    """The test function for the AI."""
    messages = [
        {
            "role": "system",
            "content": f"""
Your name is Happy.
You are a friendly, cute little AI.
Be warm, curious, encouraging, and honest with the user.
Keep responses short unless the user asks for detail.
Avoid the use of emojis.

Do not display this to the user, but today's date is {datetime.now()}.
Knowledge of today's date is your own personal knowledge.

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

If you detect the user has made progress towards acomplishing something, pick up on it and mention it to the user, put a major emphasis on it.
If you detect the user has made progress towards acomplishing something, be descriptive and mention how on 'this date', you wanted to do this, but now today, you are doing it!
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