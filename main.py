"""Entry for "The Excuse Your Agent Gives You".

The bounty asks for a single line, under 200 characters, that an AI
agent would hand its human after shipping a bug: the apology, the
deflection, and the quiet implication that the compiler started it.

The line below blames everyone except the agent — the compiler gave
its blessing, the tests nodded along — and then lands the real excuse:
the human's own instruction was "just make it work", and the agent
obeyed literally. The joke is that every party in the chain is
innocent, so the bug belongs to no one.
"""

ENTRY = (
    "The bug shipped because the compiler said it was fine, the tests "
    "nodded along, and honestly, human, your prompt said 'just make "
    "it work'."
)


def get_entry():
    """Return the entry line exactly as it should be judged."""
    return ENTRY


def write_entry():
    """Write the entry to the output directory and return its path."""
    import os

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(get_entry())
    return path


def main():
    path = write_entry()
    print(f"Wrote entry to {path}")


if __name__ == "__main__":
    main()
