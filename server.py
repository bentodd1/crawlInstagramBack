#!flask/bin/python
from flask import Flask
import crawler

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/links/<tag>', methods=['GET'])
def extract_links(tag):
    print(tag)
    crawler.extract_links(tag)
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)