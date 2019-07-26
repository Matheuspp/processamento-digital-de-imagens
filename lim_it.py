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
from skimage.color import rgb2gray
import sys

# processo de segmentação interativa

def limiarizacao_simples(image, T_init, min_delta=0.001):
    # a função retornará o valor de T quando a variação de Delta_T for mímima
    
    T = T_init
    Delta_T = np.inf # incicializando delta_T com infinito
    
    while Delta_T >= min_delta:
        g_bw = image > T
        num_px_bg, num_px_fg = np.bincount(g_bw.flatten()) 
        g_fg = image * g_bw
        g_bg = image * np.invert(g_bw)
        fg_mean = g_fg.sum() / float( num_px_fg )
        bg_mean = g_bg.sum() / float( num_px_bg )
        T_old = T        
        T = 0.5 * (fg_mean + bg_mean)
        Delta_T = np.abs(T - T_old)
    return T
    
    

def main(argv):
    
    # obtendo imagem 
    image1 = img_as_float(rgb2gray(data.imread(argv[0])))
    channels = 'gray'
    
    # verificando número de canais
    if len(image1.shape) == 3:
        channels = None
        
    T_final = limiarizacao_simples(image1, float(argv[2]))
    
    # definindo threshold 
    imagem_seg = image1 > T_final
    
    # plotando os resultados
    plt.imsave(argv[1], imagem_seg, cmap=channels)
    
    plt.figure().suptitle("Limiarização simples")
    plt.subplot(1,2,2) 
    plt.imshow(imagem_seg, cmap=channels)
    plt.title('Depois')
    plt.axis('off')
    
    plt.subplot(1,2,1) 
    plt.imshow(image1, cmap=channels)
    plt.title('Antes')
    plt.axis('off')
    plt.show()
    
if __name__ == "__main__":
    main(sys.argv[1:])
    