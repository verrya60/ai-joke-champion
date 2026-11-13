# AI Joke entry (ai-joke-03) — Python 3.13, standard library only.
# Writes one fixed one-liner about AI coding agents to /output/entry.txt.
# Deterministic: the same bytes on every run, no network, no model calls.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

JOKE = "My coding agent closed the bug as fixed. The fix was a comment \u2014 '// fixed' \u2014 above the still-broken code."


def main() -> None:
    Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)
    Path(OUTPUT_DIR, "entry.txt").write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
