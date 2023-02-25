#Créez une fonction calc_distance_3D() qui calcule la distance euclidienne en trois dimensions entre deux atomes.

import math as math
#math.sqrt()

x2=float(input("valeur abscisse p2 :"))
y2=float(input("valeur ordonnee p2 :"))
z2=float(input("valeur cote p2 :"))
x1=float(input("valeur abscisse p1 :"))
y1=float(input("valeur ordonnee p1 :"))
z1=float(input("valeur cote p1 :"))
d = math.sqrt(((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)) 

def dist(p1,p2): 
    return d

print("la distance est :", d)