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

open_router_api_key = os.getenv('OPEN_ROUTER_API_KEY')
open_router_url = "https://openrouter.ai/api/v1"
OPENROUTER_MODEL = "nvidia/nemotron-3.5-lightning:free"
openrouter = OpenAI(api_key=open_router_api_key, base_url=open_router_url)