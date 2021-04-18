# Fonctionnement du projet

## Réception de donnée

La fonction s'occupant de la réception du dessin est la fonction **ready** qui est appelé lors d'un appui sur le bouton *"pret à recevoir"*. Cette fonction boucle en attendant un caractère 'd' de la carte, ce qui correspond à une demande de transmission. 

	if(ser.read(1)==b'd'): #demande de transmission de la carte

Après réception on envoi un message signifiant que l'on est prêt à recevoir :

	ser.write(bytes('a', encoding='utf8')) #demande de transmission reçu, prêt à recevoir

La carte envoi ligne par ligne, de gauche à droite la valeur R puis G puis B des pixels, donc on lit le canal UART et on on rempli le tableau img représentant l'image avec le code suivant : 

	for i in range(246):
		for j in range(425):
			data_R = int.from_bytes(ser.read(1), byteorder='big')
			data_V = int.from_bytes(ser.read(1), byteorder='big')
			data_B = int.from_bytes(ser.read(1), byteorder='big')
			self.img[i][j] = [data_R, data_V, data_B]
			

## Interface graphique
L'interface graphique est faite avec tkinter et contient plusieur widget : 

+ listeCombo qui est le menu déroulant pour choisir le port COM.
+ boutton_ready qui est le bouton pour indiquer que l'on est pret à recevoir (appel **ready**).
+ image_base qui est le canvas ou est afficher le visualisation de l'image et les messages informatifs.
+ boutton_save qui est le bouton enregistrer.
+ myParent qui est la variable réprésentant la fenêtre tkinter

Les différentes méthodes utilisé associé à ces widgets sont :

###### méthodes communes aux widget

+ *widget.pack()* permet d'afficher le widget
+ *widget.bind("action", fonction)* permet d'appeler un *fonction* lorsqu'une *action* associé au widget est réalisé (par exemple un clique sourie).
+ *widget.configure(paramètres...)* permet de configurer les paramêtre du widget, les changment sont enregistré mais ne son pas actualisé sur l'interface graphique.
+ *widget.update_idletasks()* permet d'actualiser sur l'interface graphique le widget.

###### listeCombo 

+ Création du menu déroulant :

		self.listeCombo = ttk.Combobox(self.myParent, values = self.listeport, width = 50, postcommand = self.refresh_com)

	+ values est la liste de chaques éléments à afficher dans le menu 
	+ width est le nombre de caractère de large du menu déroulant
	+ postcommand est une fonction appelé lorsque l'utilisateur déroule le menu. Ici on appel *refresh_com* qui cherche les port com du PC pour bien afficher le port de la carte si on branche la carte après avoir lancé le script python (ou vice-versa).

+ Lecture/écriture de l'élement cliqué avec listeCombo.current(*opt* indice). Sans argument on lit l'indice de l'élément cliqué, si on met un indice en argument on affiche l'élément correspondant à l'indice. 

+ Lors de la sélection d'un élément du menu dérouland on appel la fonction *get_com* qui se charge de changer le port com associé à la liaison série.

###### Les boutons

+ Lors d'un appuie sur boutton_ready on appel la fonction *ready* qui permet la transmission comme expliqué dans [La partie ci-dessus](/STM32_Paint/fonctionsave/#Réception-de-donnée) 
+ Lors d'un appuie sur boutton_save on appel la fonction *save* qui permet d'enregistrer l'image dans le dossier *saved_image* le nom est de la forme "capture_JJ_MM_YYYY_Hh_M_Ss.png" en fonction de la date et de l'heure d'enregistrement.

###### le canvas
+ On utilise les méthode image_base.create_XXXXXX() pour changer le contenue du canvas (texte, rectangle ou image).











