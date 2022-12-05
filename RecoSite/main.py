# Fonction à testetr
import numpy as np
import os
import urllib.request
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from app import app 

from video_traitement import *

# Application web

from flask import Flask, render_template

def test():
    # Algorithme de Gram-Schmidt 
    v1 = np.array([2/3,2/3,1/3])
    v2 = np.array([-2/3,1/3,2/3])
    v3 = np.array([1/3,-2/3,2/3])

    u1 = v1 / np.linalg.norm(v1)
    u2 = v2 - np.dot(u1,v2)*u1
    u2 /= np.linalg.norm(u2)
    u3 = v3 - np.dot(u1,v3)*u1 - np.dot(u2,v3)*u2
    u3 /= np.linalg.norm(u3)

    return np.linalg.norm(u1), np.linalg.norm(u2), np.linalg.norm(u3)

@app.route('/')
def menu():
    return render_template("index.html")

@app.route('/', methods=['POST'])
def upload_file():
	if request.method == 'POST':
		vectors = test()
	f = request.files['file']
	if f.filename == '':
		flash('Pas de vidéo sélectionnée')
		return redirect(request.url)
	f.save(secure_filename("video.mp4"))
	#flash('Video uploadée')
	return render_template("stats.html", vectors=vectors, f=f)

@app.route('/index.html')
def menu2():
    return render_template("index.html")

@app.route('/stats.html')
def traitement(f):
    countPeople(f)
    return render_template("stats.html")

if __name__ == '__main__':
    DEBUG = True
    HOST = '0.0.0.0'
    app.run(debug=DEBUG, host=HOST, port=80)

