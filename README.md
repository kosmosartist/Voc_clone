# Voc_clone

Этот репозиторий содержит краткий гайд по пайплайну клонирования голоса для пения и минимальную «сборку», которая генерирует артефакт на основе документации.

## Быстрый старт

**Сборка:**
```bash
make build
```

**Сборка в Windows (через .bat):**
```bat
build.bat
```

Результат будет в файле:
```
dist/voice_cloning_pipeline.txt
```

**Очистка:**
```bash
make clean
```

## Easy Installation (Windows)

Готовый набор `.bat` находится в `easy-installation/`.

**3 шага:**
1. `easy-installation/0_install.bat`
2. `easy-installation/1_launch_webui.bat`
3. Далее: `easy-installation/2_preprocess.bat` → `easy-installation/3_train.bat` → `easy-installation/4_infer.bat`

Логи сохраняются в `easy-installation/logs/`.

## Что делает сборка

Скрипт `tools/build.py` проверяет, что файл `VOICE_CLONING_PIPELINE.md` существует и не пустой, а затем копирует его содержимое в `dist/voice_cloning_pipeline.txt` для удобной передачи/архивации.
