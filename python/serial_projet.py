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

ser = serial.Serial(port = 'COM5', baudrate=115200, bytesize=8, parity='N', stopbits=1)
img = np.zeros((246, 425,3), dtype = np.uint8)
while(1):
    if(ser.read(1)==b'd'): #demande de transmission de la carte
        print("d")
        ser.write(bytes('a', encoding='utf8')) #demande de transmission reçu, prêt à recevoir
        for i in range(246):
            for j in range(425):
                data_R = int(ser.read(1))
                data_V = int(ser.read(1))
                data_B = int(ser.read(1))
                img[i][j] = [data_R, data_V, data_B]
        time = datetime.now()
        str_time = time.strftime("%d_%m_%Y_%Hh_%Mmin_%Ss")
        print(img)
        plt.imsave("capture_{}.jpg".format(str_time), img)
        print('fin')
ser.close()
