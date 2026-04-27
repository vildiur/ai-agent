import os
import argparse
from dotenv import load_dotenv
from config import *
from google import genai
from google.genai import types
from prompts import system_prompt
from call_function import *

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

def main():
    if not api_key:
        raise RuntimeError ("Need to add API Key")
    
    parser = argparse.ArgumentParser(description="Chatbot Function")
    parser.add_argument("user_prompt", type=str, help='Run the script followed with double quotes (")')
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]
    prompt_tokens = 0
    response_tokens = 0
    for _ in range(MAX_PROMPTS):
        response = client.models.generate_content(
            model=MODEL, 
            contents=messages,
            config=types.GenerateContentConfig(
                tools=[available_functions], system_instruction=system_prompt,temperature=0
            ),
        )
        for candidate in response.candidates:
            messages.append(candidate.content)
        if response.function_calls:
            function_responses =[]
            for output in response.function_calls:
                execute = call_function(output, args.verbose)
                function_responses.append(execute.parts[0])
            messages.append(types.Content(role="user", parts=function_responses))
        prompt_tokens += response.usage_metadata.prompt_token_count
        response_tokens += response.usage_metadata.candidates_token_count
        if not response.function_calls:
            break


    if args.verbose:    
        print(f"User prompt:", args.user_prompt)
        print(f"Prompt tokens:", prompt_tokens)
        print(f"Response tokens:", response_tokens)

    if not response.text:
        print ("Maximum number of iterations was reached without a proper result")
    else:
        print(f"Response: \n",response.text)
    

if __name__ == "__main__":
    main()
