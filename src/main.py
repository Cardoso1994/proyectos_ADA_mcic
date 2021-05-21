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


def main():
    path = "/home/cardoso/garbage/grafos/200/"

    nodos = 200
    nodos_malla = (20, 10)

    m_erdos = 1020
    p_gilbert = 0.15
    r_geografico = 0.3
    d_barabasi = 5

    print("\nMalla")
    g = grafoMalla(*nodos_malla)
    g.to_graphviz(path + g.id + ".gv")
    g.random_weights()
    kruskal = g.KruskalD()
    kruskal.to_graphviz(path + kruskal.id + ".gv")
    kruskalI = g.KruskalI()
    kruskalI.to_graphviz(path + kruskalI.id + ".gv")
    prim = g.Prim()
    prim.to_graphviz(path + prim.id + ".gv")
    print(f"costo kruskal: {kruskal.costo()}")
    print(f"costo kruskalI: {kruskalI.costo()}")
    print(f"costo prim: {prim.costo()}")

    print("\nErdos")
    g = grafoErdosRenyi(nodos, m_erdos)
    g.to_graphviz(path + g.id + ".gv")
    g.random_weights()
    kruskal = g.KruskalD()
    kruskal.to_graphviz(path + kruskal.id + ".gv")
    kruskalI = g.KruskalI()
    kruskalI.to_graphviz(path + kruskalI.id + ".gv")
    prim = g.Prim()
    prim.to_graphviz(path + prim.id + ".gv")
    print(f"costo kruskal: {kruskal.costo()}")
    print(f"costo kruskalI: {kruskalI.costo()}")
    print(f"costo prim: {prim.costo()}")

    print("\nGilbert")
    g = grafoGilbert(nodos, p_gilbert, dirigido=False, auto=False)
    g.to_graphviz(path + g.id + ".gv")
    g.random_weights()
    kruskal = g.KruskalD()
    kruskal.to_graphviz(path + kruskal.id + ".gv")
    kruskalI = g.KruskalI()
    kruskalI.to_graphviz(path + kruskalI.id + ".gv")
    prim = g.Prim()
    prim.to_graphviz(path + prim.id + ".gv")
    print(f"costo kruskal: {kruskal.costo()}")
    print(f"costo kruskalI: {kruskalI.costo()}")
    print(f"costo prim: {prim.costo()}")

    print("\nGeo")
    g = grafoGeografico(nodos, r_geografico)
    g.to_graphviz(path + g.id + ".gv")
    g.random_weights()
    kruskal = g.KruskalD()
    kruskal.to_graphviz(path + kruskal.id + ".gv")
    kruskalI = g.KruskalI()
    kruskalI.to_graphviz(path + kruskalI.id + ".gv")
    prim = g.Prim()
    prim.to_graphviz(path + prim.id + ".gv")
    print(f"costo kruskal: {kruskal.costo()}")
    print(f"costo kruskalI: {kruskalI.costo()}")
    print(f"costo prim: {prim.costo()}")

    print("\nBarabasi")
    g = grafoBarabasiAlbert(nodos, d_barabasi, auto=False)
    g.to_graphviz(path + g.id + ".gv")
    g.random_weights()
    kruskal = g.KruskalD()
    kruskal.to_graphviz(path + kruskal.id + ".gv")
    kruskalI = g.KruskalI()
    kruskalI.to_graphviz(path + kruskalI.id + ".gv")
    prim = g.Prim()
    prim.to_graphviz(path + prim.id + ".gv")
    print(f"costo kruskal: {kruskal.costo()}")
    print(f"costo kruskalI: {kruskalI.costo()}")
    print(f"costo prim: {prim.costo()}")

    print("\nDorog")
    g = grafoDorogovtsevMendes(nodos, dirigido=False)
    g.to_graphviz(path + g.id + ".gv")
    g.random_weights()
    kruskal = g.KruskalD()
    kruskal.to_graphviz(path + kruskal.id + ".gv")
    kruskalI = g.KruskalI()
    kruskalI.to_graphviz(path + kruskalI.id + ".gv")
    prim = g.Prim()
    prim.to_graphviz(path + prim.id + ".gv")
    print(f"costo kruskal: {kruskal.costo()}")
    print(f"costo kruskalI: {kruskalI.costo()}")
    print(f"costo prim: {prim.costo()}")

if __name__ == "__main__":
    main()
