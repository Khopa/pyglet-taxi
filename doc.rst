# Crazy Taxi # 

Par C.Perreau

Organisation
~~~~~~~~~~~~

La voiture :
++++++++++++

// vehicule.py //

Le deplacement de la voiture est determiné par deux grandeurs : la vitesse (speed), et l'angle.
On peut tourner avec les touches 'D' et 'Q' (en faisant varier l'angle, cf méthode 'rotater')
On peut accelerer avec la touche 'Z' (on applique alors une accéleration sur la vitesse)

*NB :* La gestion de l'acceleration n'est pas tout à fait réaliste, mais elle reste cohérente, le taux d'accéleration varie par palier, cf méthode 'accelerer'

On peut freiner avec la touche 'S'.
La voiture décélére lorqu'elle est lancée et que l'on n'accèlère plus. La décélération dépend de la vitesse actuelle (frottements).

L'effet de vitesse de la voiture depend de la vitesse de la voiture : la focale de la camera varie en fonction. (cf 'gluPerspective' dans le main.py)

*NB :* Il est possible d'obtenir des effets très étrange lorsque la vitesse est trop élevée (> 300~400Km/H environ) => inversion de la caméra, réduction de la taille de rendu .. etc

Generation de la Ville
++++++++++++++++++++++

// charger_ville.py // ville.py // display_list.py //

Une ville est une matrice constitué de blocs.
Un bloc peut être une route, un immeuble, un parc ou une place... etc
Chaque Bloc est défini par un pixel dans l'image 'ville.bmp', chaque couleur correspond à un type de bloc (voir le dictionnaire couleur dans charger_ville.py)
( Remarque : Pygame est requis pour charger cette image bmp, si pygame n'est pas installé, une ville par défaut est chargée.

Seuls les blocs dans un rayon de DISTANCE_VUE autour de la voiture sont affichés. (Optimisation de type 'Frustum Culling') La ville peut ainsi être très grande.
Afin d'accélérer le rendu des blocs de la ville, les différents 'modèles' sont enregistrés dans des display list OpenGL définies dans display_list.py.
Le brouillard généré par OpenGl, crée un fondu qui permet au joueur de moins se rendre compte du Frustum Culling (meilleure immersion).


Genèration et gestion des piétons:
++++++++++++++++++++++++++++++++++

// pietons.py //


==> Les blocs (qui appartiennent eux même à la ville ) possèdent des pietons (un nombre est determiné à la génération du bloc, entre 0 et MAX_PIETON pietons)
	-> les blocs solides ne possèdent pas de piétons
	-> les routes et les passages piétons ne possedent pas de piétons
	-> les piétons se genère sur les places et les parcs -> si on reste sur la route on a peu de chance de les percuter, mais il faut rester prudent aux passages piétons !

--> les pietons situé dans les blocs distants de DISTANCE_GESTION_PIETON sont supprimés
--> les blocs situés à DISTANCE_GESTION_PIETON - 1 bloc de distance genere des pietons si il n'en possedent pas deja.
--> les blocs affichés, gèrent et affichent leur piétons 
--> les pietons se déplacent plus ou moins aléatoirement (ils sont imprévisibles !)
--> les pietons ne s'aventurent pas sur les routes, sauf aux passages pietons.

*NB :* Un piéton peut tout à fait quitter son bloc parent. Celui ci est juste générateur, et permet de donner une idée globale de la position de ses piétons.

# Interactions
--------------

--> Si la voiture percute un piéton, celui ci est tué, et le joueur perd des points !

# IA des piétons
----------------

Les piétons se déplacent constamment, et ont une chance sur 10 de changer de direction tous les 50 tours de boucle d'actualisation du programme. Ils changeront de direction plus rapidement s'ils sont bloqués.
Ils peuvent se déplacer sur les places, les parcs et les passages piétons uniquement.
Pour plus de détails sur leur comportement stupide, consulter la méthode 'actualiser' de la classe 'Pieton' dans pieton.py



Generation des clients:
+++++++++++++++++++++++

// client.py //

==> Un Client est un Piéton
	-> il y a peu de client, il faut les chercher. (quand on n'en transporte pas)
	-> leur destination est un bloc aléatoire de la map de type destination (c'est à dire défini par un pixel de couleur (255,163,0,255))
	-> le nombre de points dépend de la distance de cette destination


	