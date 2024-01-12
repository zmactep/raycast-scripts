#!/usr/bin/env conda run -n llm python

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Summarize
# @raycast.mode fullOutput

# Optional parameters:
# @raycast.icon 📜
# @raycast.argument1 { "type": "text", "placeholder": "URL" }
# @raycast.packageName llm-summarize

# Documentation:
# @raycast.description Summarizes an article at given URL
# @raycast.author zmactep
# @raycast.authorURL https://raycast.com/zmactep

import sys
sys.dont_write_bytecode = True

from llm_suite import download_text, run_llm, \
                      make_summarize_prompt


if __name__ == "__main__":
    url = sys.argv[1]
    article = download_text(url)
    prompt = make_summarize_prompt(article)
    output = run_llm(prompt)
    print(output)
