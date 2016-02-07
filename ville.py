# -*- coding: cp1252 -*-
import pyglet
from pyglet.gl import *

from config import *
import random
from pieton import *
from client import *
import charge_ville
import time

import primitives as prims
import display_list as disp

ville = charge_ville.MATRICE_VILLE

class Ville:

    """
    Classe pour representer la Ville
    (Au moyen d'une matrice de Bloc)
    """

    def __init__(self, game):
        """
        Constructeur
        """
        self.parent = game

        self.destination_possible = []
        self.matrice = []

        for i,ligne in enumerate(ville):
            self.matrice.append([])
            for j,tile in enumerate(ligne):
                
                if tile == 12: # repertorie les destinations possibles
                    self.destination_possible.append([i,j])
                    
                self.matrice[i].append(Bloc(i,j, tile, self))
               

    def draw(self, cam_pos = None):
        """
        Fonction d'affichage
        """

        #temps_affichage = time.time()
        # Optimisation de type Frustum Culling, on n'affiche que ce qui est a 'DISTANCE_VUE' de la camera
        
        range_min_i = int(cam_pos[0]) - DISTANCE_VUE
        if range_min_i < 0 : range_min_i = 0

        range_min_j = int(cam_pos[1]) - DISTANCE_VUE
        if range_min_j < 0 : range_min_j = 0

        range_max_i = int(cam_pos[0]) + DISTANCE_VUE
        if range_max_i > len(self.matrice) + 1 : range_max_i = len(self.matrice) + 1
        
        range_max_j = int(cam_pos[1]) + DISTANCE_VUE
        if range_max_j > len(self.matrice[0]) : range_max_j = len(self.matrice) + 1 

        for i in range(range_min_i, range_max_i):
            for j in range(range_min_j, range_max_j):
                try:
                    self.matrice[i][j].draw(cam_pos)
                except IndexError:
                    pass

        self.gerer_pietons(cam_pos)
        #print float(temps_affichage) - float(time.time())

    def gerer_pietons(self, cam_pos):

        """
        --> I - les pietons situé dans les blocs distants de DISTANCE_GESTION_PIETON sont supprimés
        --> II - les blocs situe à DISTANCE_GESTION_PIETON-1 bloc de distance genere des pietons aléatoirement
        """

        # I
        range_i_max = int(cam_pos[0]) + DISTANCE_GESTION_PIETON
        range_i_min = int(cam_pos[0]) - DISTANCE_GESTION_PIETON
        range_j_max = int(cam_pos[1]) + DISTANCE_GESTION_PIETON
        range_j_min = int(cam_pos[1]) - DISTANCE_GESTION_PIETON

        # Cas ligne i
        for i in range(range_i_min, range_i_max):
            for j in [range_j_max, range_j_min]:
                try:
                    self.matrice[i][j].supprimerPietons()
                except:
                    pass

        # Cas ligne j
        for j in range(range_j_min+1, range_j_max-1):
            for i in [range_i_max, range_i_min]:
                try:
                    self.matrice[i][j].supprimerPietons()
                except:
                    pass

        # II
        range_i_max = int(cam_pos[0]) + DISTANCE_GESTION_PIETON -1
        range_i_min = int(cam_pos[0]) - DISTANCE_GESTION_PIETON +1
        range_j_max = int(cam_pos[1]) + DISTANCE_GESTION_PIETON -1
        range_j_min = int(cam_pos[1]) - DISTANCE_GESTION_PIETON +1
        
        # Cas ligne i
        for i in range(range_i_min, range_i_max):
            for j in [range_j_max, range_j_min]:
                try:
                    self.matrice[i][j].genererPietons()
                except IndexError:
                    pass

                

        # Cas ligne j
        for j in range(range_j_min+1, range_j_max-1):
            for i in [range_i_max, range_i_min]:
                try:
                    self.matrice[i][j].genererPietons()
                except IndexError:
                    pass

        
        
                

    def getMatrice(self):
        """
        Accesseur de la matrice
        """
        return self.matrice

        


class Bloc:

    """
    Un Bloc peut être un morceau de route ou un batiment, en fonction de la valeur text
    Un Bloc est un element de la matrice de Ville
    """

    def __init__(self, i, j, text, ville):
        """
        Constructeur
        """
        self.parent = ville
        self.listePieton = []
        self.pietonGenere = False

        self.i = i
        self.j = j

        hauteur = random.randint(2, 15)
        
        if text == 1:
            self.mur = True
            self.RANDOM_ID = random.choice([disp.ID_IMMEUBLE, disp.ID_IMMEUBLE2, disp.ID_IMMEUBLE3, disp.ID_IMMEUBLE4])
        elif text in [8,9,11]:
            self.mur = True
        else: self.mur = False
            
        self.p0 = (i*TAILLE_BLOC,0,j*TAILLE_BLOC)
        self.p1 = (i*TAILLE_BLOC+TAILLE_BLOC,0,j*TAILLE_BLOC)
        self.p2 = (i*TAILLE_BLOC+TAILLE_BLOC,0,j*TAILLE_BLOC+TAILLE_BLOC)
        self.position_centrale = [self.p0[0]+TAILLE_BLOC/2,0,self.p0[2]+TAILLE_BLOC/2]
        
        self.texture = text
        self.d_fleche = 0
        self.sens_fleche = 0

    def supprimerPietons(self):
        self.listePieton = []
        self.pietonGenere = False
        
    def genererPietons(self):
        if self.texture in [2,3] and not(self.pietonGenere): # dans les parcs et les places
            nb_pieton = random.randint(0, MAX_PIETON)
            for i in range(nb_pieton):
                pos = [(random.randint(self.p0[0], self.p1[0])), 0, random.randint(self.p0[2], self.p2[2])]

                if random.randint(0,10) == 5 and not(self.parent.parent.vehicule.transporte_un_client):
                    self.listePieton.append(Client(self.parent.parent, pos))
                else:
                    self.listePieton.append(Pieton(self.parent.parent, pos))
            self.pietonGenere = True

    def draw(self, cam_pos):
        """
        Fonction d'affichage
        """

        if self.texture == 0: 
            disp.afficher_bloc(disp.ID_DESSIN_ROUTEZ, self.i, self.j) 
        elif self.texture == 1:
            disp.afficher_bloc(disp.ID_PAVE, self.i, self.j)
            # Gestion du cas ou la camera est dans le mur, alors, on l'affiche pas
            if int(self.p0[0]/TAILLE_BLOC) == int(cam_pos[0]) and int(self.p0[2]/TAILLE_BLOC) == int(cam_pos[1]):
                pass
            else:
                disp.afficher_bloc(self.RANDOM_ID, self.i, self.j) 
        elif self.texture == 2:
            disp.afficher_bloc(disp.ID_PAVE, self.i, self.j)
        elif self.texture == 3:
            disp.afficher_bloc(disp.ID_PARC, self.i, self.j)
            # Cette ligne ne peut etre stockee dans la display list, car l'affichage de l'arbre est dynamique (depend de l'angle de la camera)
            prims.afficherRectangle(position = self.position_centrale,\
                                                dimensions = TAILLE_ARBRE, angleY = self.parent.parent.vehicule.angle,
                                                texture = TEXTURE_ARBRE)
        elif self.texture == 4:
            disp.afficher_bloc(disp.ID_PASSAGE, self.i, self.j) 
        elif self.texture == 5:
            disp.afficher_bloc(disp.ID_DESSIN_ROUTEX, self.i, self.j) 
        elif self.texture == 6:
            disp.afficher_bloc(disp.ID_DESSIN_ROUTES, self.i, self.j) 
        elif self.texture == 7:
            disp.afficher_bloc(disp.ID_PARC, self.i, self.j) 
        elif self.texture == 8:
            disp.afficher_bloc(disp.ID_HAIE, self.i, self.j)
        elif self.texture == 9:
            if int(self.p0[0]/TAILLE_BLOC) == int(cam_pos[0]) and int(self.p0[2]/TAILLE_BLOC) == int(cam_pos[1]):
                pass
            else:
                disp.afficher_bloc(disp.ID_FALAISE, self.i, self.j) 
        elif self.texture == 10:
            disp.afficher_bloc(disp.ID_DESSIN_ROUTES, self.i, self.j) 
            disp.afficher_bloc(disp.ID_TUNNEL, self.i, self.j)
        elif self.texture == 11:
            disp.afficher_bloc(disp.ID_MAISON, self.i, self.j)
        elif self.texture == 12:
            disp.afficher_bloc(disp.ID_PAVE, self.i, self.j)

            if self.parent.parent.vehicule.destination_client == [self.i, self.j]:
                prims.afficherRectangle(position = [self.position_centrale[0],self.d_fleche, self.position_centrale[2]],\
                                                dimensions = TAILLE_ARBRE, angleY = self.parent.parent.vehicule.angle,
                                                texture = FLECHE2)
                if self.sens_fleche == 0:
                    self.d_fleche += 0.1
                    if self.d_fleche >= 1: self.sens_fleche = 1
                else:
                    self.d_fleche -= 0.1
                    if self.d_fleche <= 0: self.sens_fleche = 0
                


        for p in self.listePieton:
            p.actualiser()
            p.afficher()
