import math
from config import *


def deg2rad(d):
    return math.pi*d/180.0


class Camera:


    def __init__(self, positionOeil, directionVisee, hauteurVisee):

        self.positionOeil = positionOeil
        self.directionVisee = directionVisee
        self.hauteurVisee = hauteurVisee

    def deplacementSimple(self, x,y,z):
        ex, ey, ez = self.positionOeil
        self.positionOeil = (ex+x, ey+y, ez+z)

    def rotationCamera(self,angleDegre):
        angleRadian = deg2rad(angleDegre)
        self.directionVisee += angleRadian

    def rotationCameraY(self,angleDegre):
        angleRadian = deg2rad(angleDegre)
        self.hauteurVisee+=angleRadian

    def deplacementCamera(self,deplacement):
        ex, ey, ez = self.positionOeil
        dx, dy, dz = math.cos(self.directionVisee), math.sin(self.hauteurVisee), math.sin(self.directionVisee)
        l = math.sqrt(dx*dx + dy*dy + dz*dz)
        d1x, d1y,d1z = dx/l, dy/l, dz/l
        self.positionOeil = ex + deplacement*d1x, ey + deplacement*d1y, ez + deplacement*d1z

    def getPosition(self):
        return self.positionOeil

    def getPointVise(self):
        ex, ey,ez = self.positionOeil
        dx, dy, dz = math.cos(self.directionVisee), self.hauteurVisee, math.sin(self.directionVisee)
        self.pointVise = ex + dx, ey+dy, ez+dz
        return self.pointVise


    
        
