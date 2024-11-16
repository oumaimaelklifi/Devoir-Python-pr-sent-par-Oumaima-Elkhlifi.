
# Ajouter un élément en-tête de liste (empiler).
def Empiler(liste,valeur):
    nouvelle_liste=[valeur]
    for element in liste:
        nouvelle_liste.append(element )
    return nouvelle_liste    
  

# Ajouter un élément en fin de liste (enfiler).
def Enfiler(list,value):
    list.append(value)
    return list

# Vérifier si un élément appartient à une liste.
def Verfication(liste, element):
    for item in liste:
        if item == element:
            return True
    return False

# Dépiler un élément dans une liste
def Depiler(liste, element):
    for i in range(len(liste)-1, -1, -1): 
        if liste[i] == element:
            del liste[i] 
            break  
    return liste

# Supprimer un élément d'une liste.
def Supprimer(liste, element):
    for i in range(len(liste)):
        if liste[i] == element:
            del liste[i] 
            break  
    return liste

# Calculer la longueur d'une liste.
def Calculer_Longueur(liste):
    longueur=0
    for valeur in liste:
        longueur+=1
    return longueur
#Dans cette exercice on peut utiliser la fonction len 
# def Calculer_Longueur(liste):
#    return len(liste)
 
# Remplacer un élément par un autre dans une liste.
def Remplacer_Element(liste, ancien, nouveau):
    for i in range(len(liste)):
        if liste[i] == ancien:
            liste[i] = nouveau 
    return liste

# Afficher le contenu d'une liste.
def Afficher_liste(liste):
    print("Contenu de la liste :", liste)

# Trouver l'occurrence d’un élément dans une liste.
def Occurrence(liste, element):
    occurrence = 0
    for valeur in liste:
        if valeur == element:
            occurrence += 1  
    return f"Nombre d'occurrences de {element} : {occurrence}"

        
# Vérifier si une liste est ordonnée
def Liste_Ordonnee(liste):
    for i in range(len(liste) - 1):
        if liste[i] > liste[i + 1]:  
            return False
    return True

#Trier une liste.
def Trier_Liste(liste):
    for i in range(len(liste)):
        for j in range(i + 1, len(liste)):
            if liste[i] > liste[j]:  
                liste[i], liste[j] = liste[j], liste[i]
    return liste


#Insérer un élément dans une liste triée.
def Inserer_Element(liste, element):
    for i in range(len(liste)):
        if liste[i] > element:
            liste.insert(i, element) 
            return liste
    liste.append(element) 
    return liste

# Vérifier si deux listes sont égales.
def Comparer_deux_liste(liste1, liste2):
    if Calculer_Longueur(liste1) != Calculer_Longueur(liste2):  
        return False
    for i in range(len(liste1)):
        if liste1[i] != liste2[i]: 
            return False
    return True

# Concaténer deux listes.
def Concatener_deux_liste(liste1,liste2):
    return liste1 + liste2

# inverser une liste.
def Inverser_liste(liste):
    liste_inversee = []  
    for i in range(len(liste) - 1, -1, -1):  
        liste_inversee.append(liste[i])
    return liste_inversee


# Tester toutes les fonctions

# Empiler
liste = [2, 3, 4]
print("Empiler :", Empiler(liste, 1))  

# Enfiler
liste = [1, 2, 3]
print("Enfiler :", Enfiler(liste, 4))  

# Vérification
liste = [1, 2, 3]
print("Vérification (2 dans la liste) :", Verfication(liste, 2))  
 
# Dépiler
liste = [1, 2, 3, 4]
print("Dépiler (supprimer 3) :", Depiler(liste, 3)) 

# Supprimer
liste = [1, 2, 3, 4]
Supprimer(liste, 2)
print("Supprimer :", liste)

# Calculer Longueur
liste = [1, 2, 3, 4]
print("Longueur :", Calculer_Longueur(liste))  

# Remplacer
liste = [1, 2, 3, 4]
print("Remplacer (2 par 5) :", Remplacer_Element(liste, 2, 5)) 

# Afficher la liste
liste = [1, 2, 3, 4]
Afficher_liste(liste)  

# Trouver l'occurrence
liste = [1, 2, 2, 3, 4, 2]
print("Occurrence (2) :", Occurrence(liste, 2))

# Vérifier si liste est ordonnée
liste = [1, 2, 3, 4]
print("Liste ordonnée :", Liste_Ordonnee(liste))  
 

# Trier une liste
liste = [4, 2, 3, 1]
print("Trier :", Trier_Liste(liste)) 

# Insérer dans une liste triée
liste = [1, 2, 4, 5]
print("Insérer (3) :", Inserer_Element(liste, 3))  

# Comparer deux listes
liste1 = [1, 2, 3]
liste2 = [1, 2, 3]
print("Comparer :", Comparer_deux_liste(liste1, liste2))  


# Concaténer deux listes
liste1 = [1, 2, 3]
liste2 = [4, 5, 6]
print("Concaténer :", Concatener_deux_liste(liste1, liste2))  

# Inverser une liste
liste = [1, 2, 3, 4]
print("Inverser :", Inverser_liste(liste)) 
