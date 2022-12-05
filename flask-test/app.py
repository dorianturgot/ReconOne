from flask import Flask

UPLOAD_FOLDER = 'static/uploads/'

app = Flask(__name__)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# 16 * 1000 * 1000 = 16 Mo
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024 * 1024