from ollama_proj import Ollama_class

def main():
    ollama_instance = Ollama_class.OllamaClass()

    # Example usage of generate_text
    model_name = "gpt-oss:120b-cloud"
    prompt = "What is the capital of France?"
    generate_response = ollama_instance.generate_text(model_name, prompt)
    #print the full response objec
    print(f"Generate Response:", generate_response)

    # Example usage of chat
    messages = [
        {"role": "user", "content": "What is the capital of India?"}
        #{"role": "assistant", "content": "I'm good, thank you! How can I assist you today?"}
    ]
    chat_response = ollama_instance.chat(model_name, messages)
    print("Chat Response:", chat_response)

if __name__ == "__main__":
    main()