import flask
import time
from threading import Thread
import datetime
import os
from os import path
import requests

if os.path.exists("./bin"):
    print("bin exists")
else:
    os.mkdir("./bin")

app = flask.Flask('')

@app.route('/')
def home():
    ip_address = flask.request.remote_addr

    ip = (ip_address)
    key = "" #Put your https://ipstack.com/ API key in the quotes!
    url = ("http://api.ipstack.com/{ip}?access_key={key}")
    querystring = {"format":"json"}

    headers = {
        'ip': f"http://api.ipstack.com/{ip}",
        }

    response = requests.request("GET", url, headers=headers, params=querystring).json()
    country = response["country_name"]
    region = response["region_name"]
    city = response["city"]

    return "" #Put the message you want displayed on the page, inside the quotes.  You can also put <h1>Message</h1> for bigger text, and change colors and whatnot, using HTML!

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=80)
#Change the port or IP as needed, HTTP port is 80, perfect for web access.