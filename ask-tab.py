#!/usr/bin/env conda run -n llm python

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Ask tab
# @raycast.mode fullOutput

# Optional parameters:
# @raycast.icon ❓
# @raycast.argument1 { "type": "text", "placeholder": "Question" }
# @raycast.packageName llm-ask-tab

# Documentation:
# @raycast.description Asks a question to a given tab
# @raycast.author zmactep
# @raycast.authorURL https://raycast.com/zmactep

import sys
sys.dont_write_bytecode = True

from llm_suite import download_text, run_llm_subp, \
                      make_ask_prompt, get_arc_url, \
                      detect_paragraphs, filter_paragraphs, \
                      paragraphs_to_article


def prepare_article(article):
    paragraphs = detect_paragraphs(article)
    paragraphs = filter_paragraphs(paragraphs,
                                   skip_titles=["References", "Funding",
                                                "Rights and permissions",
                                                "Additional information",
                                                "Competing interests"])
    return paragraphs_to_article(paragraphs)


if __name__ == "__main__":
    question = sys.argv[1]
    url = get_arc_url()
    article = download_text(url)
    article = prepare_article(article)
    prompt = make_ask_prompt(question, article)
    output = run_llm_subp(prompt)
    print(output)
