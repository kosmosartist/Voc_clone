import argparse
import os
import shutil


def main() -> None:
    parser = argparse.ArgumentParser(description="Inference placeholder.")
    parser.add_argument("--input", default="data/input.wav")
    parser.add_argument("--output", default="outputs/converted.wav")
    args = parser.parse_args()

    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    if os.path.exists(args.input):
        shutil.copy(args.input, args.output)
        print(f"[OK] Copied {args.input} to {args.output}")
    else:
        with open(args.output, "wb") as handle:
            handle.write(b"")
        print(f"[WARN] Input not found. Created empty output at {args.output}")


if __name__ == "__main__":
    main()
