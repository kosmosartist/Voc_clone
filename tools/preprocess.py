import argparse
import os
from datetime import datetime


def write_marker(output_dir: str, name: str) -> None:
    os.makedirs(output_dir, exist_ok=True)
    marker_path = os.path.join(output_dir, f"{name}.txt")
    with open(marker_path, "w", encoding="utf-8") as handle:
        handle.write(f"{name} completed at {datetime.utcnow().isoformat()}Z\n")


def main() -> None:
    parser = argparse.ArgumentParser(description="Preprocess pipeline placeholder.")
    parser.add_argument("--stage", choices=["preprocess", "pitch", "embeddings"], required=True)
    parser.add_argument("--input-dir", default="data/raw")
    parser.add_argument("--output-dir", default="data/processed")
    args = parser.parse_args()

    os.makedirs(args.input_dir, exist_ok=True)
    if args.stage == "preprocess":
        write_marker(args.output_dir, "preprocess")
    elif args.stage == "pitch":
        write_marker(args.output_dir, "pitch")
    elif args.stage == "embeddings":
        write_marker(args.output_dir, "embeddings")

    print(f"[OK] Stage '{args.stage}' completed. Output: {args.output_dir}")


if __name__ == "__main__":
    main()
