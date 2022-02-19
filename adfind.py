import os
from platform import system
from time import sleep
import sys

# Get Platform
if system() == "Windows":
    hapus = "cls"
else:
    hapus = "clear"

# Error Import Handling 
try:
    import requests
except ImportError:
    os.system('pip install requests')
    exit('Reload this Tools')


# Collor
brown = "\033[33m"
greenLight = "\033[32m"
cyan = "\033[36m"
red = "\033[31m"
yellow = "\033[33m"
blue = "\033[34m"
white = "\033[37m"
purple = "\033[35m"

# Banner
def banner():
    print('''
    
    
'''+purple+'''         _______
'''+purple+'''       _/       \_   '''+greenLight+'''                 _           _       
'''+purple+'''      / |       | \  '''+greenLight+'''        /\      | |         (_)      
'''+purple+'''     /  |__   __|  \ '''+greenLight+'''       /  \   __| |_ __ ___  _ _ __  
'''+purple+'''    |__/((o| |o))\__|'''+greenLight+'''      / /\ \ / _` | '_ ` _ \| | '_ \ 
'''+purple+'''    |      | |      |'''+greenLight+'''     / ____ \ (_| | | | | | | | | | |
'''+purple+'''    |\     |_|     /|'''+greenLight+'''    /_/____\_\__,_|_| |_| |_|_|_| |_|
'''+purple+'''    | \           / |'''+greenLight+'''    |  ____(_)         | |           
'''+purple+'''     \| /  ___  \ |/ '''+greenLight+'''    | |__   _ _ __   __| | ___ _ __  
'''+purple+'''      \ | / _ \ | /  '''+greenLight+'''    |  __| | | '_ \ / _` |/ _ \ '__| 
'''+purple+'''       \_________/   '''+greenLight+'''    | |    | | | | | (_| |  __/ |    
'''+purple+'''        _|_____|_    '''+greenLight+'''    |_|    |_|_| |_|\__,_|\___|_|    
'''+purple+'''   ____|_________|____
'''+purple+'''  /                   \ '''+yellow+'''              V1.0
'''+yellow+'''  =============================================================
      
'''+red+'''    Author : AdliXSec
    GitHub : https://github.com/AdliXSec
    Team   : Dark Clown Security

    ''')

# Animation
def loading(text):
    for i in text + "\n":
        sys.stdout.write(i)
        sys.stdout.flush()
        sleep(0.1)

# Proses ngentod
def main():
    os.system(hapus)
    banner()
    url = input(cyan+" Masukkan URL Website : "+greenLight)
    loading("\n Starting Admin Finder ...")
    file = open("pgadmin.txt", "r")	
    try:
        for link in file.read().splitlines():
            curl = url + link
            res = requests.get(curl)
            if res.status_code == 200:
                print(white+" ======================")
                print(greenLight+" [+] Admin panel found --> {} ".format(curl))
                print(white+" ======================")
            else:
                print(red+" [-] Not found --> {} ".format(curl))
        
    except KeyboardInterrupt:
        print(red+" Shutdown Request ! ")
    except:
        print(red+" Unknown Error ! ")


if __name__ == "__main__":
    main()