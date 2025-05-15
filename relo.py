import numpy as np
def regular_polygon_Relo(n:int=3, center:list=[0,0], r:int=1, N:int=100)->np.ndarray:
    """do:
    матричное описание границы многоугольника РЕЛО

    Arguments: 
    * n: количество вершин (n>2 и n - нечетное), standard: n=3
    * center: массив координат центра правильного многоугольника Рело, standard: center = np. array([0,0])
    * r: ширина правильного многоугольника Рело (r>0), standard: r=1
    * N: количество точек для описания одной стороны правильного многоугольника Рело (N>0 и N - натуральное), standard: N=100

    return:
    матрица, каждая строка которой содержит координаты точек границы многоугольника РЕЛО

    """
    
    assert n>0, 'positive amount of vertices only'
    assert r>0, 'positive radius only'
    assert N>0, 'positive amount of line points only'
    assert n%2==1 and n!=1, 'only odd amount of vertices and not 1'
    assert type(center)==list and len(center)==2, 'only list with two coords'

    center=np.array(center)
    alpha=2*np.pi/n 
    beta=alpha/2
    angle= np.linspace(-beta/2,beta/2,N)
        
    l=r*np.sqrt(2*(1-np.cos(beta)))   # find l - lenghth of right rectangle side (base of relo rectangle)
    R=l/(2*np.sin(np.pi/n))   # radius of circle for relo rectangle 

    t=np.arange(0,2*np.pi,2*np.pi/n)   
    vertices=center+R*np.transpose([np.cos(t),np.sin(t)])  # vertices of relo rectangle

        # lists of sides
    list_sides = [vertices[i] + r*np.transpose([np.cos(angle + np.pi + i*alpha), np.sin(angle + np.pi + i*alpha)]) for i in range(n)] 
    sides = np.concatenate(list_sides) # concatenating sides 
    return sides
