#!/usr/bin/env python3
################################################################################
#
# Desarrollador: Marco Antonio Cardoso Moreno
#
# Main. Generador de Mallas. Proyecto 01 ADA
#
# Abril 2021
#
################################################################################

from time import perf_counter

from grafo import Grafo
from arista import Arista
from nodo import Nodo
from generador_grafos import grafoMalla, \
                             grafoErdosRenyi, \
                             grafoGilbert, \
                             grafoGeografico, \
                             grafoBarabasiAlbert, \
                             grafoDorogovtsevMendes


def main():
    path = "/home/cardoso/garbage/"
    g = grafoMalla(20, 25)
    g.to_graphviz(path + g.id + ".gv")

    g = grafoErdosRenyi(500, 800)
    g.to_graphviz(path + g.id + ".gv")

    g = grafoGilbert(500, 0.15, dirigido=False, auto=True)
    g.to_graphviz(path + g.id + ".gv")

    g = grafoGeografico(500, 0.1)
    g.to_graphviz(path + g.id + ".gv")

    g = grafoBarabasiAlbert(500, 7, auto=False)
    g.to_graphviz(path + g.id + ".gv")

    g = grafoDorogovtsevMendes(500, dirigido=False)
    g.to_graphviz(path + g.id + ".gv")

if __name__ == "__main__":
    main()
