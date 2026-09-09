import os
from dotenv import load_dotenv
from openai import OpenAI

#setting the env variables for the API key
load_dotenv(override=True)

gemini_api_key = os.getenv('GOOGLE_API_KEY')
gemini_url = "https://generativelanguage.googleapis.com/v1beta/openai/"
MODEL = 'gemini-3.6-flash'
gemini = OpenAI(api_key=gemini_api_key, base_url=gemini_url)


# anthropic_api_key = os.getenv('ANTHROPIC_API_KEY')
# anthropic_url = "https://api.anthropic.com/v1/"
# MODEL = 'claude-sonnet-4-5-20250929'
# anthropic = OpenAI(api_key=anthropic_api_key, base_url=anthropic_url)

