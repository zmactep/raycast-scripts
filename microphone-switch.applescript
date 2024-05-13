#!/usr/bin/osascript

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Microphone switch
# @raycast.mode silent

# Optional parameters:
# @raycast.icon 🎙️ 
# @raycast.packageName mic-switch

# Documentation:
# @raycast.description Switches microphone
# @raycast.author zmactep
# @raycast.authorURL https://raycast.com/zmactep

if input volume of (get volume settings) = 0 then
  set level to 50
  display notification "✅ Microphone ON" with title "Microphone"
else
  set level to 0
  display notification "❌ Microphone OFF" with title "Microphone"
end if

set volume input volume level
