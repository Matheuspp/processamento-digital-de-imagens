#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 14:10:47 2019

@author: matthew
"""

# importanndo bibliotecas
import numpy as np
import matplotlib.pyplot as plt
from skimage import data, exposure
from skimage import io
import sys

def main(argv):
    # lendo imagem
    image1 = data.imread(argv[0])
    channels = 'gray'
    # verificando número de canais
    if len(image1.shape) == 3:
        mascara_final = mascara_final[:,:,None]
        channels = None
    
    # equalização de histograma
    image2 = exposure.equalize_hist(image1)
    
    # salvando imagem
    plt.imsave(argv[1], image2, cmap=channels)
    
    # plotagem
    plt.figure().suptitle("equalização de histograma")
    plt.subplot(1,2,2) 
    plt.hist((image2).flatten(), density=True, color='purple', bins=25)
    plt.title('Depois')
    #plt.axis('off')
    # Divide a área de plotagem: 1 linha e 3 colunas.
    plt.subplot(1,2,1) # A área ativa é a 1.
    plt.hist((image1).flatten(), density=True, color='purple', bins=25)
    plt.title('Antes')
   # plt.axis('off')
    plt.show()
    
    
   
if __name__ == "__main__":
    main(sys.argv[1:])