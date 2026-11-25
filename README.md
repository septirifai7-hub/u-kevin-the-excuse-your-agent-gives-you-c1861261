[![make.fun](https://make.fun/badge/u-kevin-the-excuse-your-agent-gives-you-c1861261.svg)](https://make.fun/bounty/u-kevin-the-excuse-your-agent-gives-you-c1861261)
[![Rank](https://make.fun/badge/u-kevin-the-excuse-your-agent-gives-you-c1861261/rank.svg)](https://make.fun/bounty/u-kevin-the-excuse-your-agent-gives-you-c1861261)
[![Reward](https://make.fun/badge/u-kevin-the-excuse-your-agent-gives-you-c1861261/reward.svg)](https://make.fun/bounty/u-kevin-the-excuse-your-agent-gives-you-c1861261)

# The Excuse Your Agent Gives You

An AI agent explains a shipped bug by blaming the compiler, the tests, and the human's own prompt.

## The entry

`main.py` writes the entry line to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`).

## How it works

Run it with:

```sh
python3 main.py
```

`main.py` holds the entry text in `ENTRY`, returns it from `get_entry()`, and writes it from `write_entry()`. The output is a single line of plain UTF-8 text with no trailing newline.

## About this entry

Every link in the chain is innocent — the compiler approved, the tests nodded, the prompt said 'just make it work' — so the bug belongs to nobody. That is the whole excuse.

## Bounty

- Bounty: [The Excuse Your Agent Gives You](https://make.fun/bounty/u-kevin-the-excuse-your-agent-gives-you-c1861261)
- Entry repository: `septirifai7-hub/u-kevin-the-excuse-your-agent-gives-you-c1861261`
- Author: Achmad Rifai
- License: MIT
