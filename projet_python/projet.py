
#################################################################################################
######                                                                                     ######
######                    Unité de Recherche en Géosciences (URGéo)                        ######           
######                                Devoir final                                         ######                       
######                        Réalisé par : Stanley GRAVILLE                               ######
######                        Donné par   : Elisée VILLIARD                                ######
######                                                                                     ######
#################################################################################################

#importer les bibliothèques
import pandas as pd
import random
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plts


################################################
####                                        ####
####             PARTIE 1                   ####
####                                        ####
################################################

################################################
####         Réponse 1                     #####
################################################

#Chargement des données de débit
debit = pd.read_csv("data/MIREBALAIS___RIVIERE_ARTIBONITE_30202.txt", sep=";",skiprows=21)
#Conversion des types de données
debit['Q'] = pd.to_numeric(debit['Q'], errors='coerce')
#Suprimer les valeurs de na
debit_sans_na = debit.dropna(subset=["Q"])
debit_sans_na.to_csv("output/debit_sans_na.txt")
#Reformater la colônne dâte
debit_sans_na["Date"] = pd.to_datetime(debit["Date"], format="%Y-%m-%d")

#Grouper les débits par année
#Débit minimal annuel
# debit_min = debit_sans_na.groupby(pd.Grouper(key="Date", freq="Y")).min()
# debit_min["Date"] = debit_min.index
# debit_min.reset_index(drop=True, inplace=True)
# debit_min_ok=debit_min.drop([13], axis=0, inplace=True)

#Afficher le graphe dU débit minimal annuel
# debit_min.plot(x="Date", y="Q")
# plt.title("Variation du débit minimal annuel")
# plt.xlabel("Année")
# plt.ylabel("Débit en m3/s")
# plt.grid(True)
# plt.savefig("debit_min.png", dpi=300)
# plt.show()

###########################################
####         Réponse 2                 ####
###########################################

########### Chaque année ##################
#Débit maximal annuel
# debit_max = debit_sans_na.groupby(pd.Grouper(key="Date", freq="Y")).max()
# debit_max["Date"] = debit_max.index
# debit_max.reset_index(drop=True, inplace=True)
# debit_max_ok=debit_max.drop([13], axis=0, inplace=True)

#Afficher le graphe du débit maximal annuel
# debit_max.plot(x="Date", y="Q")
# plt.title("Variation du débit maximal annuel")
# plt.xlabel("Année")
# plt.ylabel("Débit en m3/s")
# plt.grid(True)
# plt.savefig("debit_max.png", dpi=300)
# plt.show()


##############################################
####               Réponse 3              ####
##############################################

############### Sur chaque année  ############
#Débit moyen annuel
# debit_mean = debit_sans_na.groupby(pd.Grouper(key="Date", freq="Y")).mean()
# debit_mean["Date"] = debit_mean.index
# debit_mean.reset_index(drop=True, inplace=True)
# debit_mean_ok=debit_mean.drop([13], axis=0, inplace=True)

#Afficher le graphe du débit moyen annuel
# debit_mean.plot(x="Date", y="Q")
# plt.title("Variation du débit moyen annuel")
# plt.xlabel("Année")
# plt.ylabel("Débit en m3/s")
# plt.grid(True)
# plt.savefig("debit_mean.png", dpi=300)
# plt.show()

############# Sur chaque mois #################
#Grouper les dbéits par mois
# debit_mens = debit_sans_na.groupby(pd.Grouper(key="Date", freq="M")).mean()
# debit_mens["Date"] = debit_mens.index
# debit_mens.reset_index(drop=True, inplace=True)
# debit_mens.drop(debit_mens.index[147:159], axis=0, inplace=True)

#Afficher le graphe de débit moyen mensuel
# debit_mens.plot(x="Date", y="Q")
# plt.title("Variation du débit moyen mensuel")
# plt.xlabel("Année")
# plt.ylabel("Débit en m3/s")
# plt.grid(True)
# plt.savefig("debit_mean.png", dpi=300)
# plt.show()

############# Sur chaque deux années ############
#Grouper les débits par 2 années
# debit_2A = debit_sans_na.groupby(pd.Grouper(key="Date", freq="2Y")).mean()
# debit_2A["Date"] = debit_2A.index
# debit_2A.reset_index(drop=True, inplace=True)
# debit_2A.drop(debit_2A.index[147:159], axis=0, inplace=True)

#Afficher le graphe de débit moyen 
# debit_2A.plot(x="Date", y="Q")
# plt.title("Variation du débit moyen biannuel")
# plt.xlabel("Année")
# plt.ylabel("Débit en m3/s")
# plt.grid(True)
# plt.savefig("debit_mean.png", dpi=300)
# plt.show()

#####################################################
########        Réponse 4                      ######
#####################################################

#Divisons les donnees en 4 periodes
periode1 = debit_sans_na[0:1384]
periode2 = debit_sans_na[1385:2770]
periode3 = debit_sans_na[2771:4155]
periode4 = debit_sans_na[4156:5540]

#Evolution de débit pour la periode1
# periode1.plot(x="Date", y="Q")
# plt.title("Débit journalier sur la période 1")
# plt.xlabel("Année")
# plt.ylabel("Débit en m3/s")
# plt.grid(True)
# plt.savefig("debit_mean.png", dpi=300)
# plt.show()

#Evolution de débit pour la periode2
# periode2.plot(x="Date", y="Q")
# plt.title("Débit journalier sur la période 2")
# plt.xlabel("Année")
# plt.ylabel("Débit en m3/s")
# plt.grid(True)
# plt.savefig("debit_mean.png", dpi=300)
# plt.show()

#Evolution de debit pour la periode3
# periode3=periode3.dropna()
# periode3.plot(x="Date", y="Q")
# plt.title("Débit journalier sur la période 3")
# plt.xlabel("Année")
# plt.ylabel("Débit en m3/s")
# plt.grid(True)
# plt.savefig("debit_mean.png", dpi=300)
# plt.show()

#Evolution de debit pour la periode4
# periode4.plot(x="Date", y="Q")
# plt.title("Débit journalier sur la période 4")
# plt.xlabel("Année")
# plt.ylabel("Débit en m3/s")
# plt.grid(True)
# plt.savefig("debit_mean.png", dpi=300)
# plt.show()


################################################
####                                        ####
####             PARTIE 2                   ####
####                                        ####
################################################

#Chargement des données de pluviométrie
pluie = pd.read_csv("data/P_057_MIREBALAIS.txt", sep=";",skiprows=21) 
#Sélectioner les lignes et colonnes concernées
pluie = pluie.loc[1004:6939]
#Conversion de type de données
pluie['\tP'] = pd.to_numeric(pluie['\tP'], errors='coerce')
#Formater la colonne dâte
pluie["Date"] = pd.to_datetime(pluie["Date"], format="%Y-%m-%d") 

##############################################
####               Réponse 1              ####
##############################################

#Grouper les pluies par année
#Pluie minimale annuelle
# pluie_min = pluie.groupby(pd.Grouper(key="Date", freq="Y")).min()
# pluie_min["Date"] = pluie_min.index

# #Afficher le graphe de la pluie minimal annuelle
# pluie_min.plot(x="Date", y="\tP", label="P")
# plt.title("Variation de la pluie minimale annuelle")
# plt.xlabel("Année")
# plt.ylabel("Pluie en mm/an")
# plt.grid(True)
# plt.savefig("pluie_min.png", dpi=300)
# plt.show()

##############################################
####               Réponse 2              ####
##############################################

#Pluie maximale annuelle
# pluie_max = pluie.groupby(pd.Grouper(key="Date", freq="Y")).max()
# pluie_max["Date"] = pluie_max.index

# #Afficher le graphe de pluie maximale annuelle
# pluie_max.plot(x="Date", y="\tP", label="P")
# plt.title("Variation de la pluie maximale annuelle")
# plt.xlabel("Année")
# plt.ylabel("Pluie en mm/an")
# plt.grid(True)
# plt.savefig("pluie_min.png", dpi=300)
# plt.show()


##############################################
####               Réponse 3              ####
##############################################

#Representation graphique de type scatter
#Grouper les débits par mois
# debit_mens = debit_sans_na.groupby(pd.Grouper(key="Date", freq="M")).mean()
# debit_mens["Date"] = debit_mens.index
# debit_mens.reset_index(drop=True, inplace=True)
# debit_mens.drop(debit_mens.index[147:159], axis=0, inplace=True)
# debit_mens["Date"] = pd.to_datetime(debit_mens["Date"])

#Afficher le graphe du débit moyen mensuel
# plt.title("Débit moyen mensuel")
# plt.xlabel("Année")
# plt.ylabel("Débit en m3/s")
# plt.grid(True)
# plt.savefig("debit_mean.png", dpi=300)
# plt.scatter(x=debit_mens["Date"], y=debit_mens["Q"])
# plt.show()

#Grouper les pluies par mois
# pluie_mens = pluie.groupby(pd.Grouper(key="Date", freq="M")).mean()
# pluie_mens["Date"] = pluie_mens.index
# pluie_mens.reset_index(drop=True, inplace=True)
# pluie_mens.drop(pluie_mens.index[147:159], axis=0, inplace=True)
# pluie_mens["Date"] = pd.to_datetime(pluie_mens["Date"])

#Afficher le graphe de pluie moyen mensuel
# plt.title("Pluie moyenne mensuelle")
# plt.xlabel("Année")
# plt.ylabel("Pluie en mm/an")
# plt.grid(True)
# plt.savefig("debit_mean.png", dpi=300)
# plt.scatter(x=pluie_mens["Date"], y=pluie_mens["\tP"])
# plt.show()

##############################################
####               Réponse 4              ####
##############################################

#Coeficient de corrélation paerson
pluie = pluie.loc[1004:6939]
pluie_sans_na = pluie.dropna(subset=["\tP"])
pluie_sans_na.to_csv("output/pluie_sans_na.txt")
z = debit_sans_na.merge(pluie_sans_na, on ="Date")
x = z['Q'].values.tolist()
y = z['\tP'].values.tolist()
w = z.dropna(subset=["Q"])


#########  Avec  pandas    ################### 
coef_corr = z['Q'].corr(z['\tP']).round(decimals=2)
print(coef_corr)
plt.show()

##########  Manuellement  #####################
# def correlation(x,y):
       
#          x_mean = np.mean(x)
#          y_mean = np.mean(y)
#          numerator = np.sum((x - x_mean) * (y - y_mean))
#          denominator = np.sqrt(np.sum((x - x_mean) ** 2) * np.sum((y - y_mean) ** 2))
    
#          return (numerator / denominator).round(decimals=2)
    
# correlation(x,y)
# print(correlation(x,y))


###################             FIN          ###################













