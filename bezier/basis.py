import numpy as np
import matplotlib.pyplot as plt
import imageio.v2 as im

def main():
    '''Shows the weighting of the Bernstein basis polynomials of degree 3 as an animated graph'''
    plt.xlim([0,1])
    plt.ylim([0,1])
    plt.xlabel('t')
    plt.ylabel('term value')
    plt.title('Bernstein basis polynomials of cubic Bézier curve')
    for i in np.arange(0,51,1):
        t = np.arange(0,i*0.02,0.001)
        term0 = (1-t)**3
        term1 = 3*((1-t)**2)*t
        term2 = 3*(1-t)*(t**2)
        term3 = t**3
        plt.plot(t,term0,color='red',label=r'$b_{0,3}(t) = (1-t)^3$')
        plt.plot(t,term1,color='green',label=r'$b_{1,3}(t) = 3(1-t)^2t$')
        plt.plot(t,term2,color='blue',label=r'$b_{2,3}(t) = 3(1-t)t^2$')
        plt.plot(t,term3,color='black',label=r'$b_{3,3}(t) = t^3$')
        plt.legend([r'$b_{0,3}(t) = (1-t)^3$',r'$b_{1,3}(t) = 3(1-t)^2t$',r'$b_{2,3}(t) = 3(1-t)t^2$',r'$b_{3,3}(t) = t^3$'],loc='upper center')
        plt.savefig(f'basis/{i}.jpg')
    # plt.show()
    for i in np.arange(50,71,1):
        plt.savefig(f'basis/{i}.jpg')
    toStack = [im.imread(f'basis/{i}.jpg') for i in np.arange(0,71,1)]
    for i in np.arange(50,-1,-1):
        toStack.append(im.imread(f'basis/{i}.jpg'))
    frames = np.stack(toStack,axis=0)
    im.mimsave('basis.gif',frames,fps=10)

main()