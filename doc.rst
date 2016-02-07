# Crazy Taxi # 

Par C.Perreau

Organisation
~~~~~~~~~~~~

La voiture :
++++++++++++

// vehicule.py //

Le deplacement de la voiture est determin� par deux grandeurs : la vitesse (speed), et l'angle.
On peut tourner avec les touches 'D' et 'Q' (en faisant varier l'angle, cf m�thode 'rotater')
On peut accelerer avec la touche 'Z' (on applique alors une acc�leration sur la vitesse)

*NB :* La gestion de l'acceleration n'est pas tout � fait r�aliste, mais elle reste coh�rente, le taux d'acc�leration varie par palier, cf m�thode 'accelerer'

On peut freiner avec la touche 'S'.
La voiture d�c�l�re lorqu'elle est lanc�e et que l'on n'acc�l�re plus. La d�c�l�ration d�pend de la vitesse actuelle (frottements).

L'effet de vitesse de la voiture depend de la vitesse de la voiture : la focale de la camera varie en fonction. (cf 'gluPerspective' dans le main.py)

*NB :* Il est possible d'obtenir des effets tr�s �trange lorsque la vitesse est trop �lev�e (> 300~400Km/H environ) => inversion de la cam�ra, r�duction de la taille de rendu .. etc

Generation de la Ville
++++++++++++++++++++++

// charger_ville.py // ville.py // display_list.py //

Une ville est une matrice constitu� de blocs.
Un bloc peut �tre une route, un immeuble, un parc ou une place... etc
Chaque Bloc est d�fini par un pixel dans l'image 'ville.bmp', chaque couleur correspond � un type de bloc (voir le dictionnaire couleur dans charger_ville.py)
( Remarque : Pygame est requis pour charger cette image bmp, si pygame n'est pas install�, une ville par d�faut est charg�e.

Seuls les blocs dans un rayon de DISTANCE_VUE autour de la voiture sont affich�s. (Optimisation de type 'Frustum Culling') La ville peut ainsi �tre tr�s grande.
Afin d'acc�l�rer le rendu des blocs de la ville, les diff�rents 'mod�les' sont enregistr�s dans des display list OpenGL d�finies dans display_list.py.
Le brouillard g�n�r� par OpenGl, cr�e un fondu qui permet au joueur de moins se rendre compte du Frustum Culling (meilleure immersion).


Gen�ration et gestion des pi�tons:
++++++++++++++++++++++++++++++++++

// pietons.py //


==> Les blocs (qui appartiennent eux m�me � la ville ) poss�dent des pietons (un nombre est determin� � la g�n�ration du bloc, entre 0 et MAX_PIETON pietons)
	-> les blocs solides ne poss�dent pas de pi�tons
	-> les routes et les passages pi�tons ne possedent pas de pi�tons
	-> les pi�tons se gen�re sur les places et les parcs -> si on reste sur la route on a peu de chance de les percuter, mais il faut rester prudent aux passages pi�tons !

--> les pietons situ� dans les blocs distants de DISTANCE_GESTION_PIETON sont supprim�s
--> les blocs situ�s � DISTANCE_GESTION_PIETON - 1 bloc de distance genere des pietons si il n'en possedent pas deja.
--> les blocs affich�s, g�rent et affichent leur pi�tons 
--> les pietons se d�placent plus ou moins al�atoirement (ils sont impr�visibles !)
--> les pietons ne s'aventurent pas sur les routes, sauf aux passages pietons.

*NB :* Un pi�ton peut tout � fait quitter son bloc parent. Celui ci est juste g�n�rateur, et permet de donner une id�e globale de la position de ses pi�tons.

# Interactions
--------------

--> Si la voiture percute un pi�ton, celui ci est tu�, et le joueur perd des points !

# IA des pi�tons
----------------

Les pi�tons se d�placent constamment, et ont une chance sur 10 de changer de direction tous les 50 tours de boucle d'actualisation du programme. Ils changeront de direction plus rapidement s'ils sont bloqu�s.
Ils peuvent se d�placer sur les places, les parcs et les passages pi�tons uniquement.
Pour plus de d�tails sur leur comportement stupide, consulter la m�thode 'actualiser' de la classe 'Pieton' dans pieton.py



Generation des clients:
+++++++++++++++++++++++

// client.py //

==> Un Client est un Pi�ton
	-> il y a peu de client, il faut les chercher. (quand on n'en transporte pas)
	-> leur destination est un bloc al�atoire de la map de type destination (c'est � dire d�fini par un pixel de couleur (255,163,0,255))
	-> le nombre de points d�pend de la distance de cette destination


	