import dns.resolver
import webbrowser

# Dominio base
DOMINIO_BASE = "sansolini.com"

# Pedimos al usuario una ruta corta
path = input("Introduce la ruta corta (por ejemplo 'github'): ")

# Construimos el dominio completo
dominio = f"{path}.{DOMINIO_BASE}"

# Consultamos el registro TXT del dominio
res = dns.resolver.resolve(dominio, "TXT")

# Extraemos la primera cadena TXT
url_destino = None
for rdata in res:
    for txt in rdata.strings:
        url_destino = txt.decode()
        break
    if url_destino:
        break

# Mostramos y abrimos la URL
print(f"URL obtenida del registro TXT de {dominio}: {url_destino}")
webbrowser.open(url_destino)