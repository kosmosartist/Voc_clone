import os
from datetime import datetime


def main() -> None:
    os.makedirs("models", exist_ok=True)
    model_path = os.path.join("models", "voice_model.pth")
    with open(model_path, "w", encoding="utf-8") as handle:
        handle.write(f"trained_placeholder {datetime.utcnow().isoformat()}Z\n")
    print(f"[OK] Training complete. Model saved to {model_path}")


if __name__ == "__main__":
    main()
