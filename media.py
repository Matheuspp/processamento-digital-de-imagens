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
    image1 = img_as_float(data.imread("data/" + argv[0]))
    channels = 'gray'
    
    mascara = np.ones([int(argv[2]), int(argv[2])], dtype='float')
    mascara_final = np.divide(mascara, int(argv[2]) ** 2)
    
    if len(image1.shape) == 3:
        mascara_final = mascara_final[:,:,None]
        channels = None
        
    final = filters.convolve(image1, mascara_final, mode='constant', cval=0)
    
    plt.imsave(argv[1], final, cmap=channels)
    
    plt.figure().suptitle("filtro da média")
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
    