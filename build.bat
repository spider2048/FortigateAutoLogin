@echo off

cython --embed auto_login.py -o auto_login.cpp -3 --cplus
@echo Add ShowWindow(...)
pause
g++ -I "%pyclude%" auto_login.cpp -lpython310 -L "%pylib%" -o AutoLogin.exe -O3 -DMS_WIN64 -municode
echo Done!
