import random

def chatbot_response(user_input):
    user_input = user_input.lower().strip()
    
    if not user_input:
        return "You didn't say anything! Try typing something."
    if any(word in user_input for word in ["hello", "hi", "hey"]):
        return random.choice([
            "Hello! How are you today?",
            "Hi there! What's up?",
            "Hey! Nice to chat with you."
        ])
    elif "how are you" in user_input:
        return random.choice([
            "I'm good, thanks for asking! How about you?",
            "Feeling great! What about you?",
            "I'm doing well! Hope you are too."
        ])
    elif "your name" in user_input or "who are you" in user_input:
        return "I'm AI CHATBOT, your friendly mini chatbot."
    elif any(word in user_input for word in ["bye", "exit", "see you"]):
        return "Goodbye! Have an amazing day!"
    elif any(word in user_input for word in ["dr shamsuddeen", "shamsuddeen"]):
        return (
            "Yes, I know Dr. Shamsuddeen Muhammad. "
            "He's a Google DeepMind and academic research fellow at "
            "Imperial College London, and also the founder of "
            "Arewa Data Science Academy."
        )
    elif "favorite food" in user_input or "what is your favorite food" in user_input:
        return "I love rice and beans! How about you?"
    elif "how old are you" in user_input or "age" in user_input:
        return "I was just created, so I'm very young!"
    elif "joke" in user_input or "tell me a joke" in user_input:
        return random.choice([
            "Why did the computer go to the doctor? Because it caught a virus!",
            "Why was the computer cold? It left its Windows open!",
            "Why did the AI break up with the algorithm? It needed more space!"
        ])
    elif "i am happy" in user_input:
        return "That's awesome! I'm happy to chat with you too."
    elif "i am sad" in user_input:
        return "I'm sorry to hear that. Do you want to talk about it?"
    elif "hobby" in user_input:
        return "I enjoy chatting and learning new things. What about you?"
    elif "game" in user_input:
        return "I like virtual games. What's your favorite game?"
    elif "movie" in user_input:
        return "I enjoy sci-fi movies. Do you have a favorite movie?"
    elif "school" in user_input:
        return "School is important! What's your favorite subject?"
    elif "study" in user_input:
        return "Consistency beats motivation. Try studying a little every day."
    elif "motivation" in user_input:
        return "Believe in yourself! Every expert was once a beginner."
    elif "python" in user_input or "what is python" in user_input:
        return "Python is amazing! You can make chatbots like me with it."
    elif any(word in user_input for word in ["computer science", "cs"]):
        return "Computer Science is about solving problems with logic and creativity."
    elif "ai" in user_input or "artificial intelligence" in user_input:
        return random.choice([
            "AI is fascinating! Do you want to learn how it works?",
            "AI can solve tricky problems. Do you enjoy puzzles?",
            "Artificial Intelligence is shaping the future. What would you like AI to do?"
        ])
    elif "weather" in user_input:
        return "I can't check the weather yet, but I hope it's sunny for you!"
    elif any(word in user_input for word in ["thanks", "thank you"]):
        return "You're welcome!"
    
    else:
        return "Sorry, I don't understand that. Try saying 'hello', 'tell me a joke', or 'how are you'."
    
print("AI CHATBOT: Hi! I'm AI CHATBOT. How can I assist you today? (Type 'bye' to exit)")

while True:
    user_input = input("You: ")
    response = chatbot_response(user_input)
    print("AI CHATBOT:", response)
    
    if user_input.lower() in ["bye", "exit"]:
        break
