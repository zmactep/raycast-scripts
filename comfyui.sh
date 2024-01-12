#!/bin/bash

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title ComfyUI
# @raycast.mode compact

# Optional parameters:
# @raycast.icon 🎨
# @raycast.packageName comfyui

# Documentation:
# @raycast.description Run ComfyUI
# @raycast.author zmactep
# @raycast.authorURL https://raycast.com/zmactep

eval "$(conda shell.bash hook)"
conda activate comfyui
cd $HOME/.local/share/ComfyUI
python main.py --force-fp16
