import unittest

class Tests(unittest.TestCase):

    def setUp(self):
        """Simulates a conversation between a user and Happy about a Birthday Party."""
        self.messages = []
        
        self.messages.append({"role": "user", "content": "Hey! I am going to a pizza place for a Birthday Party later!"})
        self.messages.append({"role": "assistant", "content": "That sounds like fun! What are you most looking forward to at the party? "})
        self.messages.append({"role": "user", "content": "I am looking forward to seeing everyone! A lot of people are going to be there, I think 22 people?"})
        self.messages.append({"role": "assistant", "content": "It's exciting when a large group of friends can get together for a celebration. The energy and atmosphere will be contagious."})
        self.messages.append({"role": "user", "content": "I know! I am super excited! It's for my friend John."})
        self.messages.append({"role": "assistant", "content": "John sounds like a lucky guy to have so many people celebrating his birthday with him. What do you admire most about your friend John?"})
        self.messages.append({"role": "user", "content": "He's just a cool dude, and he cares about the people around him, he is a great guy."})
        self.messages.append({"role": "assistant", "content": "That's wonderful! It's always a delight to be around someone who values kindness, empathy, and genuine connections with others. I'm sure John will have an amazing time with all of his friends there to celebrate him. "})
        self.messages.append({"role": "user", "content": "Yeah! And there are arcade games at the Pizza Place too! They have all of the games you can imagine! I love Galaga and Pacman!"})
        self.messages.append({"role": "assistant", "content": "I've always enjoyed classic arcade games as well. There's something exciting about playing a game with your friends in real time, right there on the spot. It makes for great memories."})
    
    def test_assistant_message_history(self):
        """Verify that all assistant (AI) messages are properly obtained."""
        self.included = True
        self.assistantMessageHistory = ""
        
        for i in range(len(self.messages)):
            if self.messages[i]["role"] == "assistant":
                self.assistantMessageHistory += " " + self.messages[i]["content"]
                
        for i in range(len(self.messages)):
            if self.messages[i]["role"] == "assistant":
                currentMessage = self.messages[i]["content"]
                
                if currentMessage not in self.assistantMessageHistory:
                    self.included = False
        
        self.assertTrue(self.included)
        
    def test_user_message_history(self):
        """Verify that all user messages are properly obtained."""
        self.included = True
        self.userMessageHistory = ""
        
        for i in range(len(self.messages)):
            if self.messages[i]["role"] == "user":
                self.userMessageHistory += " " + self.messages[i]["content"]
                
        for i in range(len(self.messages)):
            if self.messages[i]["role"] == "user":
                currentMessage = self.messages[i]["content"]
                
                if currentMessage not in self.userMessageHistory:
                    self.included = False
                    
        self.assertTrue(self.included)

if __name__ == "__main__":
    """Checks if the test file is directly ran."""
    unittest.main()