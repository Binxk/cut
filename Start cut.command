#!/bin/bash
# Double-click me to open cut in your browser.
cd "$(dirname "$0")"
PORT=8734
if ! lsof -iTCP:$PORT -sTCP:LISTEN >/dev/null 2>&1; then
  nohup python3 cut_server.py >/dev/null 2>&1 &
  sleep 1
fi
open "http://127.0.0.1:$PORT/index.html"
