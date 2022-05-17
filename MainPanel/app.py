from flask import Flask, render_template
import requests

import json

app = Flask(__name__)

@app.route('/')
def index():
    url = requests.get('http://127.0.0.1:5000')
    Datas = url.json()
    Service_Name = Datas['Service Name']
    Status = Datas['Status']
    length = len(Status)
    return render_template('bootstrap_table.html', title='Service Healtcheck', Service_Name=Service_Name,Status=Status,length=length)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5020, debug=True)
