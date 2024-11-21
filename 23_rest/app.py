import urllib.request
import json
from flask import Flask, render_template

file = open('key_nasa.txt', 'r')
key = file.read()
file.close()

app = Flask(__name__)

@app.route('/')
def index():
    url = 'https://api.nasa.gov/planetary/apod?api_key=' + key
    uResp = urllib.request.urlopen(url)
    page_content = json.loads(uResp.read())
    return render_template('main.html', explanation = page_content['explanation'], image = page_content['hdurl'])

if __name__ == "__main__":
    app.debug = True 
    app.run()