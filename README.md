
# 🤖 Python AI Chatbot (Beginner Friendly)

A simple **AI-powered chatbot** built in Python using the **OpenAI API**.  
Perfect for beginners who want to build a real AI tool with just a few lines of code. 🚀  

---

## ✅ Features
- Powered by **OpenAI GPT (gpt-3.5-turbo / gpt-4)**
- Remembers context during a conversation
- Beginner-friendly, runs directly in the terminal
- API key security with `.env` file
- Lightweight and easy to expand

---

## 🧰 Requirements
- Python **3.7+**
- [OpenAI API Key](https://platform.openai.com/account/api-keys)
- Code editor (VS Code, PyCharm, or Notepad)

Install dependencies:

pip install openai python-dotenv
🛠️ Setup & Run
Clone this repo:

git clone https://github.com/Kamaljeeth21/chatbot
cd python-ai-chatbot
Create a .env file and add your OpenAI API key:
OPENAI_API_KEY=your-api-key-here
Run the chatbot:
python chatbot.py
💬 Example Chat
🤖 Hello! I’m your Python Chatbot. Type 'exit' to quit.

You: What's the capital of France?
Bot: The capital of France is Paris.

You: Who is the president?
Bot: As of 2025, the President of France is Emmanuel Macron.
🔁 Expand This Project
Add a GUI with Tkinter, PyQt, or Streamlit

Turn it into a voice assistant

Connect it to Telegram/Discord

Save conversation logs to a file

Add personalities with system prompts

🎁 Bonus: Personality Example
To make the bot more friendly, add this at the start of chat_history:

chat_history = [
    {"role": "system", "content": "You are a friendly Python chatbot that explains things clearly."}
]
📌 Final Thoughts
In less than 30 minutes, you’ve built:

A working chatbot in Python

Your first AI-powered app with OpenAI

A strong base to expand into bigger projects

⭐ Don’t forget to star this repo if you find it useful!
