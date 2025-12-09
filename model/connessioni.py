from dataclasses import dataclass

@dataclass
class Connessioni:
    id_connessione : int
    id_rifugio_1 : int
    id_rifugio_2 : int
    nome_rifugio_1 : str
    nome_rifugio_2 : str
    anno : int
    localita1 : str
    localita2 : str