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
from skimage.transform import resize
from skimage.color import rgb2gray 
from scipy.misc import imresize
import sys

def main(argv):
    # lendo imagens
    image1 = rgb2gray(data.imread("data/"+argv[0]))
    image2 = rgb2gray(data.imread("data/"+argv[1]))
    
    
    channels = 'gray'
    # verificando número de canais
    if len(image1.shape) == 3:
        channels = None
    
    # operação lógica
    result = np.bitwise_and(image1, image2)
    # salvando imagem
    plt.imsave(argv[2], result, cmap=channels)
    
    # plotagem
    plt.figure().suptitle("Operações lógicas")
    plt.subplot(1,3,3) 
    plt.imshow(result, cmap=channels)
    plt.title('resultado')
    plt.axis('off')
    # Divide a área de plotagem: 1 linha e 3 colunas.
    plt.subplot(1,3,1) # A área ativa é a 1.
    plt.imshow(image1, cmap=channels)
    plt.title('imagem1')
    plt.axis('off')
    
    plt.subplot(1,3,2) # A área ativa é a 1.
    plt.imshow(image2, cmap=channels)
    plt.title('imagem2')
    plt.axis('off')
    plt.show()
    
    plt.show()
    
    
   
if __name__ == "__main__":
    main(sys.argv[1:])