import subprocess
import time
import requests,sys
from rich import print
from rich.panel import Panel
from rich.align import Align

subprocess.call('clear',shell=False)
#subprocess.call('cat logo',shell=True)
def Main():
    try:
        inp = input("domain : ")
        url = f"https://api.hackertarget.com/hostsearch/?q={inp}"
        req = requests.get(url)
        print(Panel(req.text,border_style='blue bold',highlight=True,title=' INFO '))
    except:
        sys.exit(1)
Main()


