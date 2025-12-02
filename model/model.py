import networkx as nx
from database.dao import DAO


class Model:
    def __init__(self):
        self.G = nx.Graph()

    def build_graph(self, year: int):
        """
        Costruisce il grafo (self.G) dei rifugi considerando solo le connessioni
        con campo `anno` <= year passato come argomento.
        Quindi il grafo avrà solo i nodi che appartengono almeno ad una connessione, non tutti quelli disponibili.
        :param year: anno limite fino al quale selezionare le connessioni da includere.
        """
        # TODO
        rifugi_filtrati = DAO.get_rifugio_anno(year)
        self.G.clear()
        # devo verificare che i vari nodi che prendo siano uguali o id_rifugio1 o id_rifugio2, con un if e si avrà una connessione
        for r in rifugi_filtrati:
            u = r.id_rifugio1
            v = r.id_rifugio2
            self.G.add_edge(u, v)


    def get_nodes(self):
        """
        Restituisce la lista dei rifugi presenti nel grafo.
        :return: lista dei rifugi presenti nel grafo.
        """
        # TODO

    def get_num_neighbors(self, node):
        """
        Restituisce il grado (numero di vicini diretti) del nodo rifugio.
        :param node: un rifugio (cioè un nodo del grafo)
        :return: numero di vicini diretti del nodo indicato
        """
        # TODO

    def get_num_connected_components(self):
        """
        Restituisce il numero di componenti connesse del grafo.
        :return: numero di componenti connesse
        """
        # TODO

    def get_reachable(self, start):
        """
        Deve eseguire almeno 2 delle 3 tecniche indicate nella traccia:
        * Metodi NetworkX: `dfs_tree()`, `bfs_tree()`
        * Algoritmo ricorsivo DFS
        * Algoritmo iterativo
        per ottenere l'elenco di rifugi raggiungibili da `start` e deve restituire uno degli elenchi calcolati.
        :param start: nodo di partenza, da non considerare nell'elenco da restituire.

        ESEMPIO
        a = self.get_reachable_bfs_tree(start)
        b = self.get_reachable_iterative(start)
        b = self.get_reachable_recursive(start)

        return a
        """

        # TODO
    def get_reachable_bfs_tree(self, start):
        pass

    def get_reachable_iterative(self, start):
        pass

    def get_reachable_recursive(self, start):
        pass
