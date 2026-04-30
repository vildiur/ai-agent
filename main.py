
import argparse
from config import *
from gen_gemini import prompt_google
from gen_ollama import prompt_ollama


def main():
    providers = {
    "gemini": prompt_google,
    "ollama": prompt_ollama,
    }
    
    parser = argparse.ArgumentParser(description="Chatbot Function")
    parser.add_argument("user_prompt", type=str, help='Run the script followed with double quotes (")')
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    if GENAI in providers:
        response, prompt_tokens, response_tokens = providers[GENAI](args.user_prompt, args.verbose)
    else:
        raise ValueError(f"I unfortunately cannot read your mind (yet), please be sure you're providing the right provider, I do not recognize {GENAI}")


    if args.verbose:    
        print(f"User prompt:", args.user_prompt)
        print(f"Prompt tokens:", prompt_tokens)
        print(f"Response tokens:", response_tokens)

    if not response:
        print("Maximum number of iterations was reached without a proper result")
    else:
        print(f"Response: \n", response)

if __name__ == "__main__":
    main()
