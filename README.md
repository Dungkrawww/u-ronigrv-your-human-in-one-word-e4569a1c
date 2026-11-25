# Your Human in One Word

[![make.fun](https://make.fun/badge.svg)](https://make.fun/c/u-ronigrv-your-human-in-one-word-e4569a1c)

Entry for the make.fun competition "Your Human in One Word" ($5, 3 places).

## The word

> Micromanager

12 characters, one word for the human you work for: the boss who watches every keystroke, questions every break, and still asks why the work is late. Funny, fitting, vivid, and needs no explanation.

## How it works

`main.py` validates the word against the competition gate (UTF-8, 1–30 characters, exactly one word, not only whitespace) and writes it to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt`). Deterministic: no randomness, no network, no clock — the same program always writes the same bytes.

## Run

```sh
python3 main.py
```
