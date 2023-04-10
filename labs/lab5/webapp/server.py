import argparse
import http.server
import os
import socketserver
import ssl
import sys

parser = argparse.ArgumentParser(
                    prog="server.py",
                    description="Runs the best website in the whole world!")
parser.add_argument("-i", "--ip", required=True)
parser.add_argument("-p", "--port", required=True)
parser.add_argument("-S" ,"--security", action='store_true')

DIRECTORY="./"
CERT="cert.pem"
KEY="cert.key"

def doHttp(ip, port):
    class Handler(http.server.SimpleHTTPRequestHandler):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, directory=DIRECTORY, **kwargs)

    with socketserver.TCPServer((ip, port), Handler) as httpd:
        print(f"YOURL: http://{ip}:{port}")
        httpd.serve_forever()

def doHttps(ip, port):
    class Handler(http.server.SimpleHTTPRequestHandler):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, directory=DIRECTORY, **kwargs)

    if not os.path.isfile(CERT):
        sys.exit(f"Error: Can't find self-signed certificate: {CERT}")
    if not os.path.isfile(KEY):
        sys.exit(f"Error: Can't find self-signed private key: {KEY}")

    with socketserver.TCPServer((ip, port), Handler) as httpd:
        print(f"CERT: {CERT}")
        print(f"KEY: {KEY}")
        print(f"URL : https://{ip}:{port}")
        context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        context.load_cert_chain(CERT, KEY)
        httpd.socket = context.wrap_socket(httpd.socket, server_side=True)
        httpd.serve_forever()

if __name__ == "__main__":
    args = parser.parse_args()
    if args.security:
        doHttps(args.ip, int(args.port))
    else:
        doHttp(args.ip, int(args.port))
