#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 14:10:47 2019

@author: matthew
"""

# importanndo bibliotecas
import numpy as np
import matplotlib.pyplot as plt
from skimage import data, img_as_float
from scipy.ndimage import filters
import sys

def main(argv):
    # lendo imagem
    image1 = img_as_float(data.imread(argv[0]))
    # filtro do máximo
    final_max = filters.maximum_filter(image1, size=float(argv[3]))
    # filtro do mínimo
    final_min = filters.minimum_filter(image1, size=float(argv[3]))
    
    channels = 'gray'
    
    # verificando número de canais
    if len(image1.shape) == 3:
        channels = None
    
    # salvando imagens
    plt.imsave(argv[1], final_max, cmap=channels)
    plt.imsave(argv[2], final_min, cmap=channels)
    
    # plotagem
    plt.figure().suptitle("filtro máximo e mínimo")
    plt.subplot(1,3,2) 
    plt.imshow(final_max, cmap=channels)
    plt.title('Depois máximo')
    plt.axis('off')
    
    plt.subplot(1,3,3) 
    plt.imshow(final_max, cmap=channels)
    plt.title('Depois minimo')
    plt.axis('off')
    # Divide a área de plotagem: 1 linha e 3 colunas.
    plt.subplot(1,3,1) # A área ativa é a 1.
    plt.imshow(image1, cmap=channels)
    plt.title('Antes')
    plt.axis('off')
    plt.show()
    
    
   
if __name__ == "__main__":
    main(sys.argv[1:])
    