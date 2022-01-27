# -*- coding: utf-8 -*-
"""
Created on Fri May  7 20:05:30 2021

@author: Boujelbene Zaineb, Zribi Emna, Amara Molka, Ben Mbarek Rahma, Jlassi Khouloud
"""
# Exercice 1
import math
import matplotlib.pyplot as plt
import scipy.integrate as si
#1ère question:
    
#Def de la fonction f(y, t)= y:
    
def F1(y,t):
    return y

#Def de la fonction f(y,t)=sin(t) sin(y):
    
def F2(y,t):
    return math.sin(t) * math.sin(y)

#Fonction EULER:
    
def euler(f,a,b,y0,n):
    #résolution de y’=f(y,t) par la méthode d’Euler 
    h = (b-a) / n
    X = [a]
    Y = [y0]
    x = a
    y = y0
    for i in range(1,n+1):
        y += h * f(y,x)
        x += h
        X.append(x)
        Y.append(y)
    return (X,Y)

print(euler(F1,0,2,1,100))
print(euler(F2,0,50,1,100))

#Fonction RK2 (Runge-Kutta d’ordre 2):
    
def RK2(f,a,b,y0,n):
    #résolution de y’=f(y,t) par la méthode RK2 
    h = (b-a) / n
    X = [a]
    Y = [y0]
    x = a
    y = y0
    for i in range (1,n+1):
        z = y + h / 2 * f(y,x)
        p = f(z,x+h / 2)
        y += h * p
        x += h
        X.append(x)
        Y.append(y)
    return (X,Y)

print(RK2(F1,0,2,1,100))
print(RK2(F2,0,50,1,100))

#Fonction RK4 (Runge-Kutta d’ordre 4):
    
def RK4(f,a,b,y0,n):
    #résolution de y’=f(y,t) par la méthode RK4 """
    h = (b-a) / n
    X = [a]
    Y = [y0]
    x = a
    y = y0
    for i in range (1,n+1):
        p1 = f(y,x)
        y2 = y + h / 2 * p1
        p2 = f(y2,x + h/2)
        y3 = y + h / 2 * p2
        p3 = f(y3,x + h/2)
        y4 = y + h * p3
        p4 = f(y4,x +h)
        p = (p1 + 2* p2 + 2* p3 + p4)/6
        y += h * p
        x += h
        X.append(x)
        Y.append(y)
    return(X,Y)

print(RK4(F1,0,2,1,100))
print(RK4(F2,0,50,1,100))

#Tracage:
    
def trace(f,a,b,y0,n, g = False):
    X = [a + i * (b-a) / n for i in range(n+1)]
    if g:
        Y = [g(x) for x in X]
        plt.plot(X,Y, label = "théorique")
    Y = si.odeint(f, y0, X)
    Y = [ c[0] for c in Y]
    plt.plot(X,Y,label = "odeint")
    X, Y = euler(f,a,b,y0,n)
    plt.plot(X,Y, label = "euler")
    X, Y = RK2(f,a,b,y0,n)
    plt.plot(X,Y, label = "RK2")
    X, Y = RK4(f,a,b,y0,n)
    plt.plot(X,Y, label = "RK4")
    plt.legend(loc = "best")
    plt.title("Résolution par différentes méthodes (théorique/ odeint/ euler/ RK2/ RK4)")
    plt.show()
print(trace(F1,0,2,1,2 )) #lambda x: math.exp(x))
print(trace(F1,0,2,1,10)) #lambda x: math.exp(x))
print(trace(F1,0,2,1,50))
print(trace(F1,0,2,1,100))

#Fonction erreur:
    
def erreur(methode,f,a,b,y0,n,g):
     #erreur faite par rapport à la solution théorique g 
    X,Y = methode(f,a,b,y0,n)
    err=0
    for i in range(len(X)):
        e = abs(Y[i] - g(X[i]))
        if e > err:
            err = e
    return err
def affichage_erreurs(f,a,b,y0,n,g):
    print("Erreurs obtenues pour n = {} : ".format(n))
    print("Euler : {}".format(erreur(euler,f,a,b,y0,n,g)))
    print("RK2 : {}".format(erreur(RK2,f,a,b,y0,n,g)))
    print("RK4 : {}".format(erreur(RK4,f,a,b,y0,n,g)))
    print()
    
print(affichage_erreurs(F1,0,2,1,100,lambda x: math.exp(x)))
print(affichage_erreurs(F1,0,2,1,200,lambda x: math.exp(x)))
#Fonction Rang:

def rang_necessaire(methode,f,a,b,y0,g,eps):
    #rang nécessaire n pour obtenir une approximation uniforme à eps près 
    n = 1
    while erreur(methode,f,a,b,y0,n,g) > eps:
        n += 1
    return n
print("euler, 1e-2: {}".format(rang_necessaire(euler,F1,0,2,1,math.exp,1e-2)))
print("RK2, 1e-2: {}".format(rang_necessaire(RK2,F1,0,2,1,math.exp,1e-2)))
print("RK4, 1e-2: {}".format(rang_necessaire(RK4,F1,0,2,1,math.exp,1e-2)))
print("RK2, 1e-6: {}".format(rang_necessaire(RK2,F1,0,2,1,math.exp,1e-6)))
print("RK4, 1e-6: {}".format(rang_necessaire(RK4,F1,0,2,1,math.exp,1e-6)))
print("RK4, 1e-12: {}".format(rang_necessaire(RK4,F1,0,2,1,math.exp,1e-12)))
