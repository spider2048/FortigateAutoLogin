# Fortinet auto login
> Quasar | 2022

Uses cURL and python (subprocess) to log into fortinet automatically.

## Usage:
Windows:
+ Install [Python](https://www.python.org)
+ Install beautifulsoup ``pip install bs4``
+ Make sure that you have curl.exe (from Windows or msys)
+ Edit the credentials file location and add your credentials
+ Drop the python script into ``shell:startup`` and TADA! you will never need to login to fortinet

If you don'tdon't want to use a python script, cythonize the script and build it with python headers and libraries like this (Requires cython: ``pip install cython``):
```
> cython auto_login.py -o Main.cpp --cplus -3 --embed
> clang++ Main.cpp -I "%pyclude%" -lpython310 -L "%pylib%" -o Login.exe -lUser32.lib -O3
```
where ``pyclude`` is the python header location and ``pylib`` is the python library location.

If you don't want the command window, add:
```c
#include <Windows.h>
```
in the beginning of ``Main.cpp`` and 
```c
ShowWindow(GetConsoleWindow(), SW_HIDE);
```
just after the ``wmain`` function and compile it.

Linux:
+ Install curl ``apt-get install curl``
+ Install beautifulsoup ``pip install bs4``
+ Edit the credentials file location and add your credentials
+ Add the script as a startup task

## JSON Format:
```json
{
	"username": "my-roll-no",
	"password": "my-password"
}
```
