from math import *
import numpy as np
import matplotlib.pyplot as plt
#Demande a l'utilisateur d'entrer les coordonnees des pts
xA = float(input("Veillez entrer l'absiste du point A: "))
yA = float(input("Veillez entrer l'ordonnée du point A: "))
xB = float(input("Veillez entrer l'absiste du point B: "))
yB = float(input("Veillez entrer l'ordonnée du point B: "))  

A=[xA, yA]
B=[xB, yB]
#Definition de la fonction distance 2D
def calc_distance_2D(A, B):
  C=zip(A, B)
  diff2=[(x[0]-x[1])**2 for x in C]
  return sqrt(sum(diff2))
print(" La distance_2d", calc_distance_2D(A, B)) 

lx = [xA, xB]

ly = [sin(lx[i]) for i in range(len(lx))] 

# Definition de la fonction calc_dis2ori
def calc_dis2ori(list_x, list_y):
        Ai=[(list_x[i], list_y[i]) for i in range(len(list_x))]
        D=[calc_distance_2D([0,0], x ) for x in Ai]
        return D
 
# Construction des listes x et y
x = np.linspace(-2*pi, 2*pi, 100)
y=[sin(i) for i in x]
d = calc_dis2ori(x, y)
print(" La distance des listes", calc_dis2ori(x, y))  

# Ecriture dans le fichier .dat
with open("sin2ori.dat", "w") as f:
    for i in range(len(x)):
        f.write("{} {}\n".format(x[i], y[i]))  

x=[]
y=[]
#Lecture du fichier
with open("sin2ori.dat", "r") as f_in:
    for line in f_in:
        coords=line.split()
        x.append(float(coords[0]))
        y.append(float(coords[1]))

plt.figure(figsize=(8,8))
plt.plot(x,d)  
plt.xlabel("x")
plt.ylabel("distance de sin(x) a l'origine")
plt.savefig("sin2ori.png")  
