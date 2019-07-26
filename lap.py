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
    # definindo mascara laplaciana com centro -4
    lap_4_ = np.array([[ 0.,  1., 0.],
                   [ 1., -4., 1.],
                   [ 0.,  1., 0.]], dtype=float) 
    
    image1 = img_as_float(data.imread(argv[0]))
    channels = 'gray'
    
    # verificando numero de canais
    if len(image1.shape) == 3:
        channels = None
        lap_4_ = lap_4_[:,:,None]
        
    # aplicando convolução
    final = filters.convolve(image1, lap_4_)
    
    # correção de intensidades
    final_corr = final + image1
   
    # salvando imagem
    plt.imsave(argv[1], final, cmap=channels)
    
    # plotando resultados
    plt.figure().suptitle("Aguçamento laplaciano")
    plt.subplot(1,2,2) 
    plt.imshow(final_corr, cmap=channels)
    plt.title('Depois')
    plt.axis('off')

    plt.subplot(1,2,1) 
    plt.imshow(final, cmap=channels)
    plt.title('Antes')
    plt.axis('off')
    plt.show()
    
    
   
if __name__ == "__main__":
    main(sys.argv[1:])
    