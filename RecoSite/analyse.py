import numpy as np
import matplotlib as math
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib import colors
from matplotlib.ticker import PercentFormatter


# il renvoie le nombre de nouvelles personnes multiplié par l'intervalle de confiance de chaque personne qui chanque x% de la video
# ensuite il renvoie le nbre d'image dans la video
# puis le nbre de secondes pour afficher une image
# en fait, c'est le framerate qui va ici être l'incrémentation des images de la video.

def debitmoyen(Nb, d):
    # cette fonction calcule la moyenne aritmétique du nombre de personnes rentrant au cours du temps
    D = []
    for i in range(len(Nb)):
        D.append(Nb[i] / d)
    return D


def Temps(Nb, d, debut):
    T = [debut + d / 2]
    t = debut + d / 2
    for i in range(len(Nb) - 1):
        t = t + d
        T.append(t)
    return T

def affichage(Nb, d, debut):
    D = debitmoyen(Nb, d)
    T = Temps(Nb, d, debut)
    plt.plot(T, D)
    plt.xlabel('durée')
    plt.ylabel('personnes')
    plt.grid()
    plt.savefig('static/analyse.png')
    return