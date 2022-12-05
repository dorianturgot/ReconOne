import numpy as np
import matplotlib as math
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib import colors
from matplotlib.ticker import PercentFormatter
import dorian_reconone_video as dodo

#il renvoie le nombre de nouvelles personnes multiplié par l'intervalle de confiance de chaque personne qui chanque x% de la video
#ensuite il renvoie le nbre d'image dans la video
#puis le nbre de secondes pour afficher une image
#en fait, c'est le framerate qui va ici être l'incrémentation des images de la video.

def debitmoyen(Nb, d):
    D=[]
    for i in range(len(Nb)):
        D.append(Nb[i]/d)
    return D



def Temps(Nb, d, debut):
    T = [debut + d/2]
    t = debut + d/2
    for i in range(len(Nb)-1):
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
    plt.show()
    return

def affichageH(Nb, d, debut):
    fig = plt.figure()
    ax = fig.add_subplot()
    D = debitmoyen(Nb, d)
    T = Temps(Nb, d, debut)
    R = []
    t = d
    xy=(debut + d/2, 0)
    w = d
    h = D[0]
    for i in range(len(T)):
        rect = Rectangle(xy, w, h, color="gray")
        R.append(rect)
        xy = xy + (t, 0)
        h = D[i]
        t = t + d
        ax.add_patch(rect)
        plt.axis('equal')
    plt.plot(T, R)
    plt.xlabel('durée')
    plt.ylabel('personnes')
    plt.grid()
    plt.show()
    return

nb_perso=dodo.countPeople(400)[0]
framerate=dodo.countPeople(400)[3]

print("BBBBBBBBBBBBBBBBIIIIIIIIIIIIIIIIITTTTTTTTTTTTTTTTEEEEEEEEEEEEEEE")
print(affichage(nb_perso,framerate,0))
print("BBBBBBBBBBBBBBBBIIIIIIIIIIIIIIIIITTTTTTTTTTTTTTTTEEEEEEEEEEEEEEE")

N_points = 100000
n_bins = 20
# Create a random number generator with a fixed seed for reproducibility
rng = np.random.default_rng(19680801)
# Generate two normal distributions
dist1 = rng.standard_normal(N_points)
dist2 = 0.4 * rng.standard_normal(N_points) + 5

# We can set the number of bins with the *bins* keyword argument.
axs[0].hist(dist1, bins=n_bins)
axs[1].hist(dist2, bins=n_bins)
fig, axs = plt.subplots(1, 2, tight_layout=True)

# N is the count in each bin, bins is the lower-limit of the bin
N, bins, patches = axs[0].hist(dist1, bins=n_bins)

# We'll color code by height, but you could use any scalar
fracs = N / N.max()

# we need to normalize the data to 0..1 for the full range of the colormap
norm = colors.Normalize(fracs.min(), fracs.max())

# Now, we'll loop through our objects and set the color of each accordingly
for thisfrac, thispatch in zip(fracs, patches):
    color = plt.cm.viridis(norm(thisfrac))
    thispatch.set_facecolor(color)

# We can also normalize our inputs by the total number of counts
axs[1].hist(dist1, bins=n_bins, density=True)

# Now we format the y-axis to display percentage
axs[1].yaxis.set_major_formatter(PercentFormatter(xmax=1))

fig = plt.figure()

plt.show()

