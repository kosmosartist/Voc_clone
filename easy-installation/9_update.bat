@echo off
setlocal enableextensions enabledelayedexpansion

set "SCRIPT_DIR=%~dp0"
set "ROOT_DIR=%SCRIPT_DIR%.."
set "VENV_DIR=%SCRIPT_DIR%_env"
set "LOG_DIR=%SCRIPT_DIR%logs"
set "LOG_FILE=%LOG_DIR%\update.log"

if not exist "%LOG_DIR%" (
  mkdir "%LOG_DIR%"
)

echo [INFO] Логи обновления: %LOG_FILE%

pushd "%ROOT_DIR%"

echo [INFO] git pull >> "%LOG_FILE%" 2>&1
git pull >> "%LOG_FILE%" 2>&1
if errorlevel 1 goto :error

if not exist "%VENV_DIR%\Scripts\python.exe" (
  echo [ERROR] Виртуальное окружение не найдено. Запусти 0_install.bat. Лог: %LOG_FILE%
  pause
  exit /b 1
)

call "%VENV_DIR%\Scripts\activate.bat"

echo [INFO] Обновление зависимостей >> "%LOG_FILE%" 2>&1
python -m pip install -r requirements.txt >> "%LOG_FILE%" 2>&1
if errorlevel 1 goto :error

popd
echo [INFO] Обновление завершено. Лог: %LOG_FILE%
exit /b 0

:error
popd
echo [ERROR] Обновление завершилось с ошибкой. Лог: %LOG_FILE%
pause
exit /b 1
