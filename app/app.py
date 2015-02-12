#!/usr/bin/python
from flask import Flask
import sys

app = Flask(__name__)
app.config['NAME'] = 'def'
@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/name')
def hello_name():
    return 'Name is %s' % app.config['NAME']

if __name__ == '__main__':
    app.config['NAME'] = sys.argv[1]
    app.run(host='0.0.0.0', port=5000)
