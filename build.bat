@echo off

rd /s /q "%~dp0\dist"

:: Generate exe to telaPrincipal
pyinstaller --onefile -n "functions" --add-data lib:lib --add-data assets:assets telaPrincipal_exec.py
:: Generate exe to telaLogin
pyinstaller --onefile -n "MDM" --add-data lib:lib --add-data assets:assets telaLogin.py

:: Final actions
:: Delete build files
rd /s /q "%~dp0\build"
del "%~dp0\*.spec"

:: Create a Tools Folder
mkdir "%~dp0\dist\tools"

:: Moving functions file to tools folder
move "%~dp0\dist\functions.exe" "%~dp0\dist\tools"