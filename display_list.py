# -*- coding: cp1252 -*-

import pyglet
from pyglet.gl import *

import primitives as prims
from config import *

# Definition des DISPLAY_LIST 

# NB : - Les Textures ont été chargées dans config.py
#      - Les Primitives ont été définies dans primitives.py
#      - Le but est d'offrir ici une interface d'utilisation haut niveau pour l'affichage des blocs de la matrice.
#      - L'utilisation des DISPLAY_LIST, permet aussi d'optimiser l'affichage.

# 1) DEFINITION DE TOUS LES POINTS UTILISABLES

# Base du bloc
p0 = (0,0,0)
p1 = (TAILLE_BLOC, 0, 0)
p2 = (TAILLE_BLOC, 0, TAILLE_BLOC)
p3 = (0, 0, TAILLE_BLOC)
# Points à hauteur du trottoir
p4 = (0,HAUTEUR_TROTTOIR,0)
p5 = (TAILLE_BLOC, HAUTEUR_TROTTOIR, 0)
p6 = (TAILLE_BLOC, HAUTEUR_TROTTOIR, TAILLE_BLOC)
p7 = (0, HAUTEUR_TROTTOIR, TAILLE_BLOC)
# Points à hauteur de trottoir, decale par rapport à la largeur
p8 = (LARGEUR_TROTTOIR,HAUTEUR_TROTTOIR,LARGEUR_TROTTOIR)
p9 = (TAILLE_BLOC - LARGEUR_TROTTOIR, HAUTEUR_TROTTOIR, LARGEUR_TROTTOIR)
p10 = (TAILLE_BLOC - LARGEUR_TROTTOIR, HAUTEUR_TROTTOIR, TAILLE_BLOC - LARGEUR_TROTTOIR)
p11 = (LARGEUR_TROTTOIR, HAUTEUR_TROTTOIR,+TAILLE_BLOC- LARGEUR_TROTTOIR)
# Points à hauteur de haie
p12 = (0,HAUTEUR_HAIE,0)
p13 = (TAILLE_BLOC, HAUTEUR_HAIE, 0)
p14 = (TAILLE_BLOC, HAUTEUR_HAIE, TAILLE_BLOC)
p15 = (0, HAUTEUR_HAIE, TAILLE_BLOC)
# Points à hauteur de batiments // hauteur 3 // decalage par rapport au trottoir
p16 = (LARGEUR_TROTTOIR,3,LARGEUR_TROTTOIR)
p17 = (TAILLE_BLOC - LARGEUR_TROTTOIR,3, LARGEUR_TROTTOIR)
p18 = (TAILLE_BLOC - LARGEUR_TROTTOIR, 3, TAILLE_BLOC - LARGEUR_TROTTOIR)
p19 = (LARGEUR_TROTTOIR, 3,+TAILLE_BLOC- LARGEUR_TROTTOIR)
# Points à hauteur de batiments // hauteur 4 // decalage par rapport au trottoir
p20 = (LARGEUR_TROTTOIR,4,LARGEUR_TROTTOIR)
p21 = (TAILLE_BLOC - LARGEUR_TROTTOIR, 4, LARGEUR_TROTTOIR)
p22 = (TAILLE_BLOC - LARGEUR_TROTTOIR, 4, TAILLE_BLOC - LARGEUR_TROTTOIR)
p23 = (LARGEUR_TROTTOIR, 4,+TAILLE_BLOC- LARGEUR_TROTTOIR)
# Points à hauteur de batiments // hauteur 6 // decalage par rapport au trottoir
p24 = (LARGEUR_TROTTOIR,6,LARGEUR_TROTTOIR)
p25 = (TAILLE_BLOC - LARGEUR_TROTTOIR, 6, LARGEUR_TROTTOIR)
p26 = (TAILLE_BLOC - LARGEUR_TROTTOIR, 6, TAILLE_BLOC - LARGEUR_TROTTOIR)
p27 = (LARGEUR_TROTTOIR, 6,+TAILLE_BLOC- LARGEUR_TROTTOIR)
# Points à hauteur de batiments // hauteur 8 // decalage par rapport au trottoir
p28 = (LARGEUR_TROTTOIR,8,LARGEUR_TROTTOIR)
p29 = (TAILLE_BLOC - LARGEUR_TROTTOIR, 8, LARGEUR_TROTTOIR)
p30 = (TAILLE_BLOC - LARGEUR_TROTTOIR, 8, TAILLE_BLOC - LARGEUR_TROTTOIR)
p31 = (LARGEUR_TROTTOIR, 8,TAILLE_BLOC- LARGEUR_TROTTOIR)
# Points à hauteur de falaise
p32 = (0,HAUTEUR_FALAISE,0)
p33 = (TAILLE_BLOC, HAUTEUR_FALAISE, 0)
p34 = (TAILLE_BLOC, HAUTEUR_FALAISE, TAILLE_BLOC)
p35 = (0, HAUTEUR_FALAISE,TAILLE_BLOC)
# Points à hauteur de hauteur tunnel
p36 = (0,HAUTEUR_TUNNEL,0)
p37 = (TAILLE_BLOC, HAUTEUR_TUNNEL, 0)
p38 = (TAILLE_BLOC, HAUTEUR_TUNNEL, TAILLE_BLOC)
p39 = (0, HAUTEUR_TUNNEL,TAILLE_BLOC)
# Points à hauteur de hauteur maison
p40 = (0,HAUTEUR_MAISON,0)
p41 = (TAILLE_BLOC, HAUTEUR_MAISON, 0)
p42 = (TAILLE_BLOC, HAUTEUR_MAISON, TAILLE_BLOC)
p43 = (0, HAUTEUR_MAISON,TAILLE_BLOC)
# Points à hauteur de hauteur maison avec un decalage
p44 = (-LARGEUR_TROTTOIR,HAUTEUR_MAISON,-LARGEUR_TROTTOIR)
p45 = (TAILLE_BLOC + LARGEUR_TROTTOIR, HAUTEUR_MAISON, -LARGEUR_TROTTOIR)
p46 = (TAILLE_BLOC + LARGEUR_TROTTOIR, HAUTEUR_MAISON, TAILLE_BLOC + LARGEUR_TROTTOIR)
p47 = (-LARGEUR_TROTTOIR, HAUTEUR_MAISON,TAILLE_BLOC + LARGEUR_TROTTOIR)
# point haut maison
p48 = (TAILLE_BLOC/2,HAUTEUR_MAISON+1,TAILLE_BLOC/2)


# 2) DEFINITION DES DISPLAY_LIST des Blocs

# Le bloc 1 : Route Axee Z (par rapport aux textures de marquage au sol)
ID_DESSIN_ROUTEZ = glGenLists(1)

glNewList(ID_DESSIN_ROUTEZ, GL_COMPILE)
prims.dessinerRectangle(p0, p1, p2, p3, textureRepeat = True, texture = TEXTURE_ROUTE)
glEndList()


# Le bloc 2 : Route Axee X
ID_DESSIN_ROUTEX = glGenLists(2)

glNewList(ID_DESSIN_ROUTEX, GL_COMPILE)
prims.dessinerRectangle(p0, p1, p2, p3, textureRepeat = True, texture = TEXTURE_ROUTE2)
glEndList()

# Le bloc 3 : Route sans marquage
ID_DESSIN_ROUTES = glGenLists(3)

glNewList(ID_DESSIN_ROUTES, GL_COMPILE)
prims.dessinerRectangle(p0, p1, p2, p3, textureRepeat = True, texture = TEXTURE_ROUTE3)
glEndList()

# Le bloc 4 : Zone Pavee // Genere des pietons
ID_PAVE = glGenLists(4)

glNewList(ID_PAVE, GL_COMPILE)
prims.dessinerRectangle(p0, p1, p5, p4, texture = TEXTURE_TROTTOIR)
prims.dessinerRectangle(p1, p2, p6, p5, texture = TEXTURE_TROTTOIR)
prims.dessinerRectangle(p2, p3, p7, p6, texture = TEXTURE_TROTTOIR)
prims.dessinerRectangle(p3, p0, p4, p7, texture = TEXTURE_TROTTOIR)
prims.dessinerRectangle(p4, p5, p6, p7, texture = TEXTURE_PAVE)
glEndList()

# Le bloc 5 : Petit Parc // Genere des pietons
ID_PARC = glGenLists(5)

glNewList(ID_PARC, GL_COMPILE)
prims.dessinerRectangle(p0, p1, p5, p4, texture = TEXTURE_TROTTOIR)
prims.dessinerRectangle(p1, p2, p6, p5, texture = TEXTURE_TROTTOIR)
prims.dessinerRectangle(p2, p3, p7, p6, texture = TEXTURE_TROTTOIR)
prims.dessinerRectangle(p3, p0, p4, p7, texture = TEXTURE_TROTTOIR)
prims.dessinerRectangle(p4, p5, p6, p7, texture = TEXTURE_HERBE)
glEndList()

# Le bloc 6 : Herbe
ID_HERBE = glGenLists(6)

glNewList(ID_HERBE, GL_COMPILE)
prims.dessinerRectangle(p0, p1, p2, p3, textureRepeat = True, texture = TEXTURE_HERBE)
glEndList()

# Le bloc 7 : Haie
ID_HAIE = glGenLists(7)

glNewList(ID_HAIE, GL_COMPILE)
prims.dessinerRectangle(p0, p1, p13, p12, texture = TEXTURE_FEUILLE)
prims.dessinerRectangle(p1, p2, p14, p13, texture = TEXTURE_FEUILLE)
prims.dessinerRectangle(p2, p3, p15, p14, texture = TEXTURE_FEUILLE)
prims.dessinerRectangle(p3, p0, p12, p15, texture = TEXTURE_FEUILLE)
prims.dessinerRectangle(p12, p13, p14, p15, texture = TEXTURE_FEUILLE)
glEndList()

# Le bloc 8 : Passage
ID_PASSAGE = glGenLists(8)

glNewList(ID_PASSAGE, GL_COMPILE)
prims.dessinerRectangle(p0, p1, p2, p3, textureRepeat = True, texture = TEXTURE_PASSAGE)
glEndList()

# Le bloc 9 : Immeuble 1
ID_IMMEUBLE = glGenLists(9)

glNewList(ID_IMMEUBLE, GL_COMPILE)
prims.dessinerRectangle(p8, p9, p17, p16, texture = TEXTURE_IMMEUBLE[1])
prims.dessinerRectangle(p9, p10, p18, p17, texture = TEXTURE_IMMEUBLE[1])
prims.dessinerRectangle(p10, p11, p19, p18, texture = TEXTURE_IMMEUBLE[1])
prims.dessinerRectangle(p11, p8, p16, p19, texture = TEXTURE_IMMEUBLE[1])
glEndList()

# Le bloc 10 : Immeuble 2
ID_IMMEUBLE2 = glGenLists(10)

glNewList(ID_IMMEUBLE2, GL_COMPILE)
prims.dessinerRectangle(p8, p9, p21, p20, texture = TEXTURE_IMMEUBLE[0])
prims.dessinerRectangle(p9, p10, p22, p21, texture = TEXTURE_IMMEUBLE[0])
prims.dessinerRectangle(p10, p11, p23, p22, texture = TEXTURE_IMMEUBLE[0])
prims.dessinerRectangle(p11, p8, p20, p23, texture = TEXTURE_IMMEUBLE[0])
glEndList()

# Le bloc 11 : Immeuble 3
ID_IMMEUBLE3 = glGenLists(11)

glNewList(ID_IMMEUBLE3, GL_COMPILE)
prims.dessinerRectangle(p8, p9, p25, p24, texture = TEXTURE_IMMEUBLE[2])
prims.dessinerRectangle(p9, p10, p26, p25, texture = TEXTURE_IMMEUBLE[2])
prims.dessinerRectangle(p10, p11, p27, p26, texture = TEXTURE_IMMEUBLE[2])
prims.dessinerRectangle(p11, p8, p24, p27, texture = TEXTURE_IMMEUBLE[2])
glEndList()

# Le bloc 12 : Immeuble 4
ID_IMMEUBLE4 = glGenLists(12)

glNewList(ID_IMMEUBLE4, GL_COMPILE)
prims.dessinerRectangle(p8, p9, p29, p28, texture = TEXTURE_IMMEUBLE[0])
prims.dessinerRectangle(p9, p10, p30, p29, texture = TEXTURE_IMMEUBLE[0])
prims.dessinerRectangle(p10, p11, p31, p30, texture = TEXTURE_IMMEUBLE[0])
prims.dessinerRectangle(p11, p8, p28, p31, texture = TEXTURE_IMMEUBLE[0])
glEndList()

# Le bloc 13 : Falaises
ID_FALAISE = glGenLists(13)

glNewList(ID_FALAISE, GL_COMPILE)
prims.dessinerRectangle(p0, p1, p33, p32, texture = TEXTURE_FALAISE)
prims.dessinerRectangle(p1, p2, p34, p33, texture = TEXTURE_FALAISE)
prims.dessinerRectangle(p2, p3, p35, p34, texture = TEXTURE_FALAISE)
prims.dessinerRectangle(p3, p0, p32, p35, texture = TEXTURE_FALAISE)
glEndList()


# Le bloc 14 : Tunnel
ID_TUNNEL = glGenLists(14)

glNewList(ID_TUNNEL, GL_COMPILE)
prims.dessinerRectangle(p36, p37, p38, p39, texture = TEXTURE_FALAISE)
prims.dessinerRectangle(p36, p37, p33, p32, texture = TEXTURE_FALAISE)
prims.dessinerRectangle(p37, p38, p34, p33, texture = TEXTURE_FALAISE)
prims.dessinerRectangle(p38, p39, p35, p34, texture = TEXTURE_FALAISE)
prims.dessinerRectangle(p39, p36, p32, p35, texture = TEXTURE_FALAISE)
glEndList()

# Le bloc 15 : Maison
ID_MAISON = glGenLists(15)

glNewList(ID_MAISON, GL_COMPILE)
prims.dessinerRectangle(p0, p1, p41, p40, texture = TEXTURE_MUR_MAISON)
prims.dessinerRectangle(p1, p2, p42, p41, texture = TEXTURE_MUR_MAISON)
prims.dessinerRectangle(p2, p3, p43, p42, texture = TEXTURE_MUR_MAISON)
prims.dessinerRectangle(p3, p0, p40, p43, texture = TEXTURE_MUR_MAISON)
prims.dessinerTriangle(p44, p45, p48, texture = TEXTURE_MUR_MAISON)
prims.dessinerTriangle(p45, p46, p48, texture = TEXTURE_MUR_MAISON)
prims.dessinerTriangle(p46, p47, p48, texture = TEXTURE_MUR_MAISON)
prims.dessinerTriangle(p47, p44, p48, texture = TEXTURE_MUR_MAISON)
glEndList()

def afficher_bloc(ID, i, j):
    """ Affichage d'un bloc """
    glPushMatrix()
    glTranslatef(i*TAILLE_BLOC,0,j*TAILLE_BLOC)
    glCallList(ID);
    glPopMatrix()


del p0
del p1
del p2
del p3
del p4
del p5
del p6
del p7
del p8
del p9
del p10
del p11
del p12
del p13
del p14
del p15
del p16
del p17
del p18
del p19
del p20
del p21
del p22
del p23
del p24
del p25
del p26
del p27
del p28
del p29
del p30
del p31
del p32
del p33
del p34
del p35
del p36
del p37
del p38
del p39
del p40
del p41
del p42
del p43
del p44
del p45
del p46
del p47
del p48
