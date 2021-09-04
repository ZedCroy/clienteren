from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def main():
    return 'FTG JSUIS EN LIGNE VA FAIRE TES HEURES DE VOC SALE FDP'

def run():
    app.run(host="0.0.0.0", port=8080)

def keep_alive():
    server = Thread(target=run)
    server.start()