@echo off
@title Basic_Maths Install

set /p usrpath=You Python Path: 
pause
echo install Basic_Maths
copy Basic_Maths\Basic_Maths.py %usrpath%
copy Basic_Maths\lib_ver_info.py %usrpath%
copy Basic_Maths\library_func.py %usrpath%
pause
exit