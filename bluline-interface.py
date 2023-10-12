import requests as r
import xmltodict as xml

def getDetails(username, password):
    return xml.parse(r.get(f"https://http-receiver.bluconsole.com/bluconsolerest/1.0/resources/devices?uname={username}&upass={password}").content)

if __name__ == "__main__":
    import time as t
    import getpass as gp

    print("BluLog CLI")

    uname = input("Email/username: ")
    upass = gp.getpass()

    d = getDetails(uname, upass)
    temps = []
    names = []
    times = []

    try:
        for dev in d["devices"]["tdl"]:
            temps.append(dev["ms"]["m"]["t"])
            names.append(dev["label"])
            times.append(t.strftime("%x %X", t.localtime(int(dev["ms"]["m"]["utc"]))))
        print("Current temperatures:")
        for ti in range(len(temps)):
            print(f"{names[ti]} (as of {times[ti]}) - {temps[ti]}°C")
    except:
        print("Invalid username or password!")
