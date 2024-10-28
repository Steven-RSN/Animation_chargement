# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 13:48:47 2024

@author: Clément
"""

import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = [7, 7]
import numpy as np

def ellipse_courbe_inferieure(a,b,y):
    """
    Parameters
    ----------
    a : Real, ellipse small axis.
    b : Real, ellipse major axis.
    y : Real, ellipse gravity center altitude.

    Returns
    -------
    X : list of points abscissa.
    Y : list of points ordinate.

    """
    X = []
    Y = []
    
    for n in np.linspace(0,np.pi,50):
        
        X.append( b*np.cos(n) )
        Y.append( y - a*np.sin(n))
        
    return X,Y

def ellipse_courbe_superieure(a,b,y):
    """
    Parameters
    ----------
    a : Real, ellipse small axis.
    b : Real, ellipse major axis.
    y : Real, ellipse gravity center altitude.

    Returns
    -------
    X : list of points abscissa.
    Y : list of points ordinate.

    """
    X = []
    Y = []
    
    for n in np.linspace(0,np.pi,50):
        
        X.append( b*np.cos(n) )
        Y.append( y + a*np.sin(n))
        
    return X,Y

plt.figure(1)

zoom = 4

x_min = -zoom
x_max = zoom
y_min = -0.3
y_max = 2*zoom-0.3





#Chute libre à vitesse constante jusqu'à impact avec le sol

g=5.8
y_0 = 6

#y = y_0 - 0.5*g*t**2


t_final = np.sqrt( (1-y_0)/(-0.5*g) )

dt = t_final / 30

for t in np.linspace(0,t_final,int(t_final/dt)):
    
    a=1
    b=1
    y = y_0 - 0.5*g*t**2
   
    
    X_inf, Y_inf = ellipse_courbe_inferieure(a,b,y)
    X_sup, Y_sup = ellipse_courbe_superieure(a,b,y)
    

    plt.clf()

    plt.plot([x_min,x_max],[0,0],color='black', lw=3)
    plt.fill_between([x_min,x_max],[0,0], [-0.3,-0.3],color='grey', alpha = 1)
    plt.xlim([x_min,x_max])
    plt.ylim([y_min,y_max])
    
    #plt.plot(X_inf,Y_inf,'.')
    #plt.plot(X_sup, Y_sup, '.')
    plt.plot(X_inf,Y_inf,lw=3, color='red')
    plt.plot(X_sup, Y_sup,lw=3, color='green')
    plt.fill_between(X_inf, Y_inf, Y_sup,color='green', alpha = 0.2)
    
    plt.pause(0.000001)

vitesse_impact = g*t
v0 = vitesse_impact


while 1:
    # A partir du contact avec le sol, la déformation de l'ellipse (1-a) doit être égale à y
    # La conservation de l'aire impose a*b = 1  --> b = 1/a
    # y continue de diminuer à vitesse constante pour le moment

    y_0 = y
    y_final = 0.74  # entre 0 et 1
    
    deformation_max = 1-y_final
    
    temp_de_demi_rebond = -2*(y_final-y_0)/v0
    
    dec = v0/temp_de_demi_rebond
    
    
    for t in np.linspace(0,temp_de_demi_rebond,int(2*temp_de_demi_rebond/dt)):
        
        # y varie de y_0 à y_final avec une décélération constante 
        
        y = y_0 - v0*t + dec/2*t**2
     
    
        a = y
        b = 1/a
        
        X_inf, Y_inf = ellipse_courbe_inferieure(a,b,y)
        X_sup, Y_sup = ellipse_courbe_superieure(a,b,y)
        
        plt.clf()
    
        plt.plot([x_min,x_max],[0,0],color='black', lw=3)
        plt.fill_between([x_min,x_max],[0,0], [-0.3,-0.3],color='grey', alpha = 0.2)
        plt.xlim([x_min,x_max])
        plt.ylim([y_min,y_max])
        
        plt.plot(X_inf,Y_inf,lw=3, color='red')
        plt.plot(X_sup, Y_sup,lw=3, color='green')
        plt.fill_between(X_inf, Y_inf, Y_sup,color='green', alpha = 0.2)
        
        plt.pause(0.001)
        
 
    y_0 = y
    y_final = 1
    
    # Meme chose qu'avant avec vitesse initiale nulle
    for t in np.linspace(0,temp_de_demi_rebond,int(2*temp_de_demi_rebond/dt)):
        
        # y varie de y_0 à y_final avec une décélération constante 
        
        y = y_0 + dec/2*t**2
      
        a = y
        b = 1/a
        
        X_inf, Y_inf = ellipse_courbe_inferieure(a,b,y)
        X_sup, Y_sup = ellipse_courbe_superieure(a,b,y)
        
        plt.clf()
    
        plt.plot([x_min,x_max],[0,0],color='black', lw=3)
        plt.fill_between([x_min,x_max],[0,0], [-0.3,-0.3],color='grey', alpha = 0.2)
        plt.xlim([x_min,x_max])
        plt.ylim([y_min,y_max])
        
        plt.plot(X_inf,Y_inf,lw=3, color='red')
        plt.plot(X_sup, Y_sup,lw=3, color='green')
        plt.fill_between(X_inf, Y_inf, Y_sup,color='green', alpha = 0.2)
        
        plt.pause(0.001)
    
    #Chute libre à vitesse constante jusqu'à impact avec le sol
    y_0 = y
    
    #v = v0 -g*t
    
    #y = y_0 + v0*t - 0.5*g*t**2
    
    
    t_final = 2*vitesse_impact/g
    
    for t in np.linspace(0,t_final,int(t_final/dt)):
        
        a= 1 + deformation_max*np.sin(5*np.pi/t_final*t)*np.exp(-3*t/t_final)
        b= 1/a
        y = y_0 + vitesse_impact*t - 0.5*g*t**2
       
    
        X_inf, Y_inf = ellipse_courbe_inferieure(a,b,y)
        X_sup, Y_sup = ellipse_courbe_superieure(a,b,y)
        
    
        plt.clf()
    
        plt.plot([x_min,x_max],[0,0],color='black', lw=3)
        plt.fill_between([x_min,x_max],[0,0], [-0.3,-0.3],color='grey', alpha = 0.2)
        plt.xlim([x_min,x_max])
        plt.ylim([y_min,y_max])
        
        plt.plot(X_inf,Y_inf,lw=3, color='red')
        plt.plot(X_sup, Y_sup,lw=3, color='green')
        plt.fill_between(X_inf, Y_inf, Y_sup,color='green', alpha = 0.2)
        
        plt.pause(0.001)

plt.show()
