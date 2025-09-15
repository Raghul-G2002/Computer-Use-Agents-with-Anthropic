import os
from dotenv import load_dotenv, find_dotenv

def load_env():
    """Load environment variables from a .env file."""
    _ = load_dotenv(find_dotenv())

def get_api_key():
    """Retrieve the Anthropic API key from environment variables."""
    load_env()
    return os.environ.get("ANTHROPIC_API_KEY")

ANTHROPIC_API_KEY = get_api_key()
print("Anthropic API Key Loaded:", ANTHROPIC_API_KEY)