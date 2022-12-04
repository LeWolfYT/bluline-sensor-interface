import requests as r
#import tkinter as tk
import xmltodict as xml
import time as t
import getpass as gp

print("BluLog CLI")

uname = input("Email/username: ")
upass = gp.getpass()

d = xml.parse(r.get(f"https://http-receiver.bluconsole.com/bluconsolerest/1.0/resources/devices?uname={uname}&upass={upass}").content)
temps = []
names = []
times = []

try:
    for dev in d["devices"]["tdl"]:
        temps.append(dev["ms"]["m"]["t"])
        names.append(dev["label"])
        times.append(t.strftime("%x %X", t.localtime(int(dev["ms"]["m"]["utc"]))))
    print("Current temps:")
    for ti in range(len(temps)):
        print(f"{names[ti]} (as of {times[ti]}) - {temps[ti]}°C")
except:
    print("Invalid username or password!")