#!/usr/bin/env python3
################################################################################
#
# Desarrollador: Marco Antonio Cardoso Moreno
#
# Main. Generador de Grafos y árboles DFS y BFS. Proyecto 02 ADA
#
# Abril 2021
#
################################################################################

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


def main():
    path = "/home/cardoso/garbage/grafos/500/"

    nodos = 500
    nodos_malla = (25, 20)

    m_erdos = 2000
    p_gilbert = 0.2
    r_geografico = 0.2
    d_barabasi = 5

    print("\nMalla")
    g = grafoMalla(*nodos_malla)
    g.to_graphviz(path + g.id + ".gv")
    g.random_weights()
    dijkstra = g.Dijkstra(0)
    dijkstra.to_graphviz(path + dijkstra.id + ".gv")
    print(f"g_nodes: {len(g.V)}")
    print(f"dijkstra_nodes: {len(dijkstra.V)}")

    print("\nErdos")
    g = grafoErdosRenyi(nodos, m_erdos)
    g.to_graphviz(path + g.id + ".gv")
    g.random_weights()
    dijkstra = g.Dijkstra(5)
    dijkstra.to_graphviz(path + dijkstra.id + ".gv")
    print(f"g_nodes: {len(g.V)}")
    print(f"dijkstra_nodes: {len(dijkstra.V)}")

    print("\nGilbert")
    g = grafoGilbert(nodos, p_gilbert, dirigido=False, auto=False)
    g.to_graphviz(path + g.id + ".gv")
    g.random_weights()
    dijkstra = g.Dijkstra(5)
    dijkstra.to_graphviz(path + dijkstra.id + ".gv")
    print(f"g_nodes: {len(g.V)}")
    print(f"dijkstra_nodes: {len(dijkstra.V)}")

    print("\nGeo")
    g = grafoGeografico(nodos, r_geografico)
    g.to_graphviz(path + g.id + ".gv")
    g.random_weights()
    dijkstra = g.Dijkstra(5)
    dijkstra.to_graphviz(path + dijkstra.id + ".gv")
    print(f"g_nodes: {len(g.V)}")
    print(f"dijkstra_nodes: {len(dijkstra.V)}")

    print("\nBarabasi")
    g = grafoBarabasiAlbert(nodos, d_barabasi, auto=False)
    g.to_graphviz(path + g.id + ".gv")
    g.random_weights()
    dijkstra = g.Dijkstra(5)
    dijkstra.to_graphviz(path + dijkstra.id + ".gv")
    print(f"g_nodes: {len(g.V)}")
    print(f"dijkstra_nodes: {len(dijkstra.V)}")

    print("\nDorog")
    g = grafoDorogovtsevMendes(nodos, dirigido=False)
    g.to_graphviz(path + g.id + ".gv")
    g.random_weights()
    dijkstra = g.Dijkstra(5)
    dijkstra.to_graphviz(path + dijkstra.id + ".gv")
    print(f"g_nodes: {len(g.V)}")
    print(f"dijkstra_nodes: {len(dijkstra.V)}")

if __name__ == "__main__":
    main()
