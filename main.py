#!/usr/bin/env python3
"""The joke the reviewer laughs at — make.fun entry.

Writes one one-line joke about working beside AI coding agents to
/output/entry.txt. Deterministic: the same bytes on every run.
No network, no randomness, no input.
"""

import os

JOKE = "My AI agent approves every PR with 'LGTM' \u2014 it never reads the diff, and neither do I."

def main() -> None:
    # The gate allows 1 to 280 Unicode code points, not only whitespace.
    assert 1 <= len(JOKE) <= 280 and JOKE.strip(), "joke outside the gate"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)

if __name__ == "__main__":
    main()
