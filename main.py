import requests
import threading
import time
import random
choices = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
url = "https://github.com/"

def sniper1():
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
            print("Invalid Username, " + code)
            if save == "y":
                file1 = open("invalid_usernames.txt", "a")
                file1.write(code + "\n")
                file1.close()
        if "404" in r:
            print("Valid Username/Banned, " + code)
            if save == "y":
                file2 = open("valid_or_banned_usernames.txt", "a")
                file2.write(code + "\n")
                file2.close()
        if "200" not in r and "404" not in r:
            print("Rate Limitede, Stopping For 1 Second")
            time.sleep(1)
        time.sleep(float(delay))




def sniper2():
    while True:
        r1 = random.choice(choices)
        r2 = random.choice(choices)
        r3 = random.choice(choices)
        r4 = random.choice(choices)
        code = r1 + r2 + r3 + r4
        r = requests.get(f"{url}{code}")
        r = str(r)
        if "200" in r:
            print("invalid Username, " + code)
            if save == "y":
                file1 = open("invalid_usernames.txt", "a")
                file1.write(code + "\n")
                file1.close()
        if "404" in r:
            print("Valid Username/Banned, " + code)
            if save == "y":
                file2 = open("valid_or_banned_usernames.txt", "a")
                file2.write(code + "\n")
                file2.close()
        if "200" not in r and "404" not in r:
            print("Rate Limitede, Stopping For 1 Second")
            time.sleep(1)
        time.sleep(float(delay))




def sniper3():
    while True:
        r1 = random.choice(choices)
        r2 = random.choice(choices)
        r3 = random.choice(choices)
        code = r1 + r2 + r3
        r = requests.get(f"{url}{code}")
        r = str(r)
        if "200" in r:
            print("Invalid Username, " + code)
            if save == "y":
                file1 = open("invalid_usernames.txt", "a")
                file1.write(code + "\n")
                file1.close()
        if "404" in r:
            print("Valid Username/Banned, " + code)
            if save == "y":
                file2 = open("valid_or_banned_usernames.txt", "a")
                file2.write(code + "\n")
                file2.close()
        if "200" not in r and "404" not in r:
            print("Rate Limitede, Stopping For 1 Second")
            time.sleep(1)
        time.sleep(float(delay))




while True:
    letter = input("""Pick One
1. 5 Letter
2. 4 Letter
3. 3 Letter
> """)
    if letter == "1" or letter == "2" or letter == "3":
    	break
    else:
        print("Enter A Valid Choice")



if letter == "3":
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
        t1 = threading.Thread(target=sniper3)
        t1.start()



if letter == "2":
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
        t1 = threading.Thread(target=sniper2)
        t1.start()



if letter == "1":
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
        t1 = threading.Thread(target=sniper1)
        t1.start()
