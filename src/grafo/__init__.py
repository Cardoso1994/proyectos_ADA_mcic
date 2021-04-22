#!/usr/bin/env python3
################################################################################
#
# Desarrollador: Marco Antonio Cardoso Moreno
#
# Clase Grafo. Implementación
#
# Abril 2021
#
################################################################################

import sys
from arista import Arista

class Grafo(object):
    """
    Clase Grafo.
    Generación y manejo de Grafos

    Parametros
    ----------
    id : str
        id o nombre del Grafo
    dirigido : bool
        True si el Grafo es dirigido, de otro modo, False

    Atributos
    ---------
    id : str
        id o nombre del Grafo
    dirigido : bool
        True si el Grafo es dirigido, de otro modo, False
    V : dict
        Diccionario de Nodos o Vertices del Grafo.
        key: Nodo.id
        value: Nodo
    E : dict
        Diccionario de Aristas (edges) del Grafo
        key: Arista.id
        value: Arista

    """
    def __init__(self, id='grafo', dirigido=False):
        self.id =       id
        self.dirigido = dirigido
        self.V =        dict()
        self.E =        dict()
        self.attr =     dict()

    def __repr__(self):
        """
        Asigna representación repr a los Grafos

        Returns
        -------
        str
            representación en str de los Grafos
        """
        return str("id: " + str(self.id) + '\n'
                   + 'nodos: ' + str(self.V.values()) + '\n'
                   + 'aristas: ' + str(self.E.values()))

    def add_nodo(self, nodo):
        """
        Agrega objeto nodo al grafo

        Parametros
        ----------
        nodo : Nodo
            objeto Nodo que se va a agregar a self.V

        Returns
        -------
        None
        """
        self.V[nodo.id] = nodo

    def add_arista(self, arista):
        """
        Agrega arista al grafo si esta no existe de antemano en dicho grafo.

        Parametros
        ----------
        arista : Arista
            objeto Arista que se va agregar a self.E

        Returns
        -------
        True o False : bool
            True si se agrego la arista, de otro modo, False

        """
        if self.get_arista(arista.id):
            return False

        self.E[arista.id] = arista
        return True

    def get_arista(self, arista_id):
        """
        Revisa si la arista ya existe en el grafo

        Parametros
        ----------
        arista_id : Arista.id
            atributo id de un objeto de la clase Arista

        Returns
        -------
        True o False : bool
            True si la arista existe, de otro modo, Falso
        """
        if self.dirigido:
            return arista_id in self.E
        else:
            u, v = arista_id
            return (u, v) in self.E or (v, u) in self.E

    def to_graphviz(self, filename):
        """
        Exporta grafo a formato graphvizDOT

        Parametros
        ----------
        filename : file
            Nombre de archivo en el que se va a escribir el grafo

        Returns
        -------
        None
        """
        edge_connector = "--"
        graph_directive = "graph"
        if self.dirigido:
            edge_connector = "->"
            graph_directive = "digraph"

        with open(filename, 'w') as f:
            f.write(f"{graph_directive} {self.id} " + " {\n")
            for nodo in self.V:
                f.write(f"{nodo};\n")
            for arista in self.E.values():
                f.write(f"{arista.u} {edge_connector} {arista.v};\n")
            f.write("}")

    def BFS(self, s):
        """
        Crea un nuevo grafo de tipo árbol mediante el algoritmo "breadth first
            search"

        Parametros
        ----------
        s : Nodo
            nodo raíz del árbol que se va a generar

        Returns
        -------
        bfs : Grafo
            árbol generado
        """
        if not s.id in self.V:
            print("Error, node not in V", file=sys.stderr)
            exit(-1)

        bfs = Grafo(id=f"BFS_{self.id}", dirigido=self.dirigido)
        discovered = set()
        bfs.add_nodo(s)
        L0 = [s]
        discovered = set()
        added = [s.id]

        while True:
            L1 = []
            for node in L0:
                aristas = [ids_arista for ids_arista in self.E
                            if node.id in ids_arista]

                for arista in aristas:
                    v = arista[1] if node.id == arista[0] else arista[0]

                    if v in discovered:
                        continue

                    bfs.add_nodo(self.V[v])
                    bfs.add_arista(self.E[arista])
                    discovered.add(v)
                    L1.append(self.V[v])

            L0 = L1
            if not L0:
                break

        return bfs

    def DFS_R(self, u):
        """
        Crea un nuevo grafo de tipo árbol mediante el algoritmo "depth first
            search".
        Usa una función recursiva

        Parametros
        ----------
        u : Nodo
            nodo raíz del árbol que se va a generar

        Returns
        -------
        dfs : Grafo
            árbol generado
        """
        dfs = Grafo(id=f"DFS_R_{self.id}", dirigido=self.dirigido)
        discovered = set()
        self.DFS_rec(u, dfs, discovered)

        return dfs

    def DFS_rec(self, u, dfs, discovered):
        """
        Función recursiva para agregar nodos y aristas al árbol DFS

        Parametros
        ----------
        u : Nodo
            nodo actual, en el que se continúa la búsqueda a lo profundo
        dfs : Grafo
            Grafo que contendrá al árbol de búsquedo a lo produndo.
        discovered : set
            nodos que ya han sido descubiertos

        Returns
        -------
        None
        """
        dfs.add_nodo(u)
        discovered.add(u.id)
        aristas = (arista for arista in self.E if u.id in arista)

        for arista in aristas:
            v = arista[1]
            if not self.dirigido:
                v = arista[0] if u.id == arista[1] else arista[1]
            if v in discovered:
                continue
            dfs.add_arista(self.E[arista])
            self.DFS_rec(self.V[v], dfs, discovered)

    def DFS_I(self, s):
        dfs = Grafo(id=f"DFS_I_{self.id}", dirigido=self.dirigido)
        discovered = {s.id}
        dfs.add_nodo(s)
        u = s.id
        frontera = []
        while True:
            # añadir a frontera todos los nodos con arista a u
            aristas = (arista for arista in self.E if u in arista)
            for arista in aristas:
                v = arista[1] if u == arista[0] else arista[0]
                if v not in discovered:
                    frontera.append((u, v))

            # si la frontera está vacía, salir del loop
            if not frontera:
                break

            # sacar nodo de la frontera
            parent, child = frontera.pop()
            if child not in discovered:
                dfs.add_nodo(self.V[child])
                arista = Arista(self.V[parent], self.V[child])
                dfs.add_arista(arista)
                discovered.add(child)

            u = child

        return dfs
