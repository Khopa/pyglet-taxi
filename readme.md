Pyglet Taxi (2011) :
====================

<a href="url"><img src="https://raw.github.com/Khopa/pyglet-taxi/master/screenshoot.png"></a>

This is an old project of mine from 2011.
Actually i believe it's my fourth game (or should i say playable prototype ?) if you don't count the load of silly RPG Maker games i made when i was younger, before getting into programming. It's also my first 3D game.

*Disclaimer : I have no rights on the assets (textures, sounds... etc) used in the projects. That's things i randomly took on the internet back then. If you own these assets (and can prove it) and want them removed. Just ask.
However, you can do whatever you want with the python code provided (if you ever find an use for it, which i seriously doubt) as i release it under the Lesser Beer-Ware License.*

The goal of the game is to take customers and bring them to their destination. Well it's a taxi game.

Technologies : 
--------------

- Python 2.7
- Pyglet
- Pygame

Requirements : 
--------------

- Install Python 2.7+ (2.6 should be fine too though)
- Install Pyglet  ```pip install pyglet``` Actually, i think there used to be an apt package for debian, and an msi installer for Windows that worked half the time. So you could try to use them too.
- Install Pygame (optionnal)

Cool features :
---------------

- The city is generated using a .bmp picture that can be easily edited. You can retro-engineer "ville.bmp" "charge-ville.py" and "display-list.py" if you want to change the way it looks. The loading image feature require pygame installed, otherwise a default city is loaded (which is the same as the one provided in "ville.bmp")
- You can run over pedestrians, this is almost **GTA V**

Flaws :
-------

- There is no arrow to indicate the destination of a customer, just a text indicating the distance. So you had to guess the direction using this sole indication, and I use to call it "a gameplay feature". But let's be honest, i was just too lazy to do it back then. :blush:
- The menu is awful
- The code and the comments are in french
- This is not clean code
- There is a surprise for you if you manage to go at more than 300km/h~400km/h in game





