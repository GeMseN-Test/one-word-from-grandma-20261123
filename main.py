#!/usr/bin/env python3
"""One Word From Grandma — make.fun entry.

Writes exactly one word to /output/entry.txt: the single word a grandma
would text about AI.

The word: "whatchamacallit"
- It is THE grandma word: when she cannot remember what the new machine
  thing is called, she does not say "AI" — she texts "that
  whatchamacallit". Warm, a little baffled, funny in one word, and tied
  to the machine she cannot name. No sentence, no punctuation tricks,
  just the word itself, exactly as she would type it to a grandchild.
- Why not the obvious picks: "robot" is what the machine is, not what
  grandma calls it; "robut" is a cute typo but any grandchild could
  type it; "doohickey" is close, but a doohickey is any small thing,
  while a whatchamacallit is the thing whose name she has given up on
  remembering — which is exactly how she feels about AI.
- 15 characters, inside the 1-30 gate. One word, no trailing newline,
  fully deterministic: every run writes the same bytes.
"""

import os

WORD = "whatchamacallit"
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
