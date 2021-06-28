#!/usr/bin/env python3
###############################################################################
#
# Desarrollador: Marco Antonio Cardoso Moreno
#
# Main. Generador de Grafos y árboles de Dijkstra. Proyecto 03 ADA
#
# Abril 2021
#
###############################################################################

import random
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
from visualizador_grafos.eades import spring
from visualizador_grafos.fruchterman_reginold import fruchterman_reginold


def main():
    path = "/home/cardoso/garbage/grafos/200/"

    nodos = 100
    nodos_malla = (20, 25)

    m_erdos = 3500
    p_gilbert = 0.05
    r_geografico = 0.25
    d_barabasi = 4

    print("\nMalla")
    g = grafoMalla(*nodos_malla)
    fruchterman_reginold(g)
    exit()

    # print("\nErdos")
    # g = grafoErdosRenyi(nodos, m_erdos)
    # spring(g)

    # print("\nGilbert")
    # g = grafoGilbert(nodos, p_gilbert, dirigido=False, auto=False)
    # spring(g)

    print("\nGeo")
    g = grafoGeografico(nodos, r_geografico)
    spring(g)

    # print("\nBarabasi")
    # g = grafoBarabasiAlbert(nodos, d_barabasi, auto=False)
    # spring(g)

    # print("\nDorog")
    # g = grafoDorogovtsevMendes(nodos, dirigido=False)
    # spring(g)

if __name__ == "__main__":
    main()
