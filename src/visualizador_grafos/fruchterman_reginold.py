#!/usr/bin/env python3
################################################################################
#
# Desarrollador: Marco Antonio Cardoso Moreno
#
# Visualizador de grafos por el método Spring de Eades (1984)FruchtermanReginold
#
# Abril 2021
#
################################################################################

from math import log, atan2, cos, sin
import pygame
import random

from arista import Arista
from grafo import Grafo
from nodo import Nodo

# create the main surface (or window)
WIDTH, HEIGHT   = 1000, 700
BORDER          = 15
WIN             = pygame.display.set_mode((WIDTH, HEIGHT))

# colors
BG              = (251, 241, 199)
BLUE            = (69, 133, 136)
BLACK           = (40, 40, 40)
RED             = (157, 0, 6)

# colors black mode
BG              = (40, 40, 40)
BLUE            = (131, 165, 152)
BLACK           = (235, 219, 178) # Actually white
RED             = (251, 73, 52)

# configuration
ITERS           = 1500
FPS             = 40
NODE_RADIUS     = 15
DIST_MIN        = (min(WIDTH, HEIGHT)) // 15
NODE_MIN_WIDTH  = 25
NODE_MIN_HEIGHT = 25
NODE_MAX_WIDTH  = WIDTH - 25
NODE_MAX_HEIGHT = HEIGHT - 25

# spring constants
c1 = 1.65
c2 = 0.7
c3 = 4.8
c4 = 0.1

def fruchterman_reginold(g):
    """
    Muestra una animación del metodo de visualizacion de Furchterman y Reginold
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
        x = random.randrange(NODE_MIN_WIDTH, NODE_MAX_WIDTH)
        y = random.randrange(NODE_MIN_HEIGHT, NODE_MAX_HEIGHT)
        node.attrs['coords'] = [x, y]

    return


def update_nodes(g):
    C = 1
    temp = 1
    area = (WIDTH - NODE_MIN_WIDTH) * (HEIGHT - NODE_MIN_HEIGHT)
    k = C * (area / len(g.V)) ** 0.5
    for node in g.V.values():
        fx=0
        fy=0
        for other in g.V.values():
            if node == other:
                continue

            d=((other.attrs['coords'][0] - node.attrs['coords'][0]) ** 2 +
               (other.attrs['coords'][1] - node.attrs['coords'][1])**2) ** 0.5
            if d==0:
                continue

            force= (d / abs(d)) * k**2 / d
            angle = atan2(other.attrs['coords'][1] - node.attrs['coords'][1], other.attrs['coords'][0] - node.attrs['coords'][0])
            fx-= force * cos(angle)
            fy-= force * sin(angle)

            if other.id in node.connected_to:
                #Attraction force - Adjacent nodes
                d = ((other.attrs['coords'][0] - node.attrs['coords'][0]) ** 2
                    + (other.attrs['coords'][1] - other.attrs['coords'][1]) ** 2) ** 0.5

                if d < DIST_MIN: #30
                    continue

                force = d / abs(d) * d**2 / k
                angle = atan2(other.attrs['coords'][1] - node.attrs['coords'][1],
                              other.attrs['coords'][0] - node.attrs['coords'][0])
                fx+= force * cos(angle)
                fy+= force * sin(angle)

        node.attrs['coords'][0] += c4*fx
        node.attrs['coords'][1] += c4*fy

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
