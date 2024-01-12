#!/usr/bin/env conda run -n llm python

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Summarize tab
# @raycast.mode fullOutput

# Optional parameters:
# @raycast.icon 📄
# @raycast.packageName llm-summarize-tab

# Documentation:
# @raycast.description Summarizes an article at current Arc tab 
# @raycast.author zmactep
# @raycast.authorURL https://raycast.com/zmactep

import sys
sys.dont_write_bytecode = True

from llm_suite import download_text, run_llm, \
                      make_summarize_prompt, get_arc_url


if __name__ == "__main__":
    url = get_arc_url() 
    article = download_text(url)
    prompt = make_summarize_prompt(article)
    output = run_llm(prompt)
    print(output)
