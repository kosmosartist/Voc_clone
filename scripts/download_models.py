import argparse
import os
import sys
import urllib.request


MODEL_URLS = {
    "hubert_base": "https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/hubert_base.pt",
    "contentvec": "https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/checkpoint_best_legacy_500.pt",
    "rmvpe": "https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/rmvpe.pt",
    "spin": "https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/spin.pt",
}


def download_file(url: str, output_path: str) -> None:
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with urllib.request.urlopen(url) as response, open(output_path, "wb") as handle:
        block_size = 1024 * 1024
        while True:
            chunk = response.read(block_size)
            if not chunk:
                break
            handle.write(chunk)


def main() -> int:
    parser = argparse.ArgumentParser(description="Download pretrained models.")
    parser.add_argument("--output-dir", default="pretrained", help="Target directory for models.")
    args = parser.parse_args()

    output_dir = os.path.abspath(args.output_dir)
    os.makedirs(output_dir, exist_ok=True)

    for name, url in MODEL_URLS.items():
        filename = os.path.join(output_dir, f"{name}.pt")
        if os.path.exists(filename):
            print(f"[SKIP] {name} already exists at {filename}")
            continue
        print(f"[DOWNLOAD] {name} -> {filename}")
        try:
            download_file(url, filename)
        except Exception as exc:
            print(f"[ERROR] Failed to download {name}: {exc}")
            return 1

    print("[DONE] Models downloaded.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
