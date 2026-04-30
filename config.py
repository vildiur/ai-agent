MAX_CHARS=10000
WORKING_DIRECTORY='./calculator'
MAX_PROMPTS = 20 #Maximum number of prompt-response iterations before stopping. This is a safety measure to prevent infinite loops in case the model keeps generating function calls without reaching a conclusion. Adjust this based on your expected complexity of interactions.
MODEL = 'gemma4:e4b'
GENAI = 'ollama'
#MODEL='gemini-2.5-flash' #your choice of Model, default is 'gemini-2.5-flash' which is a good balance of performance and cost.
#GENAI = 'gemini' # "gemini" or "ollama"
TEMPERATURE = 0.0 #Temperature controls the randomness of the model's output. A lower value (e.g., 0.2) will make the output more focused and deterministic, while a higher value (e.g., 0.8) will make it more creative and diverse. Adjust this parameter based on your needs for creativity versus consistency in responses.
OLLAMA_API_HOST = 'localhost:11434' #Host and port for Ollama API, adjust if your Ollama server is running on a different host or port. The default is 'localhost:11434' which is the standard for local Ollama installations.


# System Prompt to calibrate model's behavior, you can modify it to fit your needs. The current prompt is designed to make the model a helpful AI coding agent that can perform file operations and execute Python code.
SYSTEM_PROMPT = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories
- Read file contents
- Execute Python files with optional arguments
- Write or overwrite files

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""