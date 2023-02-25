
import random

#definition de la fonction gen_distrib qui prend comme argument trois entiers : debut, fin et n
#cette fonction renverra une liste de floats aleatoires entre le debut et la fin
def gen_distrib(debut, fin, n):
   return[random.uniform(debut, fin) for i in range(n)]


# definition d'une fonction calc_stat() qui prend en argument une liste de floats,
# et qui renvoie une liste de trois éléments contenant respectivement le minimum, le maximum et la moyenne de la liste.

def calc_stat(liste_floats):
   
   min_val = min(liste_floats)
   max_val = max(liste_floats)
   moy_val = sum(liste_floats)
   
   return[min_val, max_val, moy_val]

# fonction supplementaire pour arrondir les valaeurs d'une liste

def round_list_elements(floats_list, precision):
    return[round(x,precision) for x in floats_list]
  
les_listes = []
les_stat = []
    
for i in range(20):
    les_listes.append(round_list_elements(gen_distrib(0, 100,100), 2))
    les_stat.append(round_list_elements(calc_stat(les_listes[i]),2))
       
print(les_listes[0])
print(les_stat[0])
       
for i in range(len(les_stat)):
    # print(les_stat[i][0], les_stat[i][1], les_stat[i][2])
    print("\nliste() : min ={} : max ={} : moy = {}".format(i, les_stat[i][0], les_stat[i][2]))
    
    
#Initialiser la liste de moyenne des statistiques
liste_moyenne_stat = [0, 0, 0]
 
 #parcours de la liste contenant les lestes de statistique
for sous_liste in les_stat:
 # moyenne de la sous liste
 moyenne_sous_liste = sum(sous_liste)/ len(sous_liste)
 #Ajout de la moyenne a la liste de moyenne
 liste_moyenne_stat[0] +=sous_liste[0]
 liste_moyenne_stat[1] +=sous_liste[1]
 liste_moyenne_stat[2] +=sous_liste[2]  
 
 #division des totaux afin d'obtenir les moyennes finales
 liste_moyenne_stat[0] /= len(les_stat)
 liste_moyenne_stat[1]  /= len(les_stat)
 liste_moyenne_stat[2]  /= len(les_stat)
 
 print("\nmoyennes des elements de la liste statistique :", round_list_elements(liste_moyenne_stat, 3))
 


    

