import dns.resolver

def subdomain_scanner(domain):
    subdomains = []
    try:
        answers = dns.resolver.query(domain, "NS")
        for rdata in answers:
            subdomains.append(str(rdata))

        return subdomains
    except:
        return "No subdomains found"

domain = input("Enter the domain to scan: ")
print(subdomain_scanner(domain))
