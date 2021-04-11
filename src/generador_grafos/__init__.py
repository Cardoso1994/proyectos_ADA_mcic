#!/usr/bin/env python3
################################################################################
#
# Desarrollador: Marco Antonio Cardoso Moreno
#
# Generador de grafos mediante diversos métodos de generacion
#
# Abril 2021
#
################################################################################

import sys
import random

from grafo import Grafo
from arista import Arista
from nodo import Nodo

def grafoMalla(m, n, dirigido=False):
    """
    Genera grafo de malla
    :param m: número de columnas (> 1)
    :param n: número de filas (> 1)
    :param dirigido: el grafo es dirigido?
    :return: grafo generado
    """
    if m < 2 or n < 2:
        print("Error. m y n, deben ser mayores que 1", file=sys.stderr)
        exit(-1)

    total_nodes = m*n
    last_col = m - 1
    last_row = n - 1
    g = Grafo(id=f"grafoMalla_{m}_{n}", dirigido=dirigido)
    nodos = g.V

    # agregar nodos
    for id in range(total_nodes):
        g.add_nodo(Nodo(id))

    # agregar aristas
    # primera fila
    g.add_arista(Arista(nodos[0], nodos[1]))
    g.add_arista(Arista(nodos[0], nodos[m]))
    for node in range(1, m - 1):
        g.add_arista(Arista(nodos[node], nodos[node - 1]))
        g.add_arista(Arista(nodos[node], nodos[node + 1]))
        g.add_arista(Arista(nodos[node], nodos[node + m]))
    g.add_arista(Arista(nodos[m-1], nodos[m-2]))
    g.add_arista(Arista(nodos[m-1], nodos[m - 1 + m]))

    # filas [1 : n - 2]
    for node in range(m, total_nodes - m):
        col = node % m
        g.add_arista(Arista(nodos[node], nodos[node - m]))
        g.add_arista(Arista(nodos[node], nodos[node + m]))
        if col == 0:
            g.add_arista(Arista(nodos[node], nodos[node + 1]))
        elif col == last_col:
            g.add_arista(Arista(nodos[node], nodos[node - 1]))
        else:
            g.add_arista(Arista(nodos[node], nodos[node + 1]))
            g.add_arista(Arista(nodos[node], nodos[node - 1]))

    # última fila (n - 1)
    col_0 = total_nodes - m
    col_1 = col_0 + 1
    last_node = total_nodes - 1
    g.add_arista(Arista(nodos[col_0], nodos[col_1]))
    g.add_arista(Arista(nodos[col_0], nodos[col_0 - m]))
    for node in range(col_1, last_node):
        g.add_arista(Arista(nodos[node], nodos[node - 1]))
        g.add_arista(Arista(nodos[node], nodos[node + 1]))
        g.add_arista(Arista(nodos[node], nodos[node - m]))
    g.add_arista(Arista(nodos[last_node], nodos[last_node - m]))
    g.add_arista(Arista(nodos[last_node], nodos[last_node - 1]))

    return g

def grafoErdosRenyi(n, m, dirigido=False, auto=False):
    """
    Genera grafo aleatorio con el modelo Erdos-Renyi
    :param n: número de nodos (> 0)
    :param m: número de aristas (>= n-1)
    :param dirigido: el grafo es dirigido?
    :param auto: permitir auto-ciclos?
    :return: grafo generado
    """
    if m < n-1 or n < 1:
        print("Error: n > 0 y m >= n - 1", file=sys.stderr)
        exit(-1)

    g = Grafo(id=f"grafoErdos_Renyi_{n}_{m}")
    nodos = g.V

    # crear nodos
    for nodo in range(n):
        g.add_nodo(Nodo(nodo))

    # crear aristas
    rand_node = random.randrange
    for arista in range(m):
        while True:
            u = rand_node(n)
            v = rand_node(n)
            if u == v and not auto:
                continue
            if g.add_arista(Arista(nodos[u], nodos[v])):
                break

    return g

def grafoGilbert(n, p, dirigido=False, auto=False):
    """
    Genera grafo aleatorio con el modelo Gilbert
    :param n: número de nodos (> 0)
    :param p: probabilidad de crear una arista (0, 1)
    :param dirigido: el grafo es dirigido?
    :param auto: permitir auto-ciclos?
    :return: grafo generado
    """
    if p > 1 or p < 0 or n < 1:
        print("Error: 0 <= p <= 1 y n > 0", file=sys.stderr)
        exit(-1)

    g = Grafo(id=f"grafoGilbert_{n}_{int(p * 100)}", dirigido=dirigido)
    nodos = g.V

    # crear nodos
    for nodo in range(n):
        g.add_nodo(Nodo(nodo))


    # crear pares de nodos, diferente generador dependiendo del parámetro auto
    if auto:
        pairs = ((u, v) for u in nodos.keys() for v in nodos.keys())
    else:
        pairs = ((u, v) for u in nodos.keys() for v in nodos.keys() if u != v)

    # crear aristas
    for u, v in pairs:
        add_prob = random.random()
        if add_prob <= p:
            g.add_arista(Arista(nodos[u], nodos[v]))

    return g

def grafoGeografico(n, r, dirigido=False, auto=False):
    """
    Genera grafo aleatorio con el modelo geográfico simple
    Se situan todos los nodos con coordenadas dentro de un rectangulo unitario
    Se crean aristas de un nodo a todos los que estén a una distancia <= r de
        un nodo en particular
    :param n: número de nodos (> 0)
    :param r: distancia máxima para crear un nodo (0, 1)
    :param dirigido: el grafo es dirigido?
    :param auto: permitir auto-ciclos?
    :return: grafo generado
    """
    if r > 1 or r < 0 or n < 1:
        print("Error: 0 <= r <= 1 y n > 0", file=sys.stderr)
        exit(-1)

    coords = dict()
    g = Grafo(id=f"grafoGeografico_{n}_{int(r * 100)}", dirigido=dirigido)
    nodos = g.V

    # crear nodos
    for nodo in range(n):
        g.add_nodo(Nodo(nodo))
        x = round(random.random(), 3)
        y = round(random.random(), 3)
        coords[nodo] = (x, y)

    # crear aristas
    r **= 2
    for u in nodos:
        vs = (v for v in nodos if u != v)
        # si auto es true, se agrega la arista del nodo u a sí mismo
        if auto:
            g.add_arista(Arista(nodos[u], nodos[u]))
        # se agregan todos los nodos dentro de la distancia r
        for v in vs:
            dist = (coords[u][0] - coords[v][0]) ** 2 \
                    + (coords[u][1] - coords[v][1]) ** 2
            if dist <= r:
                g.add_arista(Arista(nodos[u], nodos[v]))

    return g

def grafoBarabasiAlbert(n, d, dirigido=False, auto=False):
    """
    Genera grafo aleatorio con el modelo Barabasi-Albert
    :param n: número de nodos (> 0)
    :param d: grado máximo esperado por cada nodo (> 1)
    :param dirigido: el grafo es dirigido?
    :param auto: permitir auto-ciclos?
    :return: grafo generado
    """
    if n < 1 or d < 2:
        print("Error: n > 0 y d > 1", file=sys.stderr)
        exit(-1)

    g = Grafo(id=f"grafoBarabasi_{n}_{d}", dirigido=dirigido)
    nodos = g.V
    nodos_deg = dict()

    # crear nodos
    for nodo in range(n):
        g.add_nodo(Nodo(nodo))
        nodos_deg[nodo] = 0

    # agregar aristas al azar, con cierta probabilidad
    for nodo in nodos:
        for v in nodos:
            p = random.random()
            equal_nodes = v == nodo
            if equal_nodes and not auto:
                continue

            if nodos_deg[nodo] < d and nodos_deg[v] < d \
               and p <= 1 - nodos_deg[v] / d \
               and g.add_arista(Arista(nodos[nodo], nodos[v])):
                nodos_deg[nodo] += 1
                if not equal_nodes:
                        nodos_deg[v] += 1

    return g

def grafoDorogovtsevMendes(n, dirigido=False):
    """
    Genera grafo aleatorio con el modelo Barabasi-Albert
    :param n: número de nodos (≥ 3)
    :param dirigido: el grafo es dirigido?
    :return: grafo generado
    Crear 3 nodos y 3 aristas formando un triángulo. Después, para cada nodo
    adicional, se selecciona una arista al azar y se crean aristas entre el nodo
    nuevo y los extremos de la arista seleccionada.

    """
    if n < 3:
        print("Error: n >= 3", file=sys.stderr)
        exit(-1)

    g = Grafo(id=f"grafoDorogovtsev_{n}", dirigido=dirigido)
    nodos = g.V
    aristas = g.E

    # crear primeros tres nodos y sus correspondientes aristas
    for nodo in range(3):
        g.add_nodo(Nodo(nodo))
    pairs = ((u, v) for u in nodos for v in nodos if u != v)
    for u, v in pairs:
        g.add_arista(Arista(nodos[u], nodos[v]))

    # crear resto de nodos
    for nodo in range(3, n):
        g.add_nodo(Nodo(nodo))
        u, v = random.choice(list(aristas.keys()))
        g.add_arista(Arista(nodos[nodo], nodos[u]))
        g.add_arista(Arista(nodos[nodo], nodos[v]))

    return g
