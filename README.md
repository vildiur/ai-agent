
# Google Gemini and Ollama toy AI agent

## Do not use this on your projects, there are little guardrails and cause harm

### Better with virtual environment

prepare the environment
> `uv venv`

then activate the environment
> `source .venv/bin/activate`

Check config file and set up which model you want to use
***default config for gemini flash, please review config files to select your desired model or switch to ollama provider***
***modify the .env file which contains your API key, be sure to keep it in gitignore, do not publish your API key!!!!!***

> `GEMINI_API_KEY='MY-APY-KEY-0000'`

Execute with:
> `uv run main.py <prompt> [--verbose]`

prompt is just what you want your prompt to be
flag --verbose provides extra details on the outcome, mainly prompts used

Agent comes with a python calculator to be used as example.
