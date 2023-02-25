#affichez l'approximation correspondante de e .

n =int(input("saisir le rang de l'approximation :"))

#definir la fonction factorielle

def fact(n):
    if n<=1:
        return 1
    else:
        return n*fact(n-1)
    
#initialisons e
e=0 
print(fact(n)) 
#calcul de la valeur approximee
for i in range(n+1):
    e=e + (1/fact(i))
    
print("la valeur approximee est {0}".format(e, ".3f"))



 
    

       