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
    def __init__(self, id='grafo', dirigido=False):
        self.id = id
        self.dirigido = dirigido
        self.V = dict()
        self.E = dict()
        self.attr = dict()


    def __repr__(self):
        return str("id: " + str(self.id) + '\n'
                   + 'nodos: ' + str(self.V.values()) + '\n'
                   + 'aristas: ' + str(self.E.values()))

    def add_nodo(self, nodo):
        """
        agrega objeto nodo al grafo
        """
        self.V[nodo.id] = nodo

    def add_arista(self, arista):
        """
        Agrega arista al grafo si esta no existe de antemano en dicho grafo.
        """
        # u, v = arista.id
        if self.get_arista(arista.id):
            return False

        self.E[arista.id] = arista
        return True

    def get_arista(self, arista_id):
        if self.dirigido:
            return arista_id in self.E
        else:
            u, v = arista_id
            return (u, v) in self.E or (v, u) in self.E
