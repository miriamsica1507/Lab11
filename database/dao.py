from database.DB_connect import DBConnect
from model.connessioni import Connessioni
from model.rifugio import Rifugio


class DAO:
    """
        Implementare tutte le funzioni necessarie a interrogare il database.
        """
    # TODO
    @staticmethod
    def get_connessioni():
        connessioni = []
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        query = (
            'select c.id as id_connessione,c.id_rifugio1 , c.id_rifugio2, r1.nome as nome_rifugio_1, r2.nome as nome_rifugio_2, c.anno, r1.localita as localita1, r2.localita as localita2 '
            'from rifugio r1 , rifugio r2, connessione c '
            'where r1.id = c.id_rifugio1 and r2.id = c.id_rifugio2')
        cursor.execute(query)
        for row in cursor:
            connessione = Connessioni(row['id_connessione'],
                             row['id_rifugio1'],
                             row['id_rifugio2'],
                             row['nome_rifugio_1'],
                             row['nome_rifugio_2'],
                             row['anno'],
                             row['localita1'],
                             row['localita2'])
            connessioni.append(connessione)
        cursor.close()
        conn.close()
        return connessioni

    @staticmethod
    def get_rifugi():
        rifugi = []
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        query = "select r.id, r.nome, r.localita from rifugio r"
        cursor.execute(query)
        for row in cursor:
            rifugio = Rifugio(row['id'],
                             row['nome'],
                             row['localita'])
            rifugi.append(rifugio)
        cursor.close()
        conn.close()
        return rifugi

