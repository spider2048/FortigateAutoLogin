# Fortinet auto login
> Quasar | 2022

Uses cURL and python (subprocess) to log into fortinet automatically.

## Usage:
Windows:
+ Install [Python](https://www.python.org)
+ Install beautifulsoup and pymsgbox ``pip install bs4 pymsgbox``
+ Make sure that you have curl.exe (from Windows or msys)
+ Edit the credentials file location and add your credentials
+ Drop the python script (auto_login.py) into ``shell:startup`` and TADA! you will never need to login to fortinet

If you don't want to use a python script, cythonize the script and build it with python headers and libraries like this (Requires cython: ``pip install cython``):
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

------------------------------------------------------------------
Optional: (Windows)
+ Set ``Pyclude`` to the ``PYTHONPATH/Includes`` folder
+ Set ``Pylib`` to the ``PYTHONPATH/libs`` folder
+ Use the build script!

Linux:
+ Install curl ``apt-get install curl``
+ Install beautifulsoup and pymsgbox (tk as well) ``pip install bs4 pymsgbox``
+ Edit the credentials file location and add your credentials
+ Add the script as a startup task

## JSON Format:
```json
{
	"username": "my-roll-no",
	"password": "my-password"
}
```
