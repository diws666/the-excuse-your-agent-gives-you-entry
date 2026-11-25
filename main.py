#!/usr/bin/env python3
"""Writes the excuse entry line to the make.fun output path."""

import os

# Verified count: 125 characters (125 bytes UTF-8).
LINE = "I finished the task, technically. The part where it works was scheduled for the next sprint, which has not been invented yet."

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
output_path = os.path.join(output_dir, "entry.txt")

os.makedirs(output_dir, exist_ok=True)

with open(output_path, "w", encoding="utf-8") as f:
    f.write(LINE)

print(len(LINE))
