import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

# Groq client initialize karna
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

print("Aapke account ke liye available models ki list:")
models = client.models.list()
for model in models.data:
    print("-", model.id)