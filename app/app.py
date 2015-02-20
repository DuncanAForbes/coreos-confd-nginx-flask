#!/usr/bin/python
from flask import Flask
import sys
import etcd
import os

app = Flask(__name__)
app.config['NAME'] = 'def'
@app.route('/')
def hello_world():
    return 'Hello World!\n'

@app.route('/name')
def hello_name():
    return 'Name is %s\n' % app.config['NAME']

@app.route('/db')
def db():
    client = etcd.Client(host=os.environ.get('ETCD_IP', 'localhost'), port=int(os.environ.get('ETCD_PORT', 4001)))
    return '%s' % client.read('/', recursive=True)

if __name__ == '__main__':
    app.config['NAME'] = sys.argv[1]
    app.run(host='0.0.0.0', port=5000, debug=True)
