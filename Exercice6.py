
# Ajouter un élément dans un ensemble.
def Ajouter_element(liste,element):
   if element not in liste: 
      liste.append(element)
   return liste

# Transformer une liste en un ensemble
def List_Vers_Eensembe(liste):
   ensemble=[]
   for element in liste:
      if element not in ensemble:
         ensemble.append(element)
   return ensemble

# Vérifier que deux ensembles sont égaux.
def Ensemble_Egaux(ensemble1,ensemble2):
   if len(ensemble1)!=len(ensemble2):
      return False
   for element in ensemble1:
        if element not in ensemble2:
            return False
   return True

# Vérifier qu’un ensemble est inclus dans un autre.
def iensemble_inclus(ensemble1,ensemble2):
   for element in ensemble1:
      if element not in ensemble2:
         return False 
   return True 

# Faire l’intersection de deux ensembles.
def intersection_ensembles(ensemble1,ensemble2):
   resultat=[]
   for element in ensemble2:
      if element in ensemble2:
         resultat.append(element)
   return resultat

# Faire l’union de deux ensembles.
def union_ensembles(ensemble1,ensemble2):
   union=[]
   for element in ensemble1:
      if element not in union:
         union.append(element)
   for element in ensemble2:
      if element not in union:
         union.append(element)
   return union


# Vérifier que deux ensembles sont complémentaires pour autre ensemble.
def ensemble_complementaires(ensemble1,ensemble2,ensemble_total):
   union_ensemble=union_ensembles(ensemble1,ensemble2)
   return Ensemble_Egaux(union_ensemble,ensemble_total)

# Ajouter un élément dans un ensemble
def ajouter_element(ensemble, element):
    if element not in ensemble:
        ensemble.append(element)
    return ensemble

# Transformer une liste en un ensemble
def liste_vers_ensemble(liste):
    ensemble = []
    for element in liste:
        if element not in ensemble:
            ensemble.append(element)
    return ensemble

# Vérifier que deux ensembles sont égaux
def ensembles_egaux(ensemble1, ensemble2):
    if len(ensemble1) != len(ensemble2):
        return False
    for element in ensemble1:
        if element not in ensemble2:
            return False
    return True

# Vérifier qu’un ensemble est inclus dans un autre
def ensemble_inclus(ensemble1, ensemble2):
    for element in ensemble1:
        if element not in ensemble2:
            return False
    return True

# Faire l’intersection de deux ensembles
def intersection_ensembles(ensemble1, ensemble2):
    resultat = []
    for element in ensemble1:
        if element in ensemble2:
            resultat.append(element)
    return resultat

# Faire l’union de deux ensembles
def union_ensembles(ensemble1, ensemble2):
    resultat = ensemble1[:]
    for element in ensemble2:
        if element not in resultat:
            resultat.append(element)
    return resultat

# Vérifier que deux ensembles sont complémentaires pour un autre ensemble
def ensembles_complementaires(ensemble1, ensemble2, ensemble_total):
    union_des_deux = union_ensembles(ensemble1, ensemble2)
    return ensembles_egaux(union_des_deux, ensemble_total)


# Tests
ensemble1 = [1, 2, 3]
ensemble2 = [3, 4, 5]
ensemble_total = [1, 2, 3, 4, 5]
   
print("Ajouter un élément :")
print(ajouter_element(ensemble1, 4))  

print("\nTransformer une liste en ensemble :")
print(liste_vers_ensemble([1, 2, 2, 3, 3, 4]))  

print("\nVérifier que deux ensembles sont égaux :")
print(ensembles_egaux([1, 2, 3], [3, 2, 1]))  
print(ensembles_egaux([1, 2, 3], [1, 2]))    

print("\nVérifier qu’un ensemble est inclus dans un autre :")
print(ensemble_inclus([1, 2], [1, 2, 3]))  
print(ensemble_inclus([1, 4], [1, 2, 3]))

print("\nIntersection de deux ensembles :")
print(intersection_ensembles(ensemble1, ensemble2))

print("\nUnion de deux ensembles :")
print(union_ensembles(ensemble1, ensemble2))  
 
print("\nVérifier que deux ensembles sont complémentaires :")
print(ensembles_complementaires([1, 2], [3, 4, 5], ensemble_total))  
print(ensembles_complementaires([1, 2], [3, 4], ensemble_total))   
