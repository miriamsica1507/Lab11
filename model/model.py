import networkx as nx
from database.dao import DAO


class Model:
    def __init__(self):
        self.G = nx.Graph()
        self._nodes = None
        self._edges = None

    def build_graph(self, year: int):
        """
        Costruisce il grafo (self.G) dei rifugi considerando solo le connessioni
        con campo `anno` <= year passato come argomento.
        Quindi il grafo avrà solo i nodi che appartengono almeno ad una connessione, non tutti quelli disponibili.
        :param year: anno limite fino al quale selezionare le connessioni da includere.
        """
        # TODO
        self.G.clear()
        self._edges = DAO.get_connessioni()
        self._nodes = DAO.get_rifugi()

        for edge in self._edges:
            if edge.anno <= year:
                r1_object = next((n for n in self._nodes if n.id == edge.id_rifugio_1), None)
                r2_object = next((n for n in self._nodes if n.id == edge.id_rifugio_2), None)
                if r1_object and r2_object:
                    self.G.add_edge(r1_object, r2_object)
        return self.G


    def get_nodes(self):
        """
        Restituisce la lista dei rifugi presenti nel grafo.
        :return: lista dei rifugi presenti nel grafo.
        """
        # TODO
        return list(self.G.nodes())

    def get_num_neighbors(self, node):
        """
        Restituisce il grado (numero di vicini diretti) del nodo rifugio.
        :param node: un rifugio (cioè un nodo del grafo)
        :return: numero di vicini diretti del nodo indicato
        """
        # TODO
        return self.G.degree(node)

    def get_num_connected_components(self):
        """
        Restituisce il numero di componenti connesse del grafo.
        :return: numero di componenti connesse
        """
        # TODO
        return nx.number_connected_components(self.G)

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
        a = self.get_reachable_bfs_tree(start)
        return a

        # TODO
    def get_reachable_bfs_tree(self, start):
        T = nx.bfs_tree(self.G, source=start)
        reachable_list = list(T.nodes())
        reachable_list.remove(start)
        return reachable_list
