from flask import Flask
import os
from models import init_db

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['DATABASE'] = os.path.join(app.instance_path, 'app.sqlite')

# Ensure the instance folder exists
try:
    os.makedirs(app.instance_path)
except OSError:
    pass

from . import routes

# Initialize the database
init_db()

from . import app

if __name__ == '__main__':
    app.run(debug=True)
