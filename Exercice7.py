
import math as m

# la somme
def Somme(liste):
    somme=0
    for i in liste:
        somme+=i
    return somme

# la moyenne
def Moyenne(liste):
    if not liste:
        return False 
    else :
        count=0
        somme=Somme(liste)
        for y in liste:
            count+=1
        return somme/count
     
# le produit
def Produit(liste):
    if not liste:
        return False
    produit=1
    for valeur in liste:
        produit*=valeur
    return produit

# le max
def Max(liste):
    if not liste:
        return False 
    max=liste[0]
    for value in liste:
        if value > max :
            max=value
    return max

# le min
def Min(liste):
    if not liste:
        return False 
    min=liste[0]
    for value in liste:
        if value < min :
            min=value
    return min

# la variance
def Variance(liste):
    moyenn = Moyenne(liste)
    variance = 0
    for valeur in liste:
        variance+=(valeur - moyenn)**2
    return (variance / len(liste))

# l’écart-type
def Ecart_Type(liste):
    var=Variance(liste)
    return m.sqrt(var)

# la covariance
def Covariance(liste1,liste2):
    if len(liste1) != len(liste2):
        return False
    
    moyenne_liste1=Moyenne(liste1)
    moyenne_liste2=Moyenne(liste2)

    somme_produits=0
    for i in range(len(liste1)):
        somme_produits+=liste1[i]*liste2[i]

    return (somme_produits)/len(liste1) - moyenne_liste1*moyenne_liste2

#Le test 
liste1 = [1, 2, 3, 4, 5]
liste2 = [5, 4, 3, 2, 1]

print(f'La somme est : {Somme(liste1)}')
print(f'Le produit est : {Produit(liste2)}')
print(f'La moyenne est : {Moyenne(liste2)}')
print(f'Le max est : {Max(liste1)}')
print(f'Le min est : {Min(liste1)}')
print(f'La variance est : {Variance(liste1)}')
print(f'L ecart type est : {Ecart_Type(liste1)}')
print(f'La covariance est : {Covariance(liste1,liste2)}')

   



