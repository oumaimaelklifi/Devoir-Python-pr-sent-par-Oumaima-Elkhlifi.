
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
def Verfication(liste,element):
    return element in liste

# Dépiler un élément dans une liste
def Depiler(liste, element):
    for i in range(len(liste)-1,-1,-1):
        if element == liste[i]:
            del liste[i]  
            break  
    return liste

# Supprimer un élément d'une liste.
def Supprimer(liste, element):
    for i in range(len(liste)):
        if element == liste[i]:
            del liste[i]  
            break  

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
def Remplacer_Element(liste,ancien,nouveu):
    for i,y in enumerate(liste):
        if y==ancien:
            liste[i]=nouveu
    return liste

# Afficher le contenu d'une liste.
def Afficher_liste(liste):
    print("Contenu de la liste :", liste)

# Trouver l'occurrence d’un élément dans une liste.
def Occurrence(liste,element):
    occurrence=0
    for valeur in liste:
        if valeur==element:
            occurrence+=1
    return f"Nombre d occurence est {occurrence}"

        
# Vérifier si une liste est ordonnée
def Liste_Ordonnee(liste):
    for i,y in enumerate(liste):
        if liste[i]>liste[i+1]:
            return False 
    return True
    
#Trier une liste.
def Trier_Liste(liste):
    for i in range(len(liste)):
        min_index = i
        for j in range(i + 1, len(liste)):
            if liste[j] < liste[min_index]:
                min_index = j
        liste[i], liste[min_index] = liste[min_index], liste[i]
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
def Comparer_deux_liste(liste1,liste2):
    if len(liste1)!=len(liste2):
        return False 
    else :
        for i in range(len(liste1)):
            if(liste1[i]!=liste2[i]):
                return False 
    return True 


# Concaténer deux listes.
def Concatener_deux_liste(liste1,liste2):
    return liste1 + liste2

# inverser une liste.
def Inverser_liste(liste):
    liste_inversee=[]
    for i in range(len(liste)-1,-1,-1):
        liste_inversee.append(liste[i])
    return liste_inversee