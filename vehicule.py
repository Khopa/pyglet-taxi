# -*- coding: cp1252 -*-
from config import *
import primitives as prims
import math
from camera import deg2rad
import sound_data
import random


class Vehicule:


    def __init__(self, game,  position = [0,0,0]):

        self.parent = game
        self.position = position
        self.angle = 0.0
        self.is_walking = True
        self.anim = 0
        self.type_anim = 0
        self.listeTir = []
        self.perso = 0

        self.transporte_un_client = False
        
        self.destination_client = [-1,-1]
        self.pts_destination = 0

        self.pv = 10
        self.dying = False
        self.dead_anim = -1
        self.alive = True

        self.delai_son_crash = 0

        self.speed = 0

    def accelerer(self):

        #sound_data.vroum.play()
        
        self.type_anim = 0

        if self.speed < VITESSE_MAX:
            if self.speed < 0.0:
                self.speed += 0.005
            if self.speed < 0.125: # 25Km/H
                self.speed += 0.005
            elif self.speed < 0.4: # 25-80 Km/H
                self.speed += 0.0015
            elif self.speed < 0.6: # 80-120 Km/H
                self.speed += 0.0005
            elif self.speed < 1.0: # 120-200 Km/H
                self.speed += 0.0004
            else:                               # > 200 Km/H
                self.speed += 0.00005

    def freiner(self):

        if self.speed < 0:
            self.type_anim = 2
        else:
            self.type_anim = 1

        if self.speed > 0:
            self.speed -= 0.018
        elif self.speed > VITESSE_MIN:
            self.speed -= 0.005

    def deccelerer(self):

        self.type_anim = 0
        if self.speed > 0:
            self.speed -= 0.005 * self.speed
        elif self.speed < 0:
            self.speed += 0.005 * -self.speed

        if -0.01 < self.speed < 0.01:
            self.speed = 0

    def deplacer(self, matrix = None):
        if self.alive:

            if self.speed != 0: self.is_walking = True
            angle = deg2rad(self.angle)
            ex, ey, ez = self.position
            dx, dy, dz = math.sin(angle), 0, math.cos(angle)
            l = math.sqrt(dx*dx + dy*dy + dz*dz)
            d1x, d1y,d1z = dx/l, dy/l, dz/l
            
            destination = [ex + self.speed*d1x, 0 , ez + self.speed*d1z]

            if matrix != None:

                try:
                    x,y,z = destination
                    x = int((x)/TAILLE_BLOC) #(round(x,0))
                    y = int((y)/TAILLE_BLOC) #(round(y,0))
                    z = int((z)/TAILLE_BLOC) #(round(z,0))
                    if matrix[x][z].mur:
                        #self.position[1] = HAUTEUR_TROTTOIR
                        self.speed /= 1.5
                        if self.delai_son_crash >= 50 :
                            sound_data.crash.play()
                            self.delai_son_crash = 0
                    else:
                        self.position = destination
                except IndexError:
                    pass # en dehors de la ville
            else:
                self.position = destination

    def definir_destination(self):
        """ Defini la destination d'un client qu'on vient de prendre """

        try:
            self.destination_client = random.choice(self.parent.map.destination_possible)
        except:
            self.destination_client = [0,0]

        self.pts_destination = int((math.fabs(self.position[0]/TAILLE_BLOC-self.destination_client[0]) +\
                                          math.fabs(self.position[1]/TAILLE_BLOC-self.destination_client[1]))*2*TAILLE_BLOC)

        sound_data.portiere.play()
        print self.destination_client, self.pts_destination

    def atteindre_destination(self):

        sound_data.portiere.play()
        self.parent.score += self.pts_destination
        self.destination_client = [-1,-1]
        self.transporte_un_client = False
        self.pts_destination = 0

    def actualiser(self, matrix = None):

        x = int(self.position[0]/TAILLE_BLOC) #(round(x,0))
        z = int(self.position[2]/TAILLE_BLOC) #(round(z,0))
        
        if matrix[x][z].texture in [2,3,7, 12]:
            self.position[1] = HAUTEUR_TROTTOIR

        if self.delai_son_crash < 50:
            self.delai_son_crash += 1

        if self.transporte_un_client:
            self.verifier_arrivee_destination()

    def verifier_arrivee_destination(self):

        if [int(self.position[0]/TAILLE_BLOC),int(self.position[2]/TAILLE_BLOC)] == self.destination_client:
            self.atteindre_destination()
            
        
    def rotater(self, value):
        value *= VITESSE_ROTATION
        self.angle += value


    def draw(self, angle_impose = None):

        if angle_impose != None:
            angle = angle_impose
        else:
            angle = self.angle

        if self.is_walking:
            self.anim += 1
            if self.anim >= len(VOITURE[NOM_VOITURE[self.perso]][self.type_anim]):
                self.anim = 0
        else:
            self.anim = 0

        # Determination sprite

        anim = VOITURE[NOM_VOITURE[self.perso]][self.type_anim][self.anim]
        
        # Affichage

        if self.alive and anim != None:
            prims.afficherRectangle(position = self.position, dimensions = TAILLE_VOITURE, angleY = angle, texture = anim)
            self.is_walking = False

    
