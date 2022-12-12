import numpy as np
from matplotlib import pyplot as plt
from matplotlib import collections as co
import imageio.v2 as im

def quadratic():
    '''Animates de Casteljau's algorithm generating a quadratic Bézier curve'''
    fig,ax = plt.subplots()
    for i in np.arange(0,101,1):
        ax.set_xlim([0,100])
        ax.set_ylim([0,100])
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        fig.suptitle('de Casteljau\'s algorithm: quadratic Bézier curve',fontsize=13)
        t = round(i/100,2)
        x = [10,50,90]
        y = [10,90,10]
        dx01 = x[1]-x[0]
        dy01 = y[1]-y[0]
        xB0 = x[0]+t*dx01
        yB0 = y[0]+t*dy01
        dx12 = x[2]-x[1]
        dy12 = y[2]-y[1]
        xB1 = x[1]+t*dx12
        yB1 = y[1]+t*dy12
        dx = xB1-xB0
        dy = yB1-yB0
        xB = xB0+t*dx
        yB = yB0+t*dy
        x += [xB0,xB1,xB]
        y += [yB0,yB1,yB]
        labels = [r'$P_0$',r'$P_1$',r'$P_2$',r'$B_0$',r'$B_1$',r'$B$']
        lines = [[(x[0],y[0]),(x[1],y[1])],[(x[1],y[1]),(x[2],y[2])],[(xB0,yB0),(xB1,yB1)]]
        lc = co.LineCollection(lines,colors=[(0,0,0),(0,0,0),(0,0,1)],linewidths=2)
        ax.add_collection(lc)
        t_dom = np.arange(0,i*0.01,0.01)
        x_comp = ((1-t_dom)**2)*x[0]+2*(1-t_dom)*t_dom*x[1]+(t_dom**2)*x[2]
        y_comp = ((1-t_dom)**2)*y[0]+2*(1-t_dom)*t_dom*y[1]+(t_dom**2)*y[2]
        plt.plot(x_comp,y_comp,color='red')
        ax.scatter(x,y,c=[(0,0,0),(0,0,0),(0,0,0),(0,0,1),(0,0,1),(1,0,0)])
        for j,label in enumerate(labels):
            ax.annotate(label,(x[j]+1,y[j]+0.5))
        ax.text(44,12,f't = {t}')
        plt.savefig(f'casteljau2/{i}.jpg')
        if i != 100:
            ax.clear()
        else:
            for i in np.arange(101,131,1):
                plt.savefig(f'casteljau2/{i}.jpg')
    # plt.show()
    toStack = [im.imread(f'casteljau2/{i}.jpg') for i in np.arange(0,131,1)]
    for i in np.arange(100,-1,-1):
        toStack.append(im.imread(f'casteljau2/{i}.jpg'))
    frames = np.stack(toStack,axis=0)
    im.mimsave('casteljau2.gif',frames,fps=13)

def cubic():
    '''Animates de Casteljau's algorithm generating a cubic Bézier curve'''
    fig,ax = plt.subplots()
    for i in np.arange(0,101,1):
        ax.set_xlim([0,100])
        ax.set_ylim([0,100])
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        fig.suptitle('de Casteljau\'s algorithm: cubic Bézier curve',fontsize=13)
        t = round(i/100,2)
        x = [10,25,80,70]
        y = [10,80,80,20]
        dx01 = x[1]-x[0]
        dy01 = y[1]-y[0]
        xB0 = x[0]+t*dx01
        yB0 = y[0]+t*dy01
        dx12 = x[2]-x[1]
        dy12 = y[2]-y[1]
        xB1 = x[1]+t*dx12
        yB1 = y[1]+t*dy12
        dx23 = x[3]-x[2]
        dy23 = y[3]-y[2]
        xB2 = x[2]+t*dx23
        yB2 = y[2]+t*dy23
        dx0 = xB1-xB0
        dy0 = yB1-yB0
        xB3 = xB0+t*dx0
        yB3 = yB0+t*dy0
        dx1 = xB2-xB1
        dy1 = yB2-yB1
        xB4 = xB1+t*dx1
        yB4 = yB1+t*dy1
        dx = xB4-xB3
        dy = yB4-yB3
        xB = xB3+t*dx
        yB = yB3+t*dy
        x += [xB0,xB1,xB2,xB3,xB4,xB]
        y += [yB0,yB1,yB2,yB3,yB4,yB]
        labels = [r'$P_0$',r'$P_1$',r'$P_2$',r'$P_3$',r'$B_0$',r'$B_1$',r'$B_2$',r'$B_3$',r'$B_4$',r'$B$']
        lines = [[(x[0],y[0]),(x[1],y[1])],[(x[1],y[1]),(x[2],y[2])],[(x[2],y[2]),(x[3],y[3])],[(xB0,yB0),(xB1,yB1)],[(xB1,yB1),(xB2,yB2)],[(xB3,yB3),(xB4,yB4)]]
        lc = co.LineCollection(lines,colors=[(0,0,0),(0,0,0),(0,0,0),(0,0,1),(0,0,1),(0,1,0)],linewidths=2)
        ax.add_collection(lc)
        t_dom = np.arange(0,i*0.01,0.01)
        t2=t_dom*t_dom
        t3=t2*t_dom
        s=1-t_dom
        s2=s*s
        s3=s2*s
        x_comp = (s3*x[0])+(3*s2*t_dom*x[1])+(3*s*t2*x[2])+(t3*x[3])
        y_comp = (s3*y[0])+(3*s2*t_dom*y[1])+(3*s*t2*y[2])+(t3*y[3])
        plt.plot(x_comp,y_comp,color='red')
        ax.scatter(x,y,c=[(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,1),(0,0,1),(0,0,1),(0,1,0),(0,1,0),(1,0,0)])
        for j,label in enumerate(labels):
            ax.annotate(label,(x[j]+1,y[j]+0.5))
        ax.text(44,12,f't = {t}')
        plt.savefig(f'casteljau3/{i}.jpg')
        if i != 100:
            ax.clear()
        else:
            for i in np.arange(101,131,1):
                plt.savefig(f'casteljau3/{i}.jpg')
    # plt.show()
    toStack = [im.imread(f'casteljau3/{i}.jpg') for i in np.arange(0,131,1)]
    for i in np.arange(100,-1,-1):
        toStack.append(im.imread(f'casteljau3/{i}.jpg'))
    frames = np.stack(toStack,axis=0)
    im.mimsave('casteljau3.gif',frames,fps=13)

def main():
    quadratic()
    cubic()

main()