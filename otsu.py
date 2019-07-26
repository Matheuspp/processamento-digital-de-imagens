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
from skimage import filters
from skimage.color import rgb2gray 
import sys

def main(argv):
    # lendo imagem
    image1 = img_as_float(rgb2gray(data.imread(argv[0])))
    channels = 'gray'
    
    # verificando número de canais
    if len(image1.shape) == 3:
        channels = None
    
    # aplicando otsu
    otsu = filters.threshold_otsu(image1)
    final_image = image1 < otsu
    
    # salvando imagem
    plt.imsave(argv[1], final_image, cmap=channels)
    
    # plotagem
    plt.figure().suptitle("Otsu")
    plt.subplot(1,2,2) 
    plt.imshow(final_image, cmap=channels)
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
    