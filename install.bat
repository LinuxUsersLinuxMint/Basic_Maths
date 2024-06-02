@echo off
@title Basic_Maths Install

set /p usrpath=You Python Path: 
pause
echo install Basic_Maths
copy Basic_Maths\Basic_Maths.py %usrpath%
pause
exit