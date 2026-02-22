# RPG_Dice

Simple command-line dice roller demo written in Python.

## Description

`main.py` is a small interactive program that prompts the user for a dice expression, parses the amount and die type, and prints random roll results. The prompt accepts inputs like `1d6` (one six-sided die) or `3d8` (three eight-sided dice). It demonstrates basic string parsing, type conversion, random number generation, and simple error handling.

## Requirements

- Python 3.7+
- No third-party packages required (uses the standard library `random`).

## Installation

No installation is required. Optionally create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## Usage

From the project root, run:

```bash
python main.py
```

Then enter dice expressions at the prompt. Example inputs:

- `1d6` — roll one 6-sided die
- `2d20` — roll two 20-sided dice
- `7d100` — roll seven 100-sided dice
- `exit` — quit the program

The program prints each roll as it is generated.

## What this program demonstrates

- Parsing a minimal dice-notation string (amount and sides).
- Converting string slices to integers using `int()` (this is the key fragile step in the code).
- Generating uniformly distributed integer rolls with `random.randint`.
- Basic input validation and error handling with `try/except`.

## Limitations and recommendations

- `main.py` assumes a very specific input layout (for example, the first character contains the amount and the die sides begin at index 2). Malformed inputs can raise `ValueError` when converting with `int()` (see the code around the slicing and conversion).
- To improve robustness, validate the input before conversion. Suggested approaches:
  - Use `str.strip()` and `str.isdigit()` on the sliced substring.
  - Use `str.startswith('d')`/`str.lower()` checks for letter prefixes.
  - Prefer a regular expression such as `^\s*(\d+)d(\d+)\s*$` to parse amount and sides reliably.

If you'd like, I can apply a safer replacement (`safe_main.py`) that validates inputs and supports more flexible notation (leading/trailing whitespace, uppercase `D`, multi-digit amounts, etc.).
