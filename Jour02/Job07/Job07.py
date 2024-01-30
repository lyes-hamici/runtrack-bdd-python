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



class Employe:
    def __init__(self, host, user, password, database):
        self.conn = mysql.connector.connect(host=host, user=user, password=password, database=database)
        self.cursor = self.conn.cursor()

    def create_employe(self, nom,prenom, salaire):
        sql_query = "INSERT INTO employe (nom,prenom,salaire) VALUES (%s,%s,%s)"
        values = (nom, prenom, salaire)
        self.cursor.execute(sql_query, values)
        self.conn.commit()

    def read_employe(self):
        sql_query = "SELECT * FROM employe"
        self.cursor.execute(sql_query)
        return self.cursor.fetchall()

    def update_employe(self,employe_id,nv_nom,nv_prenom,nv_salaire):
        sql_query = "UPDATE employe SET nom=%s, prenom=%s, salaire=%s WHERE id=%s"
        values = (nv_nom, nv_prenom, nv_salaire, employe_id)
        self.cursor.execute(sql_query, values)
        self.conn.commit()

    def delete_employe(self, employe_id):
        sql_query = "DELETE FROM employe WHERE id=%s"
        values = (employe_id,)
        self.cursor.execute(sql_query, values)
        self.conn.commit()

    def close_connection(self):
        self.cursor.close()
        self.conn.close()


employe_manager = Employe(host='localhost', user=user, password=mdp, database='Job07')
# Exemple d'opérations CRUD
employe_manager.create_employe('John','Doe',50000)
print("Liste des salariés après création :")
print(employe_manager.read_employe())

employe_manager.update_employe(1,'Jhon','Doe Jr',5000)
print("Liste des salariés après mise à jour :")
print(employe_manager.read_employe())

employe_manager.delete_employe(employe_id=1)
print("Liste des salariés après suppression :")
print(employe_manager.read_employe())

# Fermer la connexion à la base de données
employe_manager.close_connection()
