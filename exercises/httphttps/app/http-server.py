import os
from flask import Flask, redirect, render_template, url_for

HOST = "0.0.0.0"
PORT = 12345
USE_TLS = False

if "PORT" in os.environ:
    PORT = int(os.environ["PORT"])

if "USE_TLS" in os.environ:
    USE_TLS = int(os.environ["USE_TLS"]) == 1

app = Flask(__name__,
            static_folder="static",
            template_folder="templates")

@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template("index.html")

@app.route("/favicon.ico")
def favicon():
    return redirect(url_for("static", filename="favicon.ico"))

if __name__ == "__main__":
    if USE_TLS and os.path.isfile("cert.pem") and os.path.isfile("key.pem"):
        app.run(host=HOST, port=PORT, ssl_context=("cert.pem", "key.pem"))
    else:
        app.run(host=HOST, port=PORT)