@echo off
setlocal enableextensions enabledelayedexpansion

set "SCRIPT_DIR=%~dp0"
set "ROOT_DIR=%SCRIPT_DIR%.."
set "VENV_DIR=%SCRIPT_DIR%_env"
set "LOG_DIR=%SCRIPT_DIR%logs"
set "LOG_FILE=%LOG_DIR%\preprocess.log"

if not exist "%LOG_DIR%" (
  mkdir "%LOG_DIR%"
)

echo [INFO] Логи препроцесса: %LOG_FILE%

if not exist "%VENV_DIR%\Scripts\python.exe" (
  echo [ERROR] Виртуальное окружение не найдено. Запусти 0_install.bat. Лог: %LOG_FILE%
  pause
  exit /b 1
)

pushd "%ROOT_DIR%"
call "%VENV_DIR%\Scripts\activate.bat"

echo [INFO] Шаг 1: preprocess >> "%LOG_FILE%" 2>&1
python tools\preprocess.py --stage preprocess >> "%LOG_FILE%" 2>&1
if errorlevel 1 goto :error

echo [INFO] Шаг 2: pitch >> "%LOG_FILE%" 2>&1
python tools\preprocess.py --stage pitch >> "%LOG_FILE%" 2>&1
if errorlevel 1 goto :error

echo [INFO] Шаг 3: embeddings >> "%LOG_FILE%" 2>&1
python tools\preprocess.py --stage embeddings >> "%LOG_FILE%" 2>&1
if errorlevel 1 goto :error

popd
echo [INFO] Препроцесс завершен. Лог: %LOG_FILE%
exit /b 0

:error
popd
echo [ERROR] Препроцесс завершился с ошибкой. Лог: %LOG_FILE%
pause
exit /b 1
