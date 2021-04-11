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
    """
    Clase Arista
    Generación y manejo de Aristas para su uso en Grafos

    Parametros
    ----------
    u : Nodo
        Nodo source de la Arista
    v : Nodo
        Nodo target de la Arista
    attrs : dict
        diccionario de atributos de la Arista

    Atributos
    ---------
    u : Nodo
        Nodo source de la Arista
    v : Nodo
        Nodo target de la Arista
    id : tuple
        (u.id, i.id). Tupla de ids de los Nodos de la Arista
    attrs : dict
        diccionario de atributos de la Arista
    """
    def __init__(self, u, v, attrs=None):
        self.u = u
        self.v = v
        self.id = (u.id, v.id)
        self.attrs = attrs

    def __eq__(self, other):
        """
        Comparación de igualdad entre Aristas

        Parametros
        ----------
        other : Arista
            Arista con la que se realiza la comparación

        Returns
        -------
        True o False : bool
            True si las Aristas son iguales, False de otro modo.
        """
        return self.u == other.u and self.v == other.v

    def __repr__(self):
        """
        Asigna representación repr a los Nodos

        Returns
        -------
        str
            representación en str de los Nodos
        """
        return repr(self.id)
