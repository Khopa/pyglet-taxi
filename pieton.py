import primitives as prims
from pyglet import *
from pyglet.gl import *
from config import *
from camera import deg2rad
import sound_data

import math
import random

class Pieton:


    def __init__(self, game, position = [0,0,0]):

        self.game = game
        self.position = position
        self.angle = 0
        self.direction = 0

        self.animation = 0
        self.animer = False
        self.vivant = True

        self.image = random.randint(0, len(PIETON) -1) 
        self.delai_rotation = DELAI_ROTATION_PIETON

        self.angle_x = 0
        self.saut = 0
        self.a_saute = 0

        self.follow_mode = False
        
    def deplacer(self):

        matrix = self.game.map.getMatrice()

        angle = deg2rad(self.angle)
        ex, ey, ez = self.position
        dx, dy, dz = math.sin(angle), 0, math.cos(angle)
        l = math.sqrt(dx*dx + dy*dy + dz*dz)
        d1x, d1y,d1z = dx/l, dy/l, dz/l
        
        destination = [ex + VITESSE_PIETON*d1x, self.position[1] , ez + VITESSE_PIETON*d1z]

        if matrix != None:

            try:
                x,y,z = destination
                x = int((x)/TAILLE_BLOC)
                y = int((y)/TAILLE_BLOC)
                z = int((z)/TAILLE_BLOC)
                
                if matrix[x][z].texture in [2,3,7,12]:
                    self.position = destination
                    self.position[1] = HAUTEUR_TROTTOIR
                    self.animer = True
                elif matrix[x][z].texture == 4:
                    self.position = destination
                    self.position[1] = 0
                    self.animer = True
                elif self.follow_mode and matrix[x][z].texture in [0,5,6]:
                    self.position = destination
                    self.position[1] = 0
                    self.animer = True
                else:
                    self.animer = False
                    self.position[1] = HAUTEUR_TROTTOIR
                    self.delai_rotation += 5
            except IndexError:
                pass # en dehors de la ville
        else:
            self.position = destination
    
    def rotater(self, value):
        value *= VITESSE_ROTATION
        self.angle += value
        
    def actualiser(self):

        if self.vivant:
            self.deplacer()
            
            self.collision_avec_voiture()

            if self.animer == True:
                if self.animation < len(PIETON[NOM_PIETON[self.image]])-1:
                    self.animation += 1
                else:
                    self.animation = 0
            else:
                self.animation = 0

            if self.delai_rotation >= DELAI_ROTATION_PIETON:
                if random.randint(0,10) == 5:
                    self.rotater(random.randint(0,180))
                    self.delai_rotation = 0
            else:
                self.delai_rotation += 1

        else:
            if self.a_saute != 2:

                if self.a_saute == 0:
                    self.saut += 0.3
                    self.angle_x += 45
                    if self.saut >= self.game.vehicule.speed * 5: self.a_saute = 1
                elif self.a_saute == 1:
                    self.saut -= 0.3
                    self.angle_x += 45
                    if self.saut <= self.position[1]: self.a_saute = 2; self.angle_x = 90 
                    
            

    def collision_avec_voiture(self):

        """ Le pieton verifie si une voiture lui passe dessus"""

        if self.game.vehicule.position[0]<(self.position[0] + TAILLE_VOITURE[0]/2.0)\
            and self.game.vehicule.position[0]>(self.position[0] - TAILLE_VOITURE[0]/2.0)\
            and self.game.vehicule.position[2]<(self.position[2] + TAILLE_VOITURE[0]/2.0)\
            and self.game.vehicule.position[2]>(self.position[2] - TAILLE_VOITURE[0]/2.0)\
            and math.fabs(self.game.vehicule.speed) >= 0.05:
            self.vivant = False
            if self.image == 1:
                sound_data.mortMasculin.play()
            else:
                sound_data.mortFeminin.play()
            self.game.score -= MALUS_PIETON

    def afficher(self):

        angle = ((self.game.vehicule.angle%360)- self.angle%360)%360
            
        if angle < 45 or angle > 315:
            self.direction = 3
        elif 45 < angle < 135:
            self.direction = 1
        elif 135 < angle < 225:
            self.direction = 0
        elif 225 < angle < 315:
            self.direction = 2


        anim = PIETON[NOM_PIETON[self.image]][self.direction][self.animation]
        prims.afficherRectangle(position = [self.position[0], self.position[1]+self.saut, self.position[2]],
                                dimensions = TAILLE_VOITURE,
                                angleY = self.game.vehicule.angle,
                                angleZ = self.angle_x,
                                texture = anim)
        
        
