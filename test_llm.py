import os
from langchain_ollama import ChatOllama

def test_ollama():
    # Use Docker environment variable if available, otherwise fallback to localhost
    ollama_base_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
    
    # Initialize the LLM integration
    llm = ChatOllama(
        model="llama3", # Replace with the exact model you pulled (e.g., 'mistral', 'llama3')
        temperature=0.5,
        base_url=ollama_base_url
    )

    # Define the input messages
    messages = [
        ("system", "You are a concise technical assistant. Think more, talk less."),
        ("human", "Provide a quick 'Hello World' confirmation and state your operational status.")
    ]

    print(f"Connecting to Ollama at {ollama_base_url}...")
    
    try:
        # Invoke the model
        response = llm.invoke(messages)
        print("\n--- Response ---")
        print(response.content)
    except Exception as e:
        print(f"\nConnection Failed. Error: {e}")
        print("Ensure your Ollama container is running and the model is pulled.")

if __name__ == "__main__":
    test_ollama()