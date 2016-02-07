
import pyglet


# Sound
try:
    vroum = pyglet.media.StaticSource(pyglet.media.load('sounds/vroum.wav'))
except:
    vroum = None

try:
    mortFeminin = pyglet.media.StaticSource(pyglet.media.load('sounds/mortFeminin.wav'))
except:
    mortFeminin = None
    
try:
    mortMasculin = pyglet.media.StaticSource(pyglet.media.load('sounds/mortMasculin.wav'))
except:
    mortMasculin = None

try:
    crash = pyglet.media.StaticSource(pyglet.media.load('sounds/crash.wav'))
except:
    crash = None

try:
    portiere = pyglet.media.StaticSource(pyglet.media.load('sounds/portiere.wav'))
except:
    portiere = None



# Music
try:
    zik = pyglet.media.StaticSource(pyglet.media.load('music/music.wav'))
except:
    print "Le fichier music.wav est manquant"
    zik = None
