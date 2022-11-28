# Fonction à testetr
import numpy as np
import os

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

# Application web

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def menu():
    return render_template("index.html")

@app.route("/stats.html")
def statistique_menu():
    vectors = test()
    return render_template("stats.html", vectors=vectors)

@app.route("/index.html")
def menu2():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
