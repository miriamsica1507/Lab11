from database.DB_connect import DBConnect
from model.rifugi import Rifugi


class DAO:
    """
        Implementare tutte le funzioni necessarie a interrogare il database.
        """
    # TODO
    @staticmethod
    def get_rifugio_anno(anno_inserito):
        rifugi = []
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        query = ('select c.id as id_connessione,c.id_rifugio1 , c.id_rifugio2, r1.nome as nome_rifugio_1, r2.nome as nome_rifugio_2, c.anno, r1.localita as localita1, r2.localita as localita ' 
                'from rifugio r1 , rifugio r2, connessione c '
                'where r1.id = c.id_rifugio1 and r2.id = c.id_rifugio2 and c.anno <= %s'
                'order by c.id asc')
        cursor.execute(query, (anno_inserito,))
        for row in cursor:
            rifugio = Rifugi(row['id_connessione'],
                             row['id_rifugio1'],
                             row['id_rifugio2'],
                             row['nome_rifugio_1'],
                             row['nome_rifugio_2'],
                             row['anno'],
                             row['localita1'],
                             row['localita2'])
            rifugi.append(rifugio)
        cursor.close()
        conn.close()
        return rifugi


