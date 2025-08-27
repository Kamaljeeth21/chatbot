# Read the .env file directly
with open('../../../harsh/chatbot/.env', 'r') as f:
    content = f.read()
    print("Content of .env file:")
    print(content)
    
    # Check if it contains the API key
    if 'OPENAI_API_KEY' in content:
        print("\nOPENAI_API_KEY found in .env file")
    else:
        print("\nOPENAI_API_KEY not found in .env file")
