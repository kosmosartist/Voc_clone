#!/usr/bin/env python3
from __future__ import annotations

import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SOURCE = ROOT / "VOICE_CLONING_PIPELINE.md"
DIST_DIR = ROOT / "dist"
OUTPUT = DIST_DIR / "voice_cloning_pipeline.txt"


def main() -> int:
    if not SOURCE.exists():
        print(f"Missing source file: {SOURCE}")
        return 1

    content = SOURCE.read_text(encoding="utf-8").strip()
    if not content:
        print("Source file is empty.")
        return 1

    DIST_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(content + "\n", encoding="utf-8")
    print(f"Build complete: {OUTPUT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
