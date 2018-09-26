import sys
sys.path.append('../RigidMultiblobWall')
from Smooth_Closed_Surface_Quadrature_RBF_Test import Smooth_Closed_Surface_Quadrature_RBF_Test
from utils import timer

if __name__ == '__main__':
    timer('total')
    Smooth_Closed_Surface_Quadrature_RBF_Test()
    timer('total')

    print '\n\n\n'
    timer('', print_all=True)
