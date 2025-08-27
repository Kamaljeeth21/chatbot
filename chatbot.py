from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI client with API key
if api_key:
    client = OpenAI(api_key=api_key)
else:
    print("Error: OPENAI_API_KEY not found in environment variables")
    exit(1)

print("🤖 Hello! I’m your Python Chatbot. Type 'exit' to quit.")

chat_history = [
    {"role": "system", "content": "You are a friendly Python chatbot that explains things clearly."}
]

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("👋 Goodbye!")
        break

    chat_history.append({"role": "user", "content": user_input})

    # Use the new OpenAI API syntax
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=chat_history
    )

    reply = response.choices[0].message.content
    chat_history.append({"role": "assistant", "content": reply})

    print("Bot:", reply)
