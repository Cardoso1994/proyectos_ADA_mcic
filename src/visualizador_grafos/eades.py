#!/usr/bin/env python3
################################################################################
#
# Desarrollador: Marco Antonio Cardoso Moreno
#
# Visualizador de grafos por el método Spring de Eades (1984)
#
# Abril 2021
#
################################################################################

from math import log
import pygame
import random

from arista import Arista
from grafo import Grafo
from nodo import Nodo

# create the main surface (or window)
WIDTH, HEIGHT = 1500, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

# colors
BG      = (251, 241, 199)
BLUE    = (69, 133, 136)
BLACK   = (40, 40, 40)
RED     = (157, 0, 6)

# configuration
FPS = 4

NODE_RADIUS = 10


def spring(g):
    """
    Muestra una animación del metodo de visualizacion spring de Eades.

    Parametros
    ----------
    g : Grafo
        grafo para el cual se realiza la visualizacion
    """

    run = True
    clock = pygame.time.Clock()

    init_nodes(g)
    draw_edges(g)
    draw_nodes(g)
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        WIN.fill(BG)
        update_nodes(g)
        draw_edges(g)
        draw_nodes(g)
        pygame.display.update()

    pygame.quit()
    return


def init_nodes(g):
    """
    Inicializa los nodos del grafo g en posiciones random

    Parametros
    ----------
    g : Grafo
        grafo para el cual se realiza la visualizacion
    """

    for node in g.V.values():
        x = random.randrange(15, WIDTH - 15)
        y = random.randrange(15, HEIGHT - 15)
        node.attrs['coords'] = (x, y)

    return

def update_nodes(g):
    """
    Aplica la fuerza a los nodos del grafo G para actualizar su poisicion

    Parametros
    ----------
    g : Grafo
        grafo para el cual se realiza la visualizacion
    """

    c1 = 2
    c2 = 1
    c3 = 1
    c4 = 0.1
    d = 5

    for edge in g.E:
        u, v = edge
        u_pos = g.V[u].attrs['coords']
        v_pos = g.V[v].attrs['coords']
        d = ((u_pos[0] - v_pos[0]) ** 2 + (u_pos[1] - v_pos[1]) ** 2) ** 0.5

        force = c1 * log(d / c2)
        g.V[u].attrs['coords'] = (u_pos[0] + force * c4, u_pos[1] + force * c4)
        g.V[v].attrs['coords'] = (v_pos[0] + force * c4, v_pos[1] + force * c4)
    for node in g.V.values():
        x = random.randrange(15, WIDTH - 15)
        y = random.randrange(15, HEIGHT - 15)
        node.attrs['coords'] = (x, y)

    return


def draw_nodes(g):
    """
    Dibuja los nodos del grafo g

    Parametros
    ----------
    g : Grafo
        grafo para el cual se realiza la visualizacion
    """

    for node in g.V.values():
        pygame.draw.circle(WIN, BLUE, node.attrs['coords'], NODE_RADIUS - 3, 0)
        pygame.draw.circle(WIN, RED, node.attrs['coords'], NODE_RADIUS, 3)

    return


def draw_edges(g):
    """
    Dibuja las aristas del grafo g

    Parametros
    ----------
    g : Grafo
        grafo para el cual se realiza la visualizacion
    """

    for edge in g.E:
        u, v = edge
        u_pos = g.V[u].attrs['coords']
        v_pos = g.V[v].attrs['coords']

        pygame.draw.line(WIN, BLACK, u_pos, v_pos, 1)

    return
