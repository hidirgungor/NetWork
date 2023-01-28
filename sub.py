import socket
import requests

def subdomain_scanner(domain):
    subdomains = []
    for i in range(1, 256):
        subdomain = "scanme.{}".format(i)
        try:
            ip = socket.gethostbyname(subdomain)
            print("[+] Discovered subdomain: {} ({})".format(subdomain, ip))
            subdomains.append(subdomain)
        except socket.error:
            pass
    return subdomains

if __name__ == "__main__":
    subdomains = subdomain_scanner("sandikli.bel.tr")
    for subdomain in subdomains:
        url = "http://{}".format(subdomain)
        try:
            r = requests.get(url)
            if r.status_code == 200:
                print("[+] Valid subdomain: {}".format(subdomain))
        except requests.exceptions.RequestException:
            pass
