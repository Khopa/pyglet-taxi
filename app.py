import camera
import primitives as prims
import config
from ville import *
from vehicule import *
from pieton import *

import random


class PygletApp:

    def __init__(self):

        self.map = Ville(self)
        self.vehicule = Vehicule(self, [3*TAILLE_BLOC,0,2*TAILLE_BLOC])
        #Interrupteurs
        self.Z_pressed = False
        self.Q_pressed = False
        self.S_pressed = False
        self.D_pressed = False
        self.A_pressed = False
        self.E_pressed = False
        self.J_pressed = False
        self.U_pressed = False

        self.score = 0
        self.pause = False

    def update(self):

        if not(self.pause):
            
            if self.Q_pressed:
                self.vehicule.rotater(5)

            if self.D_pressed:
                self.vehicule.rotater(-5)

            if self.Z_pressed:
                self.vehicule.accelerer()
            elif self.S_pressed:
                self.vehicule.freiner()
            else:
                self.vehicule.deccelerer()

            self.vehicule.deplacer(self.map.getMatrice())
            self.vehicule.actualiser(self.map.getMatrice())

        #print self.perso.acceleration


    def event_KP(self, symbol):

        if symbol == Q:
            self.Q_pressed = True
        elif symbol == D:
            self.D_pressed = True
        elif symbol == Z:
            self.Z_pressed = True
        elif symbol == S:
            self.S_pressed = True
        elif symbol == A:
            self.A_pressed = True
        elif symbol == E:
            self.E_pressed = True
        elif symbol == U:
            self.U_pressed = True
        elif symbol == J:
            self.J_pressed = True

    def event_KR(self, symbol):

        if symbol == Q:
            self.Q_pressed = False
        elif symbol == D:
            self.D_pressed = False
        elif symbol == Z:
            self.Z_pressed = False
        elif symbol == S:
            self.S_pressed = False
        elif symbol == A:
            self.A_pressed = False
        elif symbol == E:
            self.E_pressed = False
        elif symbol == U:
            self.U_pressed = False
        elif symbol == J:
            self.J_pressed = False

    def draw(self, cam_pos = None):

        if not(self.pause):
            self.map.draw(cam_pos)
            self.vehicule.draw()

        

    
        
