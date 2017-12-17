# Ejercicio 1 de DGP. Realizado por :
# Ramona Verónica Moise.

# Funciones en python

# La función suma de una lista por recursión:

def suma(l):
    acum=0 
    for x in l:
        acum+=x
    return acum

# La función suma de cuadrados de una lista por comprensión:

def suma_cuadrados(n):
    return sum([i**2 for i in n if i%2==0])


# La función máximo de una lista:

def máximo(l):
    max_val=-float("inf")
    for x in l:
        if x>max_val:
            max_val=x
    return max_val


# La función multiplicación de un escalar por una matriz:

def prod_map(x,l)
    res=[]
    for n in l:
        res.append(x*n)
    return res
