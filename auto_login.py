import subprocess
from bs4 import BeautifulSoup as BS
import json
import pymsgbox
from urllib.parse import quote
import time

LOGIN_URL = r"https://172.25.0.1:1000/"
CREDS_PATH = r"Fortinet.json"

def load_creds():
    with open(CREDS_PATH) as fcreds:
        creds = json.load(fcreds)
        return creds.values()

def login(url):
    magic_src = subprocess.check_output(["curl", f"{url}login?", "-k", "-l", "-m", "5"])
    magic = str(BS(magic_src, "lxml").findAll('input')[1]).split('\"')[-2]
    username, password = load_creds()
    return b"Authentication Required" not in subprocess.check_output(["curl", url, "-d" , f"4Tredir={quote(url)}&magic={magic}&username={username}&password={password}", "-k", "-m", "5"])

def turn_off_warp():
    try: subprocess.check_output("warp-cli disconnect")
    except: pass

def main():
    turn_off_warp()
    run = True
    while run:
        try: run = not login(LOGIN_URL)
        except Exception as e:
            if pymsgbox.confirm(e, title="Login FAILED!", buttons=["Again", "Stop"]) == "Stop": run = False
            else: time.sleep(5)

main()
