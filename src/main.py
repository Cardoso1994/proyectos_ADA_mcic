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

    nodos = 500
    nodos_malla = (25, 20)

    m_erdos = 2550
    p_gilbert = 0.1
    r_geografico = 0.1
    d_barabasi = 7

    g = grafoMalla(*nodos_malla)
    g.to_graphviz(path + g.id + ".gv")

    g = grafoErdosRenyi(nodos, m_erdos)
    g.to_graphviz(path + g.id + ".gv")

    g = grafoGilbert(nodos, p_gilbert, dirigido=False, auto=False)
    g.to_graphviz(path + g.id + ".gv")

    g = grafoGeografico(nodos, r_geografico)
    g.to_graphviz(path + g.id + ".gv")

    g = grafoBarabasiAlbert(nodos, d_barabasi, auto=False)
    g.to_graphviz(path + g.id + ".gv")

    g = grafoDorogovtsevMendes(nodos, dirigido=False)
    g.to_graphviz(path + g.id + ".gv")

if __name__ == "__main__":
    main()
