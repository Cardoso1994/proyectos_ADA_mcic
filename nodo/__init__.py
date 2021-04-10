#!/usr/bin/env python3
###############################################################################
#
# Desarrollador: Marco Antonio Cardoso Moreno
#
# Clase Nodo. Implementación
#
# Abril 2021
#
###############################################################################

class Nodo(object):
    def __init__(self, id):
        self.id = id

    def __eq__(self, other):
        return self.id == other.id

    def __repr__(self):
        return repr(self.id)
