
# Google Gemini "toy" AI agent

## Better with virtual environment

> `uv venv`
> `source .venv/bin/activate`

Check config file and set up which model you want to use
***create a .env file which contains your API key***

> `GEMINI_API_KEY='MY-APY-KEY-0000'`

Execute with:
> `uv run main.py <prompt> [--verbose]`

prompt is just what you want your prompt to be
flag --verbose provides extra details on the outcome, mainly prompts used
