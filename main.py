"""Funny single-line excuse a developer gives when code breaks in production.

Writes one excuse (under 200 chars) to /output/entry.txt.
"""

import os

# Final: blame production, offer to roll back reality.
EXCUSE = "It works on my machine, so production must be the one with the bug — I suggest we roll back reality."


def main() -> None:
    text = EXCUSE.strip()
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {text!r} ({len(text)} chars) to {out_dir}/entry.txt")


if __name__ == "__main__":
    main()
