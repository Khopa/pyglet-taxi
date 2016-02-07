#! /usr/bin/python
# -*- coding: cp1252 -*-


# Pyglet Taxi
# Par Clement Perreau aka Khopa

import pyglet
from pyglet.gl import *

from config import *

import math

import camera
import sound_data
import primitives as prims
import app
import sys
import time
from vehicule import *
fsock = open('error.log', 'w')               
sys.stderr = fsock

player = pyglet.media.Player()
player.eos_action = 'loop'

try:
        player.queue(sound_data.zik)
        player.play()
except:
        pass

try:
        config = Config(sample_buffer=1, samples=4, \
          depth_size=16, double_buffer=True)
        window = pyglet.window.Window(resizable=True, config=config)
except:
        window = pyglet.window.Window(resizable=True)

window.set_fullscreen(True)
        

hauteur_camera = 2
temps_debut_partie = time.time()
temps_actuel = time.time()

try:
        best_score_value = int(open('best_score.save', 'r').read())
except:
        best_score_value = 0
        
## MENU ##

playing = False
gameover = False
selection_menu = 0
Enter = False

jouer = pyglet.text.Label('- Jouer',\
                  font_name ='Arial',\
                  font_size=56,\
                  x = 100, y = 500,\
                  anchor_x='left', anchor_y='center')

quitter = pyglet.text.Label('Quitter',\
                  font_name='Arial',\
                  font_size=56,\
                  x = 100, y = 300,\
                  anchor_x='left', anchor_y='center')

best_score = pyglet.text.Label('Meilleur Score : '+ str(best_score_value),\
                  font_name='Arial',\
                  font_size=18,\
                  x = 800, y = 0,\
                  anchor_x='right', anchor_y='bottom')

pause = pyglet.text.Label('Jeu En Pause. Appuyez sur Q pour quitter le jeu.',\
                  font_name='Arial',\
                  font_size=18,\
                  x = 400, y = 300,\
                  anchor_x='center', anchor_y='center')

gameover_score = pyglet.text.Label('Votre Score : ',\
                  font_name='Arial',\
                  font_size=18,\
                  x = 400, y = 300,\
                  anchor_x='center', anchor_y='center')

## LABEL ##

vitesse = pyglet.text.Label('0',\
                  font_name='Arial',\
                  font_size=22,\
                  x = 10, y = 40,\
                  anchor_x='left', anchor_y='center')

score = pyglet.text.Label('Score : 0',\
                  font_name='Arial',\
                  font_size=22,\
                  x = 10, y = 590,\
                  anchor_x='left', anchor_y='center')

distance = pyglet.text.Label('0',\
                  font_name='Arial',\
                  font_size=22,\
                  x = 790, y = 40,\
                  anchor_x='right', anchor_y='center')

temps = pyglet.text.Label('0',\
                  font_name='Arial',\
                  font_size=22,\
                  x = 790, y = 590,\
                  anchor_x='right', anchor_y='center')

##

horloge=0.0

Av=False
Ar=False
Ga=False
Dr=False
Q = False
Mouse_Left_Down = False

game = None
cam = camera.Camera((0,1,0), 0.0, 0.0)
w=640
h=480


def setup():
        global game, camera

        # General
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_TEXTURE_2D)
        glAlphaFunc(GL_GREATER,0.4)
        glEnable(GL_ALPHA_TEST)

        # Brouillard
        if FOG_ACTIVE:
                fogMode = [GL_EXP, GL_EXP2, GL_LINEAR]   #
                glClearColor(0.0,0.0,0.0,0.8)          # ClearColor
                glFogi(GL_FOG_MODE, fogMode[FOGMODE])        # Fog Mode
                glFogf(GL_FOG_DENSITY, FOG_DENSITE)              # Densité
                glHint(GL_FOG_HINT, GL_FASTEST)       # Fog Hint
                glFogf(GL_FOG_START, FOG_DISTANCE_1)             # Fog Start
                glFogf(GL_FOG_END, FOG_DISTANCE_2)
                glEnable(GL_FOG)

        game = app.PygletApp()

@window.event
def on_resize(width, height):
    global game
    global w, h
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glMatrixMode(GL_MODELVIEW)
    w, h = width, height
    return pyglet.event.EVENT_HANDLED

@window.event
def on_draw():
        global game, vitesse, playing, gameover, gameover_score
        global cam, hauteur_camera, w, h

        pointVise = game.vehicule.position
        alpha = camera.deg2rad(game.vehicule.angle)
        ax, ay, az = pointVise
        ay += 1
        ex,ey,ez = ax + math.sin(alpha)*DISTANCE_CAMERA*-1, hauteur_camera, az + math.cos(alpha)*DISTANCE_CAMERA*-1
                

        if playing:
                glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

                actualiser_vitesse()
                actualiser_score()
                actualiser_temps()
                game.draw([ex/TAILLE_BLOC, ez/TAILLE_BLOC])

                # Placement de la camera virtuelle
                
                glLoadIdentity()
                prepare_text()
                vitesse.draw()
                score.draw()
                temps.draw()
                if game.vehicule.transporte_un_client:
                        actualiser_distance()
                        distance.draw()
                if game.pause: pause.draw()
                after_text()
                gluPerspective((game.vehicule.speed*110 + FOCALE_DE_BASE) , w / float(h), .1, 1000.)
                gluLookAt( ex,ey,ez,  ax, ay, az,  0.0,1.0,0.0)
        elif gameover:
                glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
                glLoadIdentity()
                actualiser_menu()
                prepare_text()
                gameover_score.draw()
                best_score.draw()
                after_text()
                gluPerspective((game.vehicule.speed*110 + FOCALE_DE_BASE) , w / float(h), .1, 1000.)
                gluLookAt( ex,ey,ez,  ax, ay, az,  0.0,1.0,0.0)
        else:
                glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
                glLoadIdentity()
                actualiser_menu()
                prepare_text()
                jouer.draw()
                quitter.draw()
                best_score.draw()
                after_text()
                gluPerspective((game.vehicule.speed*110 + FOCALE_DE_BASE) , w / float(h), .1, 1000.)
                gluLookAt( ex,ey,ez,  ax, ay, az,  0.0,1.0,0.0)


@window.event
def on_key_press(symbol,modifiers):

        global Av
        global Ar
        global Ga, Q
        global Dr, game
        global Enter
        
        #print "press"
        game.event_KP(symbol)
        
        if symbol == pyglet.window.key.Q:
                Q = True
        elif symbol == pyglet.window.key.RETURN:
                Enter = True
        elif symbol == pyglet.window.key.A:
                pass
        elif symbol == pyglet.window.key.LEFT : # Fleche gauche 
                Ga=True
        elif symbol == pyglet.window.key.RIGHT : 
                Dr=True
        elif symbol == pyglet.window.key.UP : # Fleche haut
                Av=True
        elif symbol == pyglet.window.key.DOWN : # fleche bas
                Ar=True

@window.event
def on_key_release(symbol,modifiers):

        global Av
        global Ar
        global Ga, Q
        global Dr, game, Enter       
        
        #print "release"
        game.event_KR(symbol)
        
        if symbol == pyglet.window.key.Q:
                Q = False
        elif symbol == pyglet.window.key.LEFT : # Fleche gauche 
                Ga=False
        elif symbol == pyglet.window.key.RIGHT : 
                Dr=False
        elif symbol == pyglet.window.key.UP : # Fleche haut
                Av=False
        elif symbol == pyglet.window.key.DOWN : # fleche bas
                Ar=False
        if symbol == pyglet.window.key.RETURN:
                Enter = False



@window.event
def on_mouse_press(x, y, button, modifiers):
        global Mouse_Left_Down

        if button == pyglet.window.mouse.LEFT:
                Mouse_Left_Down = True
            
@window.event
def on_mouse_release(x, y, button, modifiers):
        global Mouse_Left_Down

        if button == pyglet.window.mouse.LEFT:
                Mouse_Left_Down = False

@window.event
def on_mouse_drag(x,y,dx,dy,boutons,modifiers):
        global game
        game.vehicule.rotater(-dx)

@window.event
def on_mouse_motion(x, y, dx, dy):
        global game
        game.vehicule.rotater(-dx)


def update(dt):
        global horloge, game, Av, Ar, Ga, Dr, Mouse_Left_Down, Enter, selection_menu, playing, Q, gameover

        horloge = horloge + dt

        if playing:
                game.update()

        if Av :
                selection_menu -= 1
                if selection_menu < 0:
                        selection_menu = 1
                Av = False
        if Ar :
                selection_menu += 1
                if selection_menu > 1:
                        selection_menu = 0
                Ar = False
        if Ga :
                pass
        if Dr :
                pass
        if Enter:
                Enter = False
                if gameover:
                        gameover = False
                elif not(playing):
                        if selection_menu == 0:
                                lancer_jeu()
                                game.pause = False
                        else:
                                exit_()
                else:
                        if game.pause:
                                game.pause = False
                        else:
                                game.pause = True
        if Q:
                if playing and game.pause:
                        retour_menu_principal()
                        Q = False
                
                        
                

def prepare_text():
        """ Fonction qui prepare le contexte opengl à l'affichage de texte """
        glMatrixMode(GL_PROJECTION)
        glPushMatrix() # sauvegarde de la matrice de projection 3D
        glLoadIdentity() # chargement de la matrice identite
        gluOrtho2D(0,800,0,600) # Changement de la matrice de projection (Passage en 2D)
        glMatrixMode(GL_MODELVIEW)

def after_text():
        """ Fonction qui signale a opengl que l'on arrete d'afficher du texte """
        glMatrixMode(GL_PROJECTION)
        glPopMatrix() # re chargement de la matrice sauvegardee dans prepare_text()
        glMatrixMode(GL_MODELVIEW)

def actualiser_vitesse():
        """ Actualise le texte du compteur de vitesse """
        global vitesse, game

        txt = str(int(game.vehicule.speed*200.0))
        if len(txt) > 3: txt = txt[:3]
        txt += "Km/H"
        vitesse.text = txt

def actualiser_distance():
        """ Actualise le texte du compteur de vitesse """
        global distance, game

        txt = "Distance : " + str(2*int(math.sqrt((game.vehicule.position[0]-game.vehicule.destination_client[0]*TAILLE_BLOC)**2 +\
                                          (game.vehicule.position[2]-game.vehicule.destination_client[1]*TAILLE_BLOC)**2)))
        txt += " m"
        distance.text = txt

def actualiser_score():

        global score, game

        score.text = "Score : " + str(game.score)

def actualiser_temps():

        global temps, temps_restant, temps_debut_partie

        temps_actuel = time.time()

        ecoule = int(math.fabs(temps_debut_partie - temps_actuel))
        minute = str(TEMPS_PARTIE - 1 - ecoule/60)
        seconde = str(60 - ecoule%60)
        if len(minute) <= 1: minute = "0" + minute
        if len(seconde) <= 1: seconde = "0" + seconde
        temps.text = "Temps restant : " + str(minute) + ":" + str(seconde)

        if ecoule/60 >= TEMPS_PARTIE:
                fin_partie()

def actualiser_menu():

        global jouer, quitter, selection_menu

        if selection_menu == 0:
                jouer.text = "- Jouer"
                quitter.text = "Quitter"
        else:
                jouer.text = "Jouer"
                quitter.text = "- Quitter"

def lancer_jeu():
        global game, playing, temps_debut_partie, temps_actuel
        game.score = 0
        game.pause = False
        playing = True
        temps_debut_partie = time.time()
        temps_actuel = time.time()
        game.vehicule = Vehicule(game, [3*TAILLE_BLOC,0,2*TAILLE_BLOC])

def retour_menu_principal():
        global game, playing, temps_debut_partie, temps_actuel
        playing = False

def fin_partie():
        global game, best_score_value, best_score, gameover_score, gameover, playing

        if game.score > best_score_value:
                best_score_value = game.score
                best_score.text = 'Meilleur Score : '+ str(best_score_value)
                gameover_score.text = 'Nouveau Record : ' + str(best_score_value)
                file = open('best_score.save', 'w')
                file.write(str(best_score_value))
                file.close()
        else:
                gameover_score.text = 'Votre Score : ' + str(game.score)

        playing = False
        gameover = True


def exit_():
        pyglet.app.exit()

        

if __name__ == "__main__":
        
        setup()
        pyglet.clock.schedule_interval(update, 1.0/100.0)
        pyglet.app.run()

