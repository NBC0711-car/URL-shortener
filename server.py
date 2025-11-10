from flask import Flask, redirect
import dns.resolver

app = Flask(__name__)
BASE_DOMAIN = "sansolini.com"

@app.route('/<short_code>')
def redirect_short(short_code):
    fqdn = f"{short_code}.{BASE_DOMAIN}"
    try:
        answers = dns.resolver.resolve(fqdn, 'TXT')
        for rdata in answers:
            full_url = ''.join(s.decode() for s in rdata.strings).strip('"')
            return redirect(full_url, code=302)
    except Exception as e:
        return f"Error al resolver {fqdn}: {e}", 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)