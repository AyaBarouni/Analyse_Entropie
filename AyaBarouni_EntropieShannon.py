import math
from collections import Counter  # Permet de créer des dictionnaires qui prennent en clé les caractères uniques et en valeur le nombre de fois que chaque caractère apparaît

def calculer_entropie(mot_de_passe):
    if not mot_de_passe:
        return 0  # Cas où aucun mot de passe n'est saisi

    frequences = Counter(mot_de_passe)  # Compte les occurrences de chaque caractère
    longueur_totale = len(mot_de_passe)
    
    entropie = 0  # Initialisation de l'entropie
    
    for nb_apparitions in frequences.values():  # Pour chaque fréquence de caractère, on applique la formule de Shannon
        p_i = nb_apparitions / longueur_totale  # Calcul de probabilité
        entropie -= p_i * math.log2(p_i)  # On ajoute un moins car log2 donne un nombre négatif
        
    return entropie


test_mdp = input("Entrez un mot de passe à tester : ")
print("Longueur du mot de passe :", len(test_mdp), "caractères")

while len(test_mdp) < 12:
    print("Attention : Votre mot de passe est trop court. Veuillez saisir au moins 12 caractères.")
    test_mdp = input("Entrez un mot de passe à tester : ")
    print("Longueur du mot de passe :", len(test_mdp), "caractères")

print("Longueur satisfaisante.")

resultat = calculer_entropie(test_mdp)

print("Score d'entropie :", f"{resultat:.2f}", "bits par caractère")
# Le .2f spécifie qu'on veut un float avec deux chiffres après la virgule.
if resultat < 2:
    print("Risque élevé : trop de répétitions ou trop simple.")
elif resultat < 3.5:
    print("Sécurité modérée : complexité acceptable.")
else:
    print("Haute résistance : grande diversité de caractères.")