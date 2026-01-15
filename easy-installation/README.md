# Easy Installation (Windows)

## Быстрый запуск (3 шага)
1. `0_install.bat` — создаёт venv, ставит зависимости, проверяет CUDA и скачивает модели.
2. `1_launch_webui.bat` — запускает WebUI/Gradio.
3. Дальше используйте `2_preprocess.bat` → `3_train.bat` → `4_infer.bat` по необходимости.

Все логи сохраняются в `easy-installation/logs/`.

По умолчанию рассчитано на Windows + Python 3.10 и CUDA (RTX 4080 Laptop / cu121).
