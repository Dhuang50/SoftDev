from flask import Flask
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['DATABASE'] = os.path.join(app.instance_path, 'app.sqlite')

# Ensure the instance folder exists
try:
    os.makedirs(app.instance_path)
except OSError:
    pass

import k35.app.routes
