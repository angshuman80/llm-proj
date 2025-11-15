from ollama import chat as OllamaChat
from ollama import Client as Ollama
class OllamaClass:
    def __init__(self):
        self.ollama = Ollama()

    def generate_text(self, model_name, prompt):
        response = self.ollama.generate(model=model_name, prompt=prompt)
        return response

    def chat(self, model_name, messages):
        response = self.ollama.chat(model=model_name, messages=messages)
        print(response)
      #  print(response['message']['content'])
        return response['message']['content']