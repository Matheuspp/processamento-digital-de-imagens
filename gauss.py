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
    image1 = img_as_float(data.imread("data/"+ argv[0]))
    channels = 'gray'
    
    # verificando número de canais
    if len(image1.shape) == 3:
        channels = None
    
    # aplicando filtro gaussiano
    final = filters.gaussian_filter(image1, sigma=float(argv[2]))
    
    # salvando imagem
    plt.imsave(argv[1], final, cmap=channels)
    
    # plotagem
    plt.figure().suptitle("filtro gaussiano")
    plt.subplot(1,2,2) 
    plt.imshow(final, cmap=channels)
    plt.title('Depois')
    plt.axis('off')
    # Divide a área de plotagem: 1 linha e 3 colunas.
    plt.subplot(1,2,1) # A área ativa é a 1.
    plt.imshow(image1, cmap=channels)
    plt.title('Antes')
    plt.axis('off')
    plt.show()
   
if __name__ == "__main__":
    main(sys.argv[1:])
    