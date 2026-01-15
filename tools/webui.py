import argparse
import os
import shutil

import gradio as gr


def convert_audio(input_path: str, output_dir: str) -> str:
    if not input_path:
        raise gr.Error("Не выбран входной аудиофайл.")

    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "converted.wav")
    shutil.copy(input_path, output_path)
    return output_path


def build_interface(output_dir: str) -> gr.Blocks:
    with gr.Blocks() as demo:
        gr.Markdown("# Voc Clone WebUI (Offline)")
        gr.Markdown(
            "Загрузите WAV и нажмите Convert. "
            "Это демо-шаблон: файл просто копируется в outputs/."
        )
        input_audio = gr.Audio(type="filepath", label="Input WAV")
        output_audio = gr.Audio(type="filepath", label="Output WAV")
        convert_button = gr.Button("Convert")
        convert_button.click(
            fn=lambda path: convert_audio(path, output_dir),
            inputs=input_audio,
            outputs=output_audio,
        )
    return demo


def main() -> None:
    parser = argparse.ArgumentParser(description="Launch demo WebUI.")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=7860)
    parser.add_argument("--output-dir", default="outputs")
    args = parser.parse_args()

    demo = build_interface(args.output_dir)
    demo.launch(server_name=args.host, server_port=args.port)


if __name__ == "__main__":
    main()
