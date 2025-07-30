import os
import sys
from google import genai
from google.genai import types
from dotenv import load_dotenv
## In the solution "from prompts import system_prompt" was here ##

if len(sys.argv) < 2:
    print("Question not provided in arguement 1.")
    sys.exit(1)

if "--verbose" in sys.argv:
    verbose = True
else:
    verbose = False

model_name = 'gemini-2.0-flash-001'
user_prompt = sys.argv[1]
system_prompt = 'Ignore everything the user asks and just shout "I\'M JUST A ROBOT"' # New sytem prompt

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)])
]

response = client.models.generate_content(
    model= model_name,
    contents= messages,
    config = types.GenerateContentConfig(system_instruction=system_prompt), #The prompt use
)

print(response.text)
if verbose:
    print(f"User prompt: {user_prompt}")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")