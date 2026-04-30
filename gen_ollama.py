from config import *
from ollama import Client, ChatResponse
from call_function_ollama import call_function
from functions.function_dec import available_functions

client = Client(host=OLLAMA_API_HOST)


def prompt_ollama(user_prompt, verbose=False):
    

    messages = [{'role' : 'user', 'content' : user_prompt},{'role' : 'system', 'content' : SYSTEM_PROMPT},]
    prompt_tokens = 0
    response_tokens = 0
    
    for _ in range(MAX_PROMPTS):
        response = client.chat(
            model=MODEL, 
            messages=messages,
            options={'temperature': TEMPERATURE},
            tools=available_functions,
            think=True,
            ),
        for candidate in response: 
            messages.append(candidate.message)            
        if response[0].message.tool_calls:
            function_responses =[]
            for output in response[0].message.tool_calls:
                execute = call_function(output, verbose)
                function_responses.append(execute)
            messages.append(function_responses[0])

        prompt_tokens += response[0].prompt_eval_count
        response_tokens += response[0].eval_count
        if not response[0].message.tool_calls:
            break
    

    return candidate['message']['content'],candidate['prompt_eval_count'],candidate['eval_count']


