from flask import Flask, session
from front.helper import CustomJSONEncoder

app = Flask(__name__)

app.secret_key = 'SOSECRET!!!'

app.json_encoder = CustomJSONEncoder

import front.front