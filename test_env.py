from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv(dotenv_path='../../../harsh/chatbot/.env')

print("OPENAI_API_KEY:", os.getenv("OPENAI_API_KEY"))
