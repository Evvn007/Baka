import os
from flask import Flask
from threading import Thread

app = Flask(__name__)

@app.route("/")
def home():
    return "BAKA Bot is running!"

def run():
    port = int(os.environ.get("PORT", 8099))
    app.run(host="0.0.0.0", port=port)

def keep_alive():
    Thread(target=run, daemon=True).start()
