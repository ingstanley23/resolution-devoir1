# les termes de la suite de fibonacci

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-2) + fib(n-1) 
a = int(input("entrer la valeur de n"))  
for n in range(0,a+1):
    print(f"fibonacci({n}) = {fib(n)}")
    
    
#fin

