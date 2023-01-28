import requests

def subdomain_scan(domain):
    subdomains = []
    try:
        # wordlist dosyasının yolu
        wordlist = "path/to/wordlist.txt"
        with open(wordlist, "r") as f:
            for line in f:
                subdomain = line.strip() + "." + domain
                try:
                    # subdomain adresinin çalışıp çalışmadığını kontrol et
                    response = requests.get("http://" + subdomain, timeout=5)
                    if response.status_code == 200:
                        print("[+] Found:", subdomain)
                        subdomains.append(subdomain)
                except:
                    pass
    except:
        print("[-] Error Occured.")
    return subdomains

print(subdomain_scan("example.com"))
