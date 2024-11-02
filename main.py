from responses import get_response

def chat():
    print("Chatbot: Hi! Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break
        # Get the response from the chatbot
        response = get_response(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    chat()
