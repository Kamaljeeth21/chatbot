# Python Chatbot

A simple chatbot built using OpenAI's API.

## Requirements

- Python 3.7 or higher
- An OpenAI account and API key

## Installation

1. Clone the repository.
2. Navigate to the project directory.
3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project directory and add your OpenAI API key:

   ```
   OPENAI_API_KEY=your-real-api-key
   ```

## Usage

Run the chatbot:

```bash
python chatbot.py
```

Type your messages and interact with the chatbot. Type 'exit' to quit.

## Features

- Uses OpenAI's GPT-3.5-turbo model
- Maintains conversation history for context
- Secure API key storage using environment variables
- Customizable personality through system prompts

## Expanding the Project

You can expand this project by:
- Adding a GUI using Tkinter or PyQt
- Building a voice assistant using speech_recognition and pyttsx3
- Connecting it to Telegram or Discord
- Saving conversations to a file
- Adding custom system prompts for different personalities


