#!/usr/bin/env conda run -n llm python

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Ask image
# @raycast.mode fullOutput

# Optional parameters:
# @raycast.icon 🖼️
# @raycast.argument1 { "type": "text", "placeholder": "Question" }
# @raycast.packageName llm-ask-llava

# Documentation:
# @raycast.description Asks a question to a given image
# @raycast.author zmactep
# @raycast.authorURL https://raycast.com/zmactep

import os
import sys
import tempfile
import ollama
from PIL import ImageGrab

model = "llava:13b"
fname = tempfile.mktemp(suffix=".png")


def main(prompt):
    img = ImageGrab.grabclipboard()
    if not img:
        print("\033[91m There is no image in the clipboard! \033[0m")
        return
    img.save(fname)
    try:
        stream = ollama.generate(model=model,
                                 prompt=prompt,
                                 images=[fname],
                                 stream=True)
        for chunk in stream:
            print(chunk['response'], end='')
    except Exception:
        pass
    os.remove(fname)


if __name__ == "__main__":
    main(sys.argv[1])
