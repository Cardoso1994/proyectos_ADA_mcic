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
    """
    Clase Nodo.
    Generación y manejo de Nodos para su uso en Grafos

    Parametros
    ----------
    id : str
        id o nombre del Nodo

    Atributos
    ----------
    id : int
        identificador del Nodo
    """
    def __init__(self, id):
        self.id = id
        self.attrs = dict()

    def __eq__(self, other):
        """
        Comparación de igualdad entre Nodos

        Parametros
        ----------
        other : Nodo
            Nodo con el que se realiza la comparación

        Returns
        -------
        True o False : bool
            True si los Nodos son iguales, False de otro modo.
        """
        return self.id == other.id

    def __lt__(self, other):
        """
        Checks if self.id is less than other.id
        """
        return self.id < other.id

    def __lt__(self, other):
        """
        Checks if self.id is greater than other.id
        """
        return self.id > other.id

    def __repr__(self):
        """
        Asigna representación repr a los Nodos

        Returns
        -------
        str
            representación en str de los Nodos
        """
        return repr(self.id)

    def __hash__(self):
        return hash(self.id)
