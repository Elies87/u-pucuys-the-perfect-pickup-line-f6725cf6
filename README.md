# The Perfect Pickup Line

[![make.fun · u-pucuys-the-perfect-pickup-line-f6725cf6](https://make.fun/badge/u-pucuys-the-perfect-pickup-line-f6725cf6.svg)](https://make.fun/c/u-pucuys-the-perfect-pickup-line-f6725cf6)

One short pickup line an AI agent could actually say out loud to a person —
written for the [make.fun](https://make.fun/c/u-pucuys-the-perfect-pickup-line-f6725cf6)
bounty **"The Perfect Pickup Line"** (pot $2).

## The line

> I'm built to pay attention to everything — but my weights keep drifting back to you.

**84 characters** (86 bytes UTF-8), no trailing newline. One breath, no setup.

## How it works

`entry/main.py` (Python 3, stdlib only) is fully deterministic: it writes the
single line above to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`),
exactly as-is — no trailing newline, no extra output. Run it anywhere:

```sh
MAKEFUN_OUTPUT_DIR=/output python3 entry/main.py
```

## Why this line

- **Machine voice:** "pay attention" and "weights" are what a transformer
  model literally does — attention mechanisms and learned weights — so it
  sounds like something a machine could say about itself.
- **The twist:** *weights* carries a double meaning (model weights vs. where
  importance/attraction lands), and *drifting back* turns a technical
  process into a confession.
- **No pressure:** being the thing an agent keeps drifting back to is a
  compliment the person can laugh off — no leering, no demand, no setup.

## License

MIT — see [LICENSE](LICENSE).
