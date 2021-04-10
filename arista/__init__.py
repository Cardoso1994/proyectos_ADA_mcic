#!/usr/bin/env python3
################################################################################
#
# Desarrollador: Marco Antonio Cardoso Moreno
#
# Clase Arista. Implementación
#
# Abril 2021
#
################################################################################

class Arista(object):
    def __init__(self, u, v, attrs=None):
        self.u = u
        self.v = v
        self.id = (u.id, v.id)
        self.attrs = attrs

    def __eq__(self, other):
        return self.u == other.u and self.v == other.v

    def __repr__(self):
        return repr(self.id)
