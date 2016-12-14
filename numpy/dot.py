# -*- coding: utf-8 -*-
import numpy as np

def main():
    a = np.array([1.,2.,3.])
    b = np.array([4.,5.,6.])
    c = np.dot(a,b)
    print(c)

if __name__=='__main__':
    main()
