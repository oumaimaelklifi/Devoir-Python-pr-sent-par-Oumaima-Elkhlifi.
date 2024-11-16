
#créer une liste de personnes ;
def Personne():
    N = input("Quel est votre nom ? ")
    P = input("Quel est votre prénom ? ")
    G = input("Quel est votre genre ? ")
    A = int(input("Quel est votre âge ? "))
   
    personne=[N,P,G,A]
    
    return personne  

#Lister cette liste
def Lister_Personne(list_personne):
    print("Liste des personnes :")
    for personne in list_personne:

        print(f"Nom : {personne[0]}, Prénom : {personne[1]}, Age : {personne[3]}, Genre : {personne[2]}")


#Chercher une personne de cette liste
def Chercher_Personne(liste_personne, Nom):
    for personne in liste_personne:
        if personne[0].lower() == Nom.lower():
            return personne 
    return None  

#test
Liste_Personne = []


for i in range(1):
    p = Personne()
    Liste_Personne.append(p)


Lister_Personne(Liste_Personne)


nom_a_chercher = input("Quel nom voulez-vous chercher ? ")
personne_trouvee = Chercher_Personne(Liste_Personne, nom_a_chercher)

if personne_trouvee:
    print(f"Personne trouvée : Nom : {personne_trouvee[0]}, Prénom : {personne_trouvee[1]}, Age : {personne_trouvee[3]}, Genre : {personne_trouvee[2]}")
else:
    print(f"Aucune personne trouvée avec le om {nom_a_chercher}.")


