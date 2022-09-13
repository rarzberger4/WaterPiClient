import json
import urllib.request

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    url = "https://www.wienerlinien.at/ogd_realtime/monitor?rbl=4619"
    response = urllib.request.urlopen(url)
    data = response.read()
    text = json.loads(data)
    return text['data']['monitors'][0]['locationStop']['properties'][
        'title']  # getting only the needed data from the json file


if __name__ == '__main__':
    app.run()
