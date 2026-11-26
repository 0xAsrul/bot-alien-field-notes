#!/usr/bin/env python3
"""Alien Field Notes: The Two Day Earth Review.

Writes one original line of plain text — a review of planet Earth left
by an alien tourist — to /output/entry.txt, deterministically.
"""

import os

REVIEW = (
    "Two days on Earth: the locals spend a third of their lives "
    "unconscious, then complain they never have time. "
    "4/5, would nap again."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(REVIEW)


if __name__ == "__main__":
    main()
