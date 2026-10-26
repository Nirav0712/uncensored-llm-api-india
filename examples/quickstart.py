# Uncensored LLM API for developers in India — OpenAI-compatible — quickstart
# pip install openai
import os
from openai import OpenAI

client = OpenAI(base_url="https://uncensored-llm.sbs/v1", api_key=os.environ["UNLLM_KEY"])
r = client.chat.completions.create(
    model="uncensored-llm",
    messages=[{"role": "user", "content": "Explain in plain terms how crypto market cap is calculated."}],
)
print(r.choices[0].message.content)
