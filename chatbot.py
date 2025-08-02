def chatbot():
    print("Hello! I am a basic chatbot. Type 'bye' to exit.")
    while True:
        user_input = input("You: ").lower().strip()

        if any(greet in user_input for greet in ["hello", "hi", "hey"]):
            print("Bot: Hello! How can I help you today?")
        elif "how are you" in user_input:
            print("Bot: I'm just a program, but thanks for asking!")
        elif any(exit_word in user_input for exit_word in ["bye", "exit", "quit"]):
            print("Bot: Goodbye! Have a nice day.")
            break
        else:
            print("Bot: Sorry, I don't understand that. Can you try something else?")

if __name__ == "__main__":
    chatbot()
