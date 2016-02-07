import pyglet

from config import *
from pieton import *



class Client(Pieton):

    def __init__(self, game, position = [0,0,0]):

        Pieton.__init__(self, game, position)

        self.d_fleche = 0
        self.sens_fleche = 0

        self.pris = False

    def actualiser(self):

        if not(self.pris):
            Pieton.actualiser(self)

            # Animation de la fleche au dessus du client
            if self.sens_fleche == 0:
                if self.d_fleche < 0.5:
                    self.d_fleche += 0.1
                else:
                    self.d_fleche -= 0.1
                    self.sens_fleche = 1
            elif self.sens_fleche == 1:
                if self.d_fleche > 0:
                    self.d_fleche -= 0.1
                else:
                    self.d_fleche += 0.1
                    self.sens_fleche = 0

            # Si le taxi est proche et qu'il ne transporte pas de client, le client se dirige vers lui
            if not(self.game.vehicule.transporte_un_client):
                if math.fabs(self.position[0]-self.game.vehicule.position[0] + self.position[2]-self.game.vehicule.position[2]) < 2*TAILLE_BLOC:
                    self.turn([self.game.vehicule.position[0],self.game.vehicule.position[2]])
                    self.follow_mode = True

    def collision_avec_voiture(self):

        """ Le client verifie si le taxi lui passe dessus, il est ecrase si le taxi va vite, sinon le taxi le prend"""

        if self.game.vehicule.position[0]<(self.position[0] + TAILLE_VOITURE[0]/2.0)\
            and self.game.vehicule.position[0]>(self.position[0] - TAILLE_VOITURE[0]/2.0)\
            and self.game.vehicule.position[2]<(self.position[2] + TAILLE_VOITURE[0]/2.0)\
            and self.game.vehicule.position[2]>(self.position[2] - TAILLE_VOITURE[0]/2.0):

            if math.fabs(self.game.vehicule.speed) >= 0.10: # Si on lui passe dessus a grande vitesse
                self.vivant = False
                
                if self.image == 1:
                    sound_data.mortMasculin.play()
                else:
                    sound_data.mortFeminin.play()
                    
                self.game.score -= MALUS_PIETON
            elif not(self.game.vehicule.transporte_un_client):
                self.game.vehicule.transporte_un_client = True
                self.game.vehicule.definir_destination()
                self.game.score += 25
                self.pris = True


    def turn(self, pos):

        """ Tourne le client vers la position pos """
        
        to_x, to_y = pos
        from_x, from_y = self.position[0],self.position[2]

        sx, sy = 1, 1
        from_x += sx/2
        from_y += sy/2

        x_diff = to_x - from_x
        y_diff = -1* (to_y - from_y)

        c = math.sqrt(x_diff**2 + y_diff**2)

        if c == 0:
            self.angle = 0
            return

        if (x_diff > 0 and y_diff > 0) or \
          (x_diff < 0 and y_diff < 0):
            a = math.sqrt(y_diff**2)
        else:
            a = math.sqrt(x_diff**2)

        alpha = math.degrees(math.asin(1.0*a/c))

        if x_diff > 0:
            if y_diff <= 0:
                alpha -= 90
        elif x_diff < 0:
            if y_diff < 0:
                alpha -= 180
            else:
                alpha -= 270
        elif x_diff == 0:
            if y_diff >= 0:
                alpha = 90
            else:
                alpha = -90


        self.angle = alpha + 90
                

    def afficher(self):

        if not(self.pris):
            Pieton.afficher(self)
            if not(self.game.vehicule.transporte_un_client):
                prims.afficherRectangle(position = [self.position[0], self.position[1]+self.saut+TAILLE_VOITURE[1]+self.d_fleche, self.position[2]],
                                        dimensions = TAILLE_VOITURE,
                                        angleY = self.game.vehicule.angle,
                                        angleZ = self.angle_x,
                                        texture = FLECHE)

