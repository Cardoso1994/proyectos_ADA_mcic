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

class Grafo(object):
    """
    Clase Grafo.
    Generación y manejo de Grafos

    Parameters
    ----------
    id : str
        id o nombre del grafo
    dirigido : bool
        Numeric error code.

    Attributes
    ----------
    msg : str
        Human readable string describing the exception.
    dirigido : bool
        indica si el grafo es dirigido
    """
    def __init__(self, id='grafo', dirigido=False):
        self.id = id
        self.dirigido = dirigido
        self.V = dict()
        self.E = dict()
        self.attr = dict()


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
        # u, v = arista.id
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
