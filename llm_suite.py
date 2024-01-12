#!/usr/bin/env conda run -n llm python

import os
import sys
import subprocess
import requests
import trafilatura
from llama_cpp import Llama

USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
HEADERS = {'User-Agent': USER_AGENT}

MODEL_DIR = "/Users/pavel/.local/share/llm/models"
MODEL = "solar-10.7b-instruct-v1.0.Q5_K_M.gguf"
PROMPT_TEMPLATE = """### User:
{instruction}

{input}

### Assistant:
"""


def get_arc_url():
    script = "tell application \"Arc\" to tell first window to tell active tab to get URL"
    result = subprocess.run(['osascript', '-e', script], capture_output=True)
    return result.stdout.decode('utf-8').strip()


def make_prompt(instruction, article):
    return PROMPT_TEMPLATE.format(instruction=instruction,
                                  input=article)


def make_summarize_prompt(article):
    return make_prompt("Summarize the following article to a few sentences that keep the key ideas of the text.", article)


def make_ask_prompt(question, article):
    return make_prompt(f"Read the following article and answer the question: {question}", article)


def download_text(url):
    response = requests.get(url, headers=HEADERS)
    if response.status_code != 200:
        print(f"Page response error: {response.status_code}")
        sys.exit(1)
    downloaded = response.text
    if not downloaded:
        print("Page does not contain any article")
        sys.exit(1)
    return trafilatura.extract(downloaded)


def run_llm(prompt):
    llm = Llama(model_path=os.path.join(MODEL_DIR, MODEL),
                n_ctx=4096, n_threads=8, n_gpu_layers=49,
                verbose=False)
    output = llm(prompt, max_tokens=4096)
    return output['choices'][0]['text']
