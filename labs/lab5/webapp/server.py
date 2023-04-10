import argparse
import http.server
import os
import socketserver
import ssl

parser = argparse.ArgumentParser(
                    prog="server.py",
                    description="Runs the best website in the whole world!")
parser.add_argument("-c", "--cert", required=False)
parser.add_argument("-i", "--ip", required=True)
parser.add_argument("-p", "--port", required=True)

DIRECTORY="./"

def doHttp(ip, port):
    class Handler(http.server.SimpleHTTPRequestHandler):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, directory=DIRECTORY, **kwargs)

    with socketserver.TCPServer((ip, port), Handler) as httpd:
        print(f"YOURL: http://{ip}:{port}")
        httpd.serve_forever()

def doHttps(ip, port, cert):
    class Handler(http.server.SimpleHTTPRequestHandler):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, directory=DIRECTORY, **kwargs)

    with socketserver.TCPServer((ip, port), Handler) as httpd:
        print(f"CERT: {cert}")
        print(f"URL : https://{ip}:{port}")
        context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        context.load_cert_chain("cert.pem", "cert.pem")
        httpd.socket = context.wrap_socket(httpd.socket, server_side=True)
        httpd.serve_forever()

if __name__ == "__main__":
    args = parser.parse_args()
    if args.cert:
        if not os.path.isfile(args.cert):
            print(f"Error: Cert path does not exist: {args.cert}")
            exit(1)
        doHttps(args.ip, int(args.port), args.cert)
    else:
        doHttp(args.ip, int(args.port))
