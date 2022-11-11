@echo off 
echo Time script. Just for fun. Don't take it seriously!
set /p month=Please enter the month(eg:202211):
set /p name=Please enter your name:

envs\python.exe src\fitow_worksheet.py %month% %name%
pause
