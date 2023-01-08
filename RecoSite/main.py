# Fonction à testetr
import numpy as np
import os
import urllib.request
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from app import app

from video_traitement import *
from analyse import *

# Application web

from flask import Flask, render_template

@app.route('/')
def menu():
    return render_template("index.html")


@app.route('/', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        pass
    f = request.files['file']
    if f.filename == '':
        flash('Pas de vidéo sélectionnée')
        return redirect(request.url)
    f.save(secure_filename("video.mp4"))
    return redirect(url_for("traitement"))


@app.route('/index.html')
def menu2():
    return render_template("index.html")


@app.route('/stats.html')
def traitement():
    people = countPeople("video.mp4")

    nb_perso = people[0]
    nb_perso_debit = nb_perso[1:]
    framerate = people[3]

    affichage(nb_perso_debit, framerate, 0)

    result = open("static/analyse.png", "r")

    return render_template("stats.html", result=result)


if __name__ == '__main__':
    DEBUG = True
    HOST = '0.0.0.0'
    app.run(debug=DEBUG, host=HOST, port=80)
