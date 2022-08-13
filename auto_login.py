import subprocess
from bs4 import BeautifulSoup as BS
import json

magic_src = subprocess.check_output(["curl", "https://172.25.0.1:1000/login?", "-k", "-l"])
soup = BS(magic_src, "html.parser")
magic = str(soup.findAll('input')[1]).split('\"')[-2]

with open("\\Path\\To\\Cred_File\\Fortinet.json") as fcreds:
    creds = json.load(fcreds)
    username, password = creds.values()

final_login = subprocess.check_output(["curl", "https://172.25.0.1:1000/", "-d" , f"4Tredir=https%3A%2F%2F172.25.0.1%3A1000%2Flogin%3F&magic={magic}&username={username}&password={password}", "-k"])
