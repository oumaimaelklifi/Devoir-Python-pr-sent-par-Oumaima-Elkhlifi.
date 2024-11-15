
def Personne():
    N = input("Quel est votre nom ? ")
    P = input("Quel est votre prénom ? ")
    G = input("Quel est votre genre ? ")
    A = int(input("Quel est votre âge ? "))
   
    personne = {'Nom': N, 'Prenom': P, 'Genre': G, 'Age': A}
    
    return personne  

def Lister_Personne(list_personne):
    print("Liste des personnes :")
    for personne in list_personne:
      
        print(f"Nom : {personne['Nom']}, Prénom : {personne['Prenom']}, Age : {personne['Age']}, Genre : {personne['Genre']}")

def Chercher_Personne(liste_personne, Nom):
    for personne in liste_personne:
        if personne['Nom'].lower() == Nom.lower():
            return personne 
    return None  

#test
Liste_Personne = []


for i in range(3):
    p = Personne()
    Liste_Personne.append(p)


Lister_Personne(Liste_Personne)


nom_a_chercher = input("Quel nom voulez-vous chercher ? ")
personne_trouvee = Chercher_Personne(Liste_Personne, nom_a_chercher)

if personne_trouvee:
    print(f"Personne trouvée : Nom : {personne_trouvee['Nom']}, Prénom : {personne_trouvee['Prenom']}, Age : {personne_trouvee['Age']}, Genre : {personne_trouvee['Genre']}")
else:
    print(f"Aucune personne trouvée avec le nom {nom_a_chercher}.")


