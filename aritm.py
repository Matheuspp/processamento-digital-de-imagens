#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 14:10:47 2019

@author: matthew
"""

# importanndo bibliotecas
import numpy as np
import matplotlib.pyplot as plt
from skimage import data
from skimage import io
import sys

def main(argv):
    # imagem 1
    image1 = data.imread("data/" + argv[0])
    # imagem 2
    image2 = data.imread("data/" + argv[1])
    
    #operação de soma
    result = np.add(image1, image2)
    
    maior = np.max(result)
    menor = np.min(result)
    
    aux =  np.subtract(result ,menor) # normalização
    final = (255/(maior - menor))*aux # normalização
    
    # salvando imagens
    plt.imsave(argv[2], final, cmap='gray')
    
    # plotando resultados
    plt.figure()
    plt.subplot(1,2,2) 
    plt.imshow(final, cmap='gray')
    .
    plt.subplot(1,2,1) 
    plt.imshow(image1, cmap='gray')
    plt.show()
    
    
   
if __name__ == "__main__":
    main(sys.argv[1:])