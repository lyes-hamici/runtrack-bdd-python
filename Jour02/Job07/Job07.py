import mysql.connector
import getpass


user = getpass.getpass('Entrez votre nom user  : ')
mdp = getpass.getpass('Entrez votre mdp  : ')
# Paramètres de connexion à la base de données
host = 'localhost'
user = user
password = mdp
database = 'Job07'



conn = mysql.connector.connect(host=host, user=user, password=password, database=database)

# Créer un objet curseur pour exécuter des requêtes SQL
cursor = conn.cursor()

# Exemple d'exécution d'une requête SELECT
query = "SELECT *  FROM employe WHERE salaire > 3000;"
cursor.execute(query)

# Récupérer les résultats de la requête
result = cursor.fetchall()

# Afficher les résultats
for row in result:
    print(row)

cursor.close()
conn.close()




conn2 = mysql.connector.connect(host=host, user=user, password=password, database=database)

# Créer un objet curseur pour exécuter des requêtes SQL
cursor2 = conn2.cursor()
# Exemple d'exécution d'une requête SELECT
query2 = "SELECT employe.id, employe.nom,employe.prenom, service.nom AS service_nom FROM employe JOIN service ON employe.id_service = service.id;"
cursor2.execute(query2)

# Récupérer les résultats de la requête
result2 = cursor2.fetchall()

# Afficher les résultats
for row in result2:
    print(row)

# Fermer le curseur et la connexion
cursor2.close()
conn2.close()



class Salarie:
    def __init__(self, host, user, password, database):
        self.conn = mysql.connector.connect(host=host, user=user, password=password, database=database)
        self.cursor = self.conn.cursor()

    def create_salarie(self, nom, poste, salaire):
        sql_query = "INSERT INTO salarie (nom, poste, salaire) VALUES (%s, %s, %s)"
        values = (nom, poste, salaire)
        self.cursor.execute(sql_query, values)
        self.conn.commit()

    def read_salarie(self):
        sql_query = "SELECT * FROM salarie"
        self.cursor.execute(sql_query)
        return self.cursor.fetchall()

    def update_salarie(self, salarie_id, nv_nom, nv_poste, nv_salaire):
        sql_query = "UPDATE salarie SET nom=%s, poste=%s, salaire=%s WHERE id=%s"
        values = (nv_nom, nv_poste, nv_salaire, salarie_id)
        self.cursor.execute(sql_query, values)
        self.conn.commit()

    def delete_salarie(self, salarie_id):
        sql_query = "DELETE FROM salarie WHERE id=%s"
        values = (salarie_id,)
        self.cursor.execute(sql_query, values)
        self.conn.commit()

    def close_connection(self):
        self.cursor.close()
        self.conn.close()


salarie_manager = Salarie(host='localhost', user=user, password=mdp, database='Job07')
# Exemple d'opérations CRUD
salarie_manager.create_salarie('John Doe','Ingénieur',50000)
print("Liste des salariés après création :")
print(salarie_manager.read_salarie())

salarie_manager.update_salarie(salarie_id=1, nv_nom='John Doe Jr', nv_poste='Développeur', nv_salaire=60000)
print("Liste des salariés après mise à jour :")
print(salarie_manager.read_salarie())

salarie_manager.delete_salarie(salarie_id=1)
print("Liste des salariés après suppression :")
print(salarie_manager.read_salarie())

# Fermer la connexion à la base de données
salarie_manager.close_connection()
