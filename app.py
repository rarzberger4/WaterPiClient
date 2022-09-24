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
        'title'])
    return text['data']['monitors'][0]['locationStop']['properties'][
        'title']  # getting only the needed data from the json file



if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')
