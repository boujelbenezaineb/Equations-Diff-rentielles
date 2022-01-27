import math
import scipy.integrate as si
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# 1ère question:
def F(Y,t):
    return [Y[1], -math.sin(Y[0]) - Y[1] / 4]
t = np.linspace(0,30,500)
for v in range(2,5):
    if v==3:
        continue
    Y = odeint(F,[0,v],t)
    V = [i[0] for i in Y]
    Z = [i[1] for i in Y]
    plt.plot(t,V,label='v={}'.format(v))
plt.legend()
plt.xlabel('temps')
plt.ylabel('position')
plt.grid()
plt.title('Solution pour v=2 et v=4')
plt.show()

def tracage(vmax,tmax):
    #for v in range(1, vmax+1):
    X,V,T= pendule(vmax,tmax)
    plt.plot(T,X,label="v={}".format(vmax))
    
    plt.xlabel("temps")
    plt.ylabel("position")
    plt.grid()
    plt.title("Position en fonction du temps")
    plt.show()
#interprétation: le lancement du pendule avec une vitesse égale à 4 effectue un nombre de tours (osscillations) inférieur à celui d'une vitesse égale à 2, d'ou la stabilisation.

# 2éme question:
def diagramme_phase(V,tmax):
    for v in V:
        X,V,T= pendule(v,tmax)
        plt.plot(X,V,label ="v={}".format(v))
    plt.xlabel("position")
    plt.ylabel("vitesse")
    plt.grid()
    plt.title("Diagramme de phase")
    plt.legend()
    plt.show()
print(diagramme_phase([2,4],30))

# 3éme question:
def vitesse(k,err):
    v=1
    X,V,T= pendule(v,100)
    while X[-1] < (2 * k -1) *math.pi:
        v += 1
        X,V,T= pendule(v,100)
    vmax = v
    vmin = v-1
    while vmax - vmin > err:
        v = (vmax + vmin) / 2
        X,V,T= pendule(v,100)
        if X[-1] < (2 * k -1) *math.pi:
            vmin = v
        else:
            vmax = v
    return vmax
for k in range(10):
    print("Pour faire ",k," tours: v=",vitesse(k,1e-10))
