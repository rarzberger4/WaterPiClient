import json
import urllib.request

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    url = "https://www.wienerlinien.at/ogd_realtime/monitor?rbl=123"
    response = urllib.request.urlopen(url)
    data = response.read()
    text = json.loads(data)
    return text


if __name__ == '__main__':
    app.run()
