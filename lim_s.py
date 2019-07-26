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
from scipy.ndimage import filters as fil
from skimage.color import rgb2gray 
import sys

def main(argv):
    # lendo imagem
    image1 = img_as_float(rgb2gray(data.imread("data/" + argv[0])))
    channels = 'gray'
    
    # verificando número de canais
    if len(image1.shape) == 3:
        channels = None
    
    # mascara da média
    mascara = np.ones([int(argv[2]), int(argv[2])], dtype='float')
    mascara_final = np.divide(mascara, int(argv[2]) ** 2) 
    # processo de suavização
    final = fil.convolve(image1, mascara_final, mode='constant', cval=0)
    
    # aplicando otsu
    otsu = filters.threshold_otsu(image1)
    final_image = final < otsu
    
    # salvando imagem
    plt.imsave(argv[1], final_image, cmap=channels)
    
    # plotagem
    plt.figure().suptitle("Suavização + otsu")
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
    