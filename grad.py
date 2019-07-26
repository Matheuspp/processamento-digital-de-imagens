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
    
    # mascara horizontal de sobel
    sob_h = np.array([[-1., -2., -1.],
                  [ 0.,  0.,  0.],
                  [ 1.,  2.,  1.]], dtype=float)
    # mascara vertical de sobel
    sob_v = np.array([[-1.,  0.,  1.],
                  [-2.,  0.,  2.],
                  [-1.,  0.,  1.]], dtype=float)
     
    # lendo imagem
    image1 = img_as_float(data.imread(argv[0]))
    channels = 'gray'
    
    # verificando numero de canais
    if len(image1.shape) == 3:
         sob_h = sob_h[:,:,None]
         sob_v = sob_v[:,:,None]
         channels = None
    
    # aplicando convolução
    im_sob_h  = filters.convolve(image1, sob_h)
    im_sob_v  = filters.convolve(image1, sob_v)
    
    # obtendo magnitude do gradiente
    im_sob = np.sqrt(im_sob_h**2 + im_sob_v**2)
    
   
    # salvando imagem
    plt.imsave(argv[1], im_sob, cmap=channels)
    
    
    # plotando resultados
    plt.figure().suptitle("Gradiente Sobel Mask")
    plt.subplot(1,2,2) 
    plt.imshow(im_sob, cmap=channels)
    plt.title('Depois')
    plt.axis('off')
    
    plt.subplot(1,2,1) 
    plt.imshow(image1, cmap=channels)
    plt.title('Antes')
    plt.axis('off')
    plt.show()
    
    
   
if __name__ == "__main__":
    main(sys.argv[1:])
    