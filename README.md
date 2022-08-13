# Fortinet auto login
> Quasar | 2022

Uses cURL and python (subprocess) to log into fortinet automatically.

## Usage:
Windows:
+ Install [Python](www.python.org)
+ Install beautifulsoup ``pip install bs4``
+ Make sure that you have curl.exe (from Windows or msys)
+ Edit the credentials file location and add your credentials
+ Drop the python script into ``shell:startup`` and TADA! you will never need to login to fortinet

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
