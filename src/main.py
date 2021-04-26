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
    d_barabasi = 7

    g = grafoMalla(*nodos_malla)
    g.to_graphviz(path + g.id + ".gv")
    bfs = g.BFS(Nodo(0))
    bfs.to_graphviz(path + bfs.id + ".gv")
    dfs = g.DFS_R(Nodo(0))
    dfs.to_graphviz(path + dfs.id + ".gv")
    dfs_i = g.DFS_I(Nodo(0))
    dfs_i.to_graphviz(path + dfs_i.id + ".gv")

    g = grafoErdosRenyi(nodos, m_erdos)
    g.to_graphviz(path + g.id + ".gv")
    bfs = g.BFS(Nodo(0))
    bfs.to_graphviz(path + bfs.id + ".gv")
    dfs = g.DFS_R(Nodo(0))
    dfs.to_graphviz(path + dfs.id + ".gv")
    dfs_i = g.DFS_I(Nodo(0))
    dfs_i.to_graphviz(path + dfs_i.id + ".gv")

    g = grafoGilbert(nodos, p_gilbert, dirigido=False, auto=False)
    g.to_graphviz(path + g.id + ".gv")
    bfs = g.BFS(Nodo(0))
    bfs.to_graphviz(path + bfs.id + ".gv")
    dfs = g.DFS_R(Nodo(0))
    dfs.to_graphviz(path + dfs.id + ".gv")
    dfs_i = g.DFS_I(Nodo(0))
    dfs_i.to_graphviz(path + dfs_i.id + ".gv")

    g = grafoGeografico(nodos, r_geografico)
    g.to_graphviz(path + g.id + ".gv")
    bfs = g.BFS(Nodo(0))
    bfs.to_graphviz(path + bfs.id + ".gv")
    dfs = g.DFS_R(Nodo(0))
    dfs.to_graphviz(path + dfs.id + ".gv")
    dfs_i = g.DFS_I(Nodo(0))
    dfs_i.to_graphviz(path + dfs_i.id + ".gv")

    g = grafoBarabasiAlbert(nodos, d_barabasi, auto=False)
    g.to_graphviz(path + g.id + ".gv")
    bfs = g.BFS(Nodo(0))
    bfs.to_graphviz(path + bfs.id + ".gv")
    dfs = g.DFS_R(Nodo(0))
    dfs.to_graphviz(path + dfs.id + ".gv")
    dfs_i = g.DFS_I(Nodo(0))
    dfs_i.to_graphviz(path + dfs_i.id + ".gv")

    g = grafoDorogovtsevMendes(nodos, dirigido=False)
    g.to_graphviz(path + g.id + ".gv")
    bfs = g.BFS(Nodo(0))
    bfs.to_graphviz(path + bfs.id + ".gv")
    dfs = g.DFS_R(Nodo(0))
    dfs.to_graphviz(path + dfs.id + ".gv")
    dfs_i = g.DFS_I(Nodo(0))
    dfs_i.to_graphviz(path + dfs_i.id + ".gv")

if __name__ == "__main__":
    main()
