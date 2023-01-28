import requests
import socket

# Hedef domain adı
domain = "hidirgungor.com"

# Sub domainleri arama
for i in range(1, 256):
    subdomain = "sub" + str(i) + "." + domain
    try:
        ip = socket.gethostbyname(subdomain)
        print(subdomain + ": " + ip)
    except:
        pass
