# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 23:37:26 2021

@author: admin
"""

import serial
# ajouter serial avec la commande : pip install pyserial
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
import tkinter as tk
from tkinter import ttk
import serial.tools.list_ports
import time
from PIL import Image, ImageTk
import os


class MyApp:
    def __init__(self, parent):
        self.myParent = parent
        ## - - - - - Création du menu déroulant pour choisir le port COM - - - - - ##
        self.labelChoix = tk.Label(self.myParent, text = 'veuillez choisir le port série')
        self.labelChoix.pack()
        self.listeport = [comports.description for comports in serial.tools.list_ports.comports()]
        self.listeCombo = ttk.Combobox(self.myParent, values = self.listeport, width = max([len(x) for x in self.listeport]))
        self.listeCombo.current(0)
        self.listeCombo.pack()
        self.listeCombo.bind("<<ComboboxSelected>>", self.get_com)

        ## - - - - - Création des widgets - - - - - ##
        self.boutton_ready = tk.Button(self.myParent, text = "pret à recevoir")
        self.boutton_ready.pack()
        self.boutton_ready.bind("<Button-1>", self.ready)
    
        self.image_base = tk.Canvas(self.myParent, width = 425, height = 246)
        self.image_base.create_rectangle(0,0,425,246,fill='white')
        self.image_base.pack()
        
        self.boutton_save = tk.Button(self.myParent, text = "enregistrer", state = "disabled")
        self.boutton_save.pack()
        ## - - - - - Initialisation variables - - - - - ##
        self.img = np.zeros((246, 425,3), dtype = np.uint8)
        self.idx = self.listeCombo.current()
        self.port_com = serial.tools.list_ports.comports()[self.idx].device
    
    def ready(self, event):
        ser = serial.Serial(port = self.port_com, baudrate=115200, bytesize=8, parity='N', stopbits=1)
        reception = True
        while(reception == True):
            self.image_base.create_rectangle(0,0,425,246,fill='white')
            self.image_base.create_text(212,123,text = "Attente de message de départ de la carte", width = 400, font = ('Times', '18', 'bold'))
            self.image_base.update_idletasks()
            if(ser.read(1)==b'd'): #demande de transmission de la carte
                self.image_base.create_rectangle(0,0,425,246,fill='white')
                self.image_base.create_text(212,123,text = " Réception des données en cours", font = ('Times', '18', 'bold'))
                self.image_base.update_idletasks()
                ser.write(bytes('a', encoding='utf8')) #demande de transmission reçu, prêt à recevoir
                for i in range(246):
                    for j in range(425):
                        data_R = int.from_bytes(ser.read(1), byteorder='big')
                        data_V = int.from_bytes(ser.read(1), byteorder='big')
                        data_B = int.from_bytes(ser.read(1), byteorder='big')
                        self.img[i][j] = [data_R, data_V, data_B]
                #temps = datetime.now()
                #str_time = temps.strftime("%d_%m_%Y_%Hh_%Mmin_%Ss")
                # plt.imsave("capture_{}.png".format(str_time), img)
                plt.imsave("./temp/capture_temp.png", self.img)
                reception = False
                self.img_tk = img_tk = tk.PhotoImage(file = "./temp/capture_temp.png")
                os.remove("./temp/capture_temp.png")
                self.image_base.create_image(0,0, anchor = 'nw', image = self.img_tk)
                self.image_base.update_idletasks()
                self.boutton_save.configure(state = 'normal')
                self.boutton_save.bind("<Button-1>", self.save)
                self.boutton_save.update_idletasks()
                ser.close()
    
    def get_com(self, event):
        """ Fonction appelé lorsque l'utilisateur choisit un des port dans le menu déroulant"""
        self.idx = self.listeCombo.current()
        #on récupère le port com sélectionné
        self.port_com = serial.tools.list_ports.comports()[self.idx].device
        
    def save(self, event):
        temps = datetime.now()
        str_time = temps.strftime("%d_%m_%Y_%Hh_%Mmin_%Ss")
        plt.imsave("./saved_image/capture_{}.png".format(str_time), self.img)
        self.boutton_save.configure(state = 'disabled')
        self.boutton_save.unbind("<Button-1>")
        self.boutton_save.update_idletasks()


root = tk.Tk()
root.geometry('450x360')
myApp = MyApp(root)
root.mainloop()
    
    
    
    
    