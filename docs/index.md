# Projet paint sur carte STM32 discovery

Les fichiers du projet sont disponibles à l'adresse :
[https://github.com/GoyKa-mol/STM32_Paint.git](https://github.com/GoyKa-mol/STM32_Paint.git)


Le projet contient deux parties : 

+ Un programme C sur la carte STM32 permettant de dessiner dessus avec plusieurs options (couleur, choix du pinceau, etc). Ce programme est indépendant du second programme. Pour faire référence à cette fonction on parlera de **dessin sur la carte**
+ Un programme python pour sauvgarder le dessin réalisé sur la carte. La carte doit être en train d'éxécuter sont programme et être en liaison avec l'ordinateur pour sauvegarder le dessin. Pour faire référence à cette fonction on parlera d'**application de sauvegarde**

## Prérequis

##### Pour le programme de dessin sur la carte

Pour pouvoir utiliser la partie dessin du projet il faut possêder :

+ Une carte STM32F746G-DISCO.
+ L'extension ENS-Paris-Saclay récente de la carte.
+ STM32CubeIDE pour compiler et transmettre le programme à la carte.

##### Pour le programme de sauvegarde

Pour pouvoir utiliser la partie sauvegarde du projet il faut possêder :

+ Python 3.8 (peut être avec d'anciennes version de python 3 mais je ne l'ai pas testé).
+ Les modules suivants:
	* tkinter
	* pyserial
	* matplotlib
	* numpy

## Contenu du dépôt
Les dossier du dépot nécessaire au projet sont :

* Le dossier paint pour le programme de dessin contenant le projet ST32CubeIDE.
* Le dossier python pour le programme de sauvegarde contenant le programme python.