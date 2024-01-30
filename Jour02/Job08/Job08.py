import getpass
import mysql.connector

user = getpass.getpass('Entrez votre nom user  : ')
mdp = getpass.getpass('Entrez votre mdp  : ')


conn = mysql.connector.connect(
    host="localhost",
    user=user,
    password=mdp,
    database="zoo"
)
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS animal (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nom VARCHAR(255),
        race VARCHAR(255),
        cage_id INT,
        date_naissance DATE,
        pays_origine VARCHAR(255)
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS cage (
        id INT AUTO_INCREMENT PRIMARY KEY,
        superficie FLOAT,
        capacite_max INT
    )
''')

def ajouter_animal(nom, race, cage_id, date_naissance, pays_origine):
    cursor.execute(f"INSERT INTO animal (nom, race, cage_id, date_naissance, pays_origine) VALUES ('{nom}', '{race}', {cage_id}, '{date_naissance}', '{pays_origine}')")
    conn.commit()

def supprimer_animal(animal_id):
    cursor.execute(f"DELETE FROM animal WHERE id = {animal_id}")
    conn.commit()

def modifier_animal(animal_id, nom, race, cage_id, date_naissance, pays_origine):
    cursor.execute(f"UPDATE animal SET nom='{nom}', race='{race}', cage_id={cage_id}, date_naissance='{date_naissance}', pays_origine='{pays_origine}' WHERE id={animal_id}")
    conn.commit()

def afficher_animaux():
    cursor.execute('SELECT * FROM animal')
    animaux = cursor.fetchall()
    for animal in animaux:
        print(animal)

def afficher_animaux_cages():
    cursor.execute("SELECT cage.id, cage.superficie, cage.capacite_max, animal.* FROM cage LEFT JOIN animal ON cage.id = animal.cage_id")
    animaux_cages = cursor.fetchall()
    for animal_cage in animaux_cages:
        print(animal_cage)

def calculer_superficie_totale():
    superficie_totale = 0
    cursor.execute('SELECT superficie FROM cage')
    for ligne in cursor.fetchall():
        superficie_totale += ligne[0]
    print(f"Superficie totale de toutes les cages : {superficie_totale} m²")

def ajouter_cage(superficie, capacite_max):
    cursor.execute(f"INSERT INTO cage (superficie, capacite_max) VALUES ({superficie}, {capacite_max})")
    conn.commit()


while True:
    print("\nMenu:")
    print("1. Ajouter un animal")
    print("2. Supprimer un animal")
    print("3. Modifier un animal")
    print("4. Afficher la liste des animaux")
    print("5. Afficher la liste des animaux dans les cages")
    print("6. Calculer la superficie totale des cages")
    print("7. Ajouter une cage")
    print("0. Quitter")

    choix = input("Choisissez une option : ")

    if choix == "1":
        nom = input("Nom de l'animal : ")
        race = input("Race de l'animal : ")
        cage_id = int(input("ID de la cage : "))
        date_naissance = input("Date de naissance (AAAA-MM-JJ) : ")
        pays_origine = input("Pays d'origine : ")
        ajouter_animal(nom, race, cage_id, date_naissance, pays_origine)

    elif choix == "2":
        animal_id = int(input("ID de l'animal à supprimer : "))
        supprimer_animal(animal_id)

    elif choix == "3":
        animal_id = int(input("ID de l'animal à modifier : "))
        nom = input("Nouveau nom de l'animal : ")
        race = input("Nouvelle race de l'animal : ")
        cage_id = int(input("Nouvel ID de la cage : "))
        date_naissance = input("Nouvelle date de naissance (AAAA-MM-JJ) : ")
        pays_origine = input("Nouveau pays d'origine : ")
        modifier_animal(animal_id, nom, race, cage_id, date_naissance, pays_origine)

    elif choix == "4":
        afficher_animaux()

    elif choix == "5":
        afficher_animaux_cages()

    elif choix == "6":
        calculer_superficie_totale()

    if choix == "7":
        superficie = float(input("Superficie de la nouvelle cage : "))
        capacite_max = int(input("Capacité maximale de la nouvelle cage : "))
        ajouter_cage(superficie, capacite_max)
    elif choix == "0":
        break

    else:
        print("Option invalide. Veuillez choisir une option valide.")