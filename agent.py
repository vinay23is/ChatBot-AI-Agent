import ollama

def run_agent():
    print("🤖 Simple AI Agent (Ollama - Mistral) (type 'exit' to quit)\n")

    conversation = []  # memory for context

    while True:
        user_input = input("You: ")

        if user_input.lower() in ["exit", "quit"]:
            print("Agent: Goodbye!")
            break

        # Add user message to conversation
        conversation.append({"role": "user", "content": user_input})

        # Send prompt to Ollama
        response = ollama.chat(
            model="mistral",
            messages=conversation
        )

        ai_message = response['message']['content']
        print("Agent:", ai_message)

        # Add agent's response to conversation
        conversation.append({"role": "assistant", "content": ai_message})

if __name__ == "__main__":
    run_agent()

