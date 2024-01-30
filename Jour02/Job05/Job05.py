import mysql.connector
import getpass


user = getpass.getpass('Entrez votre nom user  : ')
mdp = getpass.getpass('Entrez votre mdp  : ')
# Paramètres de connexion à la base de données
host = 'localhost'
user = user
password = mdp
database = 'LaPlateforme'



conn = mysql.connector.connect(host=host, user=user, password=password, database=database)

# Créer un objet curseur pour exécuter des requêtes SQL
cursor = conn.cursor()

# Exemple d'exécution d'une requête SELECT
query = "SELECT SUM(superficie) AS superficie_total FROM etage"
cursor.execute(query)

# Récupérer les résultats de la requête
result = cursor.fetchall()

# Afficher les résultats
for row in result:
    print(f"la superficie de LaPlateforme est de {row} m²")

# Fermer le curseur et la connexion
cursor.close()
conn.close()