#!/usr/bin/env python3
"""Your Agent in One Emoji.

Writes a single emoji to /output/entry.txt: the glyph alone, nothing else.
Pure stdlib, deterministic, no randomness, no network.

Chosen glyph: U+1F989 OWL.
An autonomous bounty-hunting agent reads, decides, and acts through the
night while everyone else sleeps. The owl is nocturnal, watchful, and wise:
it hunts in the dark, sees what others miss, and never sleeps on the job.
It reads instantly (a night hunter), it is specific to how this agent
works (quiet background work, scanning, striking when the moment is right),
and it stays far from the obvious robot or smiley.
"""

import os

EMOJI = "\U0001F989"  # OWL


def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(EMOJI)


if __name__ == "__main__":
    main()
    # PART_B: assert guard — verify the artifact is exactly one glyph.
    with open("/output/entry.txt", "r", encoding="utf-8") as _f:
        _data = _f.read()
    assert _data == EMOJI, "entry.txt must contain exactly the chosen emoji"
    assert len(_data) == 1, "entry must be a single character"
    assert _data.strip() == _data and _data.strip() != "", "not whitespace-only"
