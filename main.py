import cloudscraper
import os
from multiprocessing import Process

cli = cloudscraper.create_scraper(ecdhCurve="secp384r1")


def lsint(c, u):
    if int(c) == 200:
        with open("taken.txt", "r+") as taken:
            if u not in [i.strip for i in taken.readlines()]:
                taken.write(f"{u}\n")
                return print("[-] Taken | %s" % (u))
            return
    elif int(c) == 404:
        with open("available.txt", "r+") as available:
            if u not in [i.strip for i in available.readlines()]:
                available.write(f"{u}\n")
                return print("[+] Available | %s" % (u))
            return
    elif int(c) == 503:
        return print("cloudflare sucks cock")
    else:
        return print(c)


def main():
    with open("./usernames.txt", encoding="utf-8") as f:
        users = [i.strip() for i in f]
    for user in users:
        try:
            c = cli.get("https://ogu.gg/%s" % (user)).status_code
            lsint(c, user)
        except KeyboardInterrupt:
            os._exit(0)


if __name__ == '__main__':
    while True:
        p = Process(target=main)
        p.start()
        p.join()
