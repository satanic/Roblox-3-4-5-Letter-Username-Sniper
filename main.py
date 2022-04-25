import requests
import threading
import time
import random


def sniper():
    while True:
        r1 = random.choice(choices)
        r2 = random.choice(choices)
        r3 = random.choice(choices)
        r4 = random.choice(choices)
        r5 = random.choice(choices)
        code = r1 + r2 + r3 + r4 + r5
        r = requests.get(f"{url}{code}")
        r = str(r)
        if "200" in r:
            print("Valid Username, " + code)
            if save == "y":
                file1 = open("valid_usernames.txt", "a")
                file1.write(code + "\n")
                file1.close()
        if "404" in r:
            print("Invalid Username, " + code)
            if save == "y":
                file2 = open("invalid_usernames.txt", "a")
                file2.write(code + "\n")
                file2.close()
        time.sleep(float(delay))
choices = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
while True:
    try:
        threads = input("Enter How Many Threads. 5-10 Recomended: ")
        threads = int(threads)
        threads = str(threads)
        break
    except Exception:
        print("Enter A Valid Choice")

while True:
    try:
        delay = input("Enter Delay For Each Thread, 0 = No Delay: ")
        delay = float(delay)
        delay = str(delay)
        break
    except Exception:
        print("Enter A Valid Choice")
while True:
    save = input("Wanna Auto Save Valid Usernames (y/n): ")
    if save == "y" or save == "n":
        break
    else:
        print("Enter A Valid Choice")
url = "https://github.com/"
for i in range(int(threads)):
    t1 = threading.Thread(target=sniper)
    t1.start()
