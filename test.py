from __future__ import division, print_function
import sys
sys.path.append('../fiber/python/')
from Smooth_Closed_Surface_Quadrature_RBF_Test import Smooth_Closed_Surface_Quadrature_RBF_Test
from utils import timer

if __name__ == '__main__':
    timer.timer('total')
    Smooth_Closed_Surface_Quadrature_RBF_Test()
    timer.timer('total')

    print('\n\n\n')
    timer.timer('', print_all=True)
