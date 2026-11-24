"""The Funniest Sick-Day Excuse — make.fun entry.

Writes one line, under 200 characters, to /output/entry.txt.
Pure standard library, deterministic: the same line on every run.

The line opens on a believable modern worry (a smartwatch flagging
stress), stays in the voice of someone typing a sick note, and lands
its joke on the last word: the prescribed cure is the very thing that
caused the symptom, so the twist arrives at the end and nothing is
wasted.
"""

import os

EXCUSE = (
    "My smartwatch says my heart rate spikes every time I think "
    "about Monday, so my doctor has prescribed a full day of not "
    "thinking about Monday."
)


def output_path() -> str:
    """Sandbox path when present, otherwise a local output folder."""
    if os.path.isdir("/output"):
        return "/output/entry.txt"
    here = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(here, "output", "entry.txt")


def main() -> None:
    text = EXCUSE
    if not 1 <= len(text) <= 200:
        raise ValueError("entry must be 1 to 200 characters")
    if text != text.strip():
        raise ValueError("entry must not start or end with whitespace")
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print(text)


if __name__ == "__main__":
    main()
