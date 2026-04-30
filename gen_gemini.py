from google import genai
from google.genai import types
from dotenv import load_dotenv
from config import *
from call_function_gemini import *

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

def prompt_google(user_prompt, verbose=False):
    if not api_key:
        raise RuntimeError ("Need to add API Key")
    
    messages = [types.Content(role="user", parts=[types.Part(text=user_prompt)])]
    prompt_tokens = 0
    response_tokens = 0
    for _ in range(MAX_PROMPTS):
        response = client.models.generate_content(
            model=MODEL, 
            contents=messages,
            config=types.GenerateContentConfig(
                tools=[available_functions], system_instruction=SYSTEM_PROMPT,temperature=TEMPERATURE
            ),
        )
        print (response)
        for candidate in response.candidates:
            messages.append(candidate.content)
        if response.function_calls:
            function_responses =[]
            for output in response.function_calls:
                execute = call_function(output, verbose)
                function_responses.append(execute.parts[0])
            messages.append(types.Content(role="user", parts=function_responses))
        prompt_tokens += response.usage_metadata.prompt_token_count
        response_tokens += response.usage_metadata.candidates_token_count
        if not response.function_calls:
            break
    return response.text, prompt_tokens, response_tokens