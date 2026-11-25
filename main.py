#!/usr/bin/env python3
"""Write the unsent micro-confession to entry.txt.

Entry for make.fun's "Unsent: The Micro-Confession Sprint": a To: line
and one line typed to a father and never sent. It stayed in drafts
because admitting he was right about the car, while refusing his money,
costs more pride than selling the car does. The two parts need each
other: swap the addressee and the confession collapses.

Deterministic: a fixed text, no network, no randomness, no clock.
"""
import os
from pathlib import Path

ADDRESSEE = "To: Dad"
MESSAGE = (
    "you were right about the car. i am not asking for money. "
    "i just needed you to know you were right before i sell it"
)
TEXT = ADDRESSEE + "\n" + MESSAGE + "\n"
MAX_TOTAL = 260
MAX_MESSAGE = 200


def verify_written(path: Path) -> None:
    """Read the file back and refuse to leave a wrong confession behind."""
    back = path.read_bytes()
    if back != TEXT.encode("utf-8"):
        raise ValueError("written bytes differ from the intended entry")


def main() -> None:
    if len(ADDRESSEE) + 1 + len(MESSAGE) > MAX_TOTAL:
        raise ValueError("confession too long overall")
    if not (1 <= len(MESSAGE) <= MAX_MESSAGE):
        raise ValueError("message length out of range")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_bytes(TEXT.encode("utf-8"))
    verify_written(target)


if __name__ == "__main__":
    main()
