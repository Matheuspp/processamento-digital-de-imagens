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
import sys

def main(argv):
    # lendo imagem
    image1 = data.imread("data/"+argv[0])
    
    # plotando histograma
    plt.hist((image1).flatten(), density=True, color='purple', bins=25)
    plt.show()
    
    
   
if __name__ == "__main__":
    main(sys.argv[1:])
    #anderson.luizr@ufv.br