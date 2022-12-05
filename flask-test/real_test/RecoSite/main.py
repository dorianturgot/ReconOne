# Fonction à testetr
import numpy as np
import os
import urllib.request
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from app import app 

# Application web

from flask import Flask, render_template

@app.route('/')
def menu():
    return render_template("index.html")

@app.route('/', methods=['POST'])
def upload_video():
	if 'file' not in request.files:
		flash('No file part')
		return redirect(request.url)
	file = request.files['file']
	if file.filename == '':
		flash('No video selected for uploading')
		return redirect(request.url)
	else:
		file_name, file_extension = os.path.splitext(file.filename)
		filename = secure_filename("video"+file_extension)
		file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		flash('Video successfully uploaded and displayed below')
		return render_template('index.html', filename=filename)

if __name__ == '__main__':
    DEBUG = True
    HOST = '0.0.0.0'
    app.run(debug=DEBUG, host=HOST)
