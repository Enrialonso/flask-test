from flask import Flask
import requests

app = Flask(__name__)


@app.route('/')
def index():
    res = requests.get('http://169.254.169.254/latest/meta-data/local-ipv4')
    return res.text


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
