import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np

NB=[5,4,7,8]
d=125
#débit moyen par session

def debit(NB,d):
    D=[]
    T=[0]
    t=0
    for i in range(len(NB)):
        D.append(NB[i]/d)
        t=t+d
        T.append(t)
    return(D,T)




def affichage(NB,T):
    plt.hist(NB, bins = T)
    plt.xlabel('durée')
    plt.ylabel('personnes')
    
    
    rect = Rectangle(xy, w, h, color="gray")
    ax.add_patch(rect)
    plt.axis('equal')
    plt.grid()
    plt.show()
    return 

fig = plt.figure()
ax = fig.add_subplot()
xy=(-2,3)
w=4
h=2
rect = Rectangle(xy, w, h, color="gray")
ax.add_patch(rect)
plt.axis('equal')
plt.show()