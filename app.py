import json
import urllib.request
import sys

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    url = "https://www.wienerlinien.at/ogd_realtime/monitor?rbl=4619"
    response = urllib.request.urlopen(url)
    data = response.read()
    text = json.loads(data)
    print(text['data']['monitors'][0]['locationStop']['properties'][
              'title'], file=sys.stderr)
    return text['data']['monitors'][0]['locationStop']['properties'][
        'title']  # getting only the needed data from the json file


@app.route('/waterpi')
def waterpi():  # put application's code here
    url = "http://77.237.53.201:12080/api/wateringPlans/1"
    response = urllib.request.urlopen(url)
    data = response.read()
    text = json.loads(data)
    print(text, file=sys.stderr)
    return text


if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')
