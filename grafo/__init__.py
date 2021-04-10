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
