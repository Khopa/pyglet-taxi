"""
Config.py


Definition des valeurs des constantes, et chargement des textures

"""





import pyglet
from pyglet.gl import *
import os

def chargerTexture(nom):
    image = pyglet.image.load(nom)
    print "Texture ", nom, " chargee"
        
    texture = image.get_texture()
    
    glBindTexture(GL_TEXTURE_2D,texture.id)
    glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_MIN_FILTER,GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_MAG_FILTER,GL_LINEAR)
    glTexEnvi(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_REPLACE)

    return texture

# Chargement de toutes les textures

name = os.listdir("voiture")
NOM_VOITURE = name
VOITURE = {}
for k in name:
    VOITURE[k] = []
    for i,m in enumerate(os.listdir("voiture/"+str(k))):
        VOITURE[k].append([])
        for p in os.listdir("voiture/"+str(k)+"/"+str(m)):
            VOITURE[k][i].append(chargerTexture("voiture/"+str(k)+"/"+str(m)+"/"+str(p)))

name = os.listdir("pieton")
NOM_PIETON = name
PIETON = {}
for k in name:
    PIETON[k] = []
    for i,m in enumerate(os.listdir("pieton/"+str(k))):
        PIETON[k].append([])
        for p in os.listdir("pieton/"+str(k)+"/"+str(m)):
            PIETON[k][i].append(chargerTexture("pieton/"+str(k)+"/"+str(m)+"/"+str(p)))

TEXTURE_ROUTE = chargerTexture("textures/route.png")
TEXTURE_ROUTE2 = chargerTexture("textures/route2.png")
TEXTURE_ROUTE3 = chargerTexture("textures/route3.png")

TEXTURE_PASSAGE = chargerTexture("textures/passage.png")
TEXTURE_TROTTOIR = chargerTexture("textures/trottoir.png")
TEXTURE_IMMEUBLE = [chargerTexture("textures/immeuble.png"),chargerTexture("textures/immeuble2.png"),chargerTexture("textures/immeuble3.png"),\
                    chargerTexture("textures/immeuble4.png")]

TEXTURE_PAVE = chargerTexture("textures/pave.png")
TEXTURE_HERBE = chargerTexture("textures/herbe.png")

TEXTURE_ARBRE = chargerTexture("textures/arbre.png")
TAILLE_ARBRE = [2,3]

TEXTURE_FEUILLE = chargerTexture("textures/feuille.png")

TEXTURE_FALAISE = chargerTexture("textures/falaise.png")

TEXTURE_MUR_MAISON = chargerTexture("textures/mur_maison.png")

FLECHE =  chargerTexture("textures/fleche.png")
FLECHE2 =  chargerTexture("textures/fleche2.png")
FLECHE3 =  chargerTexture("textures/fleche3.png")



# Chargement de la configuration clavier

LEFT = pyglet.window.key.LEFT
RIGHT = pyglet.window.key.RIGHT
UP = pyglet.window.key.UP
DOWN = pyglet.window.key.DOWN
Z = pyglet.window.key.Z
Q = pyglet.window.key.Q
S = pyglet.window.key.S
D = pyglet.window.key.D
A = pyglet.window.key.A
E = pyglet.window.key.E
U = pyglet.window.key.U
J = pyglet.window.key.J


# Vehicule

VITESSE_MAX = 10
VITESSE_MIN = -0.1
TAILLE_VOITURE = [1,1]

# PIETONS

VITESSE_PIETON = 0.05
MAX_PIETON = 3
DELAI_ROTATION_PIETON = 50

MALUS_PIETON = 50


# Camera

VITESSE_ROTATION = 0.5;
DISTANCE_CAMERA = 4;
HAUTEUR_CAMERA = 18;

# Armes

VITESSE_TIR = 0.5
PORTEE_MAX = 25

# OPEN GL FOG

FOG_ACTIVE = True
FOGMODE = 1
FOG_DENSITE = 0.03
FOG_DISTANCE_1 = 1
FOG_DISTANCE_2 = 15
FOCALE_DE_BASE = 50

DISTANCE_VUE = 10
DISTANCE_GESTION_PIETON = 6

# Config Map

TAILLE_BLOC = 4
HAUTEUR_BLOC = 3
HAUTEUR_TROTTOIR = 0.1
LARGEUR_TROTTOIR = 0.3
HAUTEUR_HAIE = 0.8
HAUTEUR_FALAISE = 4
HAUTEUR_TUNNEL = 2.5
HAUTEUR_MAISON = 1
X_SIZE = 25
Z_SIZE = 25

#

TEMPS_PARTIE = 3 # minutes






                     

