"""The funniest toaster error message.

A one-line entry for make.fun's "The Funniest Toaster Error Message"
bounty. The program writes a single error message, exactly as a kitchen
toaster would show it to its owner, to /output/entry.txt.

No arguments, no network, standard library only, deterministic: every
run writes the same bytes.
"""

import os

LINE = "ERROR: Fork detected in slot 2. I cannot help you. No one can help you now."

OUTPUT_DIR = "/output"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "entry.txt")


def main():
    # The gate accepts 1 to 120 characters; refuse to write anything else.
    if not 1 <= len(LINE) <= 120:
        raise ValueError("entry line must be 1 to 120 characters")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as handle:
        handle.write(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
