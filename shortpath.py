import dns.resolver
import webbrowser

def open_short_url(short_code, base_domain):
    fqdn = f"{short_code}.{base_domain}"
    answers = dns.resolver.resolve(fqdn, 'TXT')
    for rdata in answers:
        full_url = ''.join(s.decode() for s in rdata.strings).strip('"')
        webbrowser.open(full_url)
        return

open_short_url("github", "sansolini.com")