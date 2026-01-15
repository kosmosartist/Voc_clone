@echo off
setlocal enableextensions enabledelayedexpansion

set "SCRIPT_DIR=%~dp0"
set "ROOT_DIR=%SCRIPT_DIR%.."
set "VENV_DIR=%SCRIPT_DIR%_env"
set "LOG_DIR=%SCRIPT_DIR%logs"
set "LOG_FILE=%LOG_DIR%\install.log"

if not exist "%LOG_DIR%" (
  mkdir "%LOG_DIR%"
)

echo [INFO] Логи установки: %LOG_FILE%

where py >nul 2>&1
if %errorlevel%==0 (
  set "PYTHON_CMD=py -3.10"
) else (
  set "PYTHON_CMD=python"
)

pushd "%ROOT_DIR%"

echo [INFO] Создание venv в %VENV_DIR% >> "%LOG_FILE%" 2>&1
call %PYTHON_CMD% -m venv "%VENV_DIR%" >> "%LOG_FILE%" 2>&1
if errorlevel 1 goto :error

call "%VENV_DIR%\Scripts\activate.bat"
if errorlevel 1 goto :error

echo [INFO] Обновление pip >> "%LOG_FILE%" 2>&1
python -m pip install --upgrade pip >> "%LOG_FILE%" 2>&1
if errorlevel 1 goto :error

echo [INFO] Установка PyTorch (CUDA 12.1) >> "%LOG_FILE%" 2>&1
python -m pip install torch==2.4.1+cu121 torchvision==0.19.1+cu121 torchaudio==2.4.1+cu121 --index-url https://download.pytorch.org/whl/cu121 >> "%LOG_FILE%" 2>&1
if errorlevel 1 goto :error

echo [INFO] Установка зависимостей >> "%LOG_FILE%" 2>&1
python -m pip install -r requirements.txt >> "%LOG_FILE%" 2>&1
if errorlevel 1 goto :error

echo [INFO] Проверка CUDA >> "%LOG_FILE%" 2>&1
python -c "import torch; print('torch', torch.__version__); print('cuda_available', torch.cuda.is_available())" >> "%LOG_FILE%" 2>&1
if errorlevel 1 goto :error

echo [INFO] Загрузка моделей >> "%LOG_FILE%" 2>&1
python scripts\download_models.py --output-dir pretrained >> "%LOG_FILE%" 2>&1
if errorlevel 1 goto :error

popd
echo [INFO] Установка завершена. Лог: %LOG_FILE%
exit /b 0

:error
popd
echo [ERROR] Установка не выполнена. Лог: %LOG_FILE%
pause
exit /b 1
