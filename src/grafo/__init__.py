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

import copy
import random
import sys

import heapdict
import numpy as np

from arista import Arista
from nodo import Nodo

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

    def copy_grafo(self, id=f"copy", dirigido=False):
        """
        Regresa una copia deep del grafo

        Returns
        -------
        other : Grafo
            deep copy de self
        """
        other = Grafo(id, dirigido)
        other.V = copy.deepcopy(self.V)
        other.E = copy.deepcopy(self.E)
        other.attr = copy.deepcopy(self.attr)

        return other

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


    def random_weights(self):
        """
        Asigna un peso random a todas las aristas del nodo
        """
        for arista in self.E.values():
            arista.attrs['weight'] = random.randint(1, 100)

    def costo(self):
        """
        Calcula el costo del grafo. Suma del peso de las aristas

        Returns
        -------
        costo : float
            suma del peso de las aristas del grafo
        """
        _costo = 0
        for edge in self.E.values():
            _costo += edge.attrs['weight']

        return _costo

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
                if "Dijkstra" in self.id:
                    f.write(f"\"{nodo} ({self.V[nodo].attrs['dist']})\";\n")
                else:
                    f.write(f"{nodo};\n")
            for arista in self.E.values():
                if "Dijkstra" in self.id:
                    weight = np.abs(self.V[arista.u.id].attrs['dist']
                                    - self.V[arista.v.id].attrs['dist'])
                    f.write(f"\"{arista.u} ({self.V[arista.u.id].attrs['dist']})\""
                            + f" {edge_connector} "
                            + f"\"{arista.v} ({self.V[arista.v.id].attrs['dist']})\""
                            # + f" [weight={weight}];\n")
                            + f";\n")
                else:
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
        dfs: Grafo
            arbol generado
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
        """
        Crea un nuevo grafo de tipo árbol mediante el algoritmo "depth first
            search".
        Metodo iterativo

        Parametros
        ----------
        s : Nodo
            nodo raíz del árbol que se va a generar

        Returns
        -------
        dfs : Grafo
            árbol generado
        """
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


    def Dijkstra(self, s):
        """
        Crea un nuevo grafo de tipo árbol mediante el algoritmo de Dijkstra,
        que encuentra el grafo del camino más corto entre nodos
        Usa una función recursiva

        Parametros
        ----------
        s : Nodo
            nodo raíz del árbol que se va a generar

        Returns
        -------
        tree : Grafo
            árbol generado
        """
        tree = Grafo(id=f"{self.id}_Dijkstra")
        line = heapdict.heapdict()
        parents = dict()
        in_tree = set()


        """
        asignar valores infinitos a los nodos.
        asignar nodo padre en el arbol a None
        """
        line[s] = 0
        parents[s] = None
        for node in self.V:
            if node == s:
                continue
            line[node] = np.inf
            parents[node] = None

        while line:
            u, u_dist = line.popitem()
            if u_dist == np.inf:
                continue

            self.V[u].attrs['dist'] = u_dist
            tree.add_nodo(self.V[u])
            if parents[u] is not None:
                arista = Arista(self.V[parents[u]], self.V[u])
                tree.add_arista(arista)
            in_tree.add(u)

            # get neighbor nodes
            neigh = []
            for arista in self.E:
                if self.V[u].id in arista:
                    v = arista[0] if self.V[u].id == arista[1] else arista[1]
                    if v not in in_tree:
                        neigh.append(v)

            # actualizar distancias de ser necesario
            for v in neigh:
                arista = (u, v) if (u, v) in self.E else (v, u)
                if line[v] > u_dist + self.E[arista].attrs['weight']:
                    line[v] = u_dist + self.E[arista].attrs['weight']
                    parents[v] = u

        return tree

    def KruskalD(self):
        """
        Crea un nuevo grafo de tipo árbol mediante el algoritmo de Kruskal
        directo, que encuentra el árbol de expansión mínima

        Returns
        -------
        mst : Grafo
            árbol de expansión mínima (mst)
        """

        mst = Grafo(id=f"{self.id}_KruskalD")

        # sort edges by weight
        edges_sorted = list(self.E.values())
        edges_sorted.sort(key = lambda edge: edge.attrs['weight'])

        # connected component
        connected_comp = dict()
        for nodo in self.V:
            connected_comp[nodo] = nodo

        # add edges, iterating by weight
        for edge in edges_sorted:
            u, v = edge.u, edge.v
            if connected_comp[u.id] != connected_comp[v.id]:
                # add nodes and edge to mst
                mst.add_nodo(u)
                mst.add_nodo(v)
                mst.add_arista(edge)

                # change the connected component of v to be the same as u
                for comp in connected_comp:
                    if connected_comp[comp] == connected_comp[v.id]:
                        other_comp = connected_comp[v.id]
                        connected_comp[comp] = connected_comp[u.id]

                        # if we change the connected comp of one node,
                        # change it for the whole connected comp
                        iterator = (key for key in connected_comp \
                                    if connected_comp[key] == other_comp)
                        for item in iterator:
                            connected_comp[item] = connected_comp[u.id]

        return mst


    def KruskalI(self):
        """
        Crea un nuevo grafo de tipo árbol mediante el algoritmo de Kruskal
        inverso, que encuentra el árbol de expansión mínima

        Returns
        -------
        mst : Grafo
            árbol de expansión mínima (mst)
        """
        mst = self.copy_grafo(id=f"{self.id}_KruskalI", dirigido=self.dirigido)

        # sort edges by weight
        edges_sorted = list(self.E.values())
        edges_sorted.sort(key = lambda edge: edge.attrs['weight'], reverse=True)

        # start removing edges from mst
        for edge in edges_sorted:
            u, v = edge.u.id, edge.v.id
            key, value = (u, v), edge
            del(mst.E[(u, v)])
            # if graph not connected after removal, put back the edge again
            if len(mst.BFS(edge.u).V) != len(mst.V):
                mst.E[(u, v)] = edge

        return mst


    def Prim(self):
        """
        Crea un nuevo grafo de tipo árbol mediante el algoritmo de Prim,
        que encuentra el árbol de expansión mínima

        Returns
        -------
        mst : Grafo
            árbol de expansión mínima (mst)
        """
        mst = Grafo(id=f"{self.id}_Prim")
        line = heapdict.heapdict()
        parents = dict()
        in_tree = set()

        s = random.choice(list(self.V.values()))

        """
        asignar valores infinitos a los nodos.
        asignar nodo padre en el arbol a None
        """
        line[s.id] = 0
        parents[s.id] = None
        for node in self.V:
            if node == s.id:
                continue
            line[node] = np.inf
            parents[node] = None

        while line:
            u, u_dist = line.popitem()
            if u_dist == np.inf:
                continue

            self.V[u].attrs['dist'] = u_dist
            mst.add_nodo(self.V[u])
            if parents[u] is not None:
                arista = Arista(self.V[parents[u]], self.V[u])
                if (u, parents[u]) in self.E:
                    weight = self.E[(u, parents[u])].attrs['weight']
                else:
                    weight = self.E[(parents[u], u)].attrs['weight']
                arista.attrs['weight'] = weight
                mst.add_arista(arista)
            in_tree.add(u)

            # get neighbor nodes
            neigh = []
            for arista in self.E:
                if self.V[u].id in arista:
                    v = arista[0] if self.V[u].id == arista[1] else arista[1]
                    if v not in in_tree:
                        neigh.append(v)

            # actualizar distancias de ser necesario
            for v in neigh:
                arista = (u, v) if (u, v) in self.E else (v, u)
                if line[v] > self.E[arista].attrs['weight']:
                    line[v] = self.E[arista].attrs['weight']
                    parents[v] = u

        return mst
