import math
import random
T=1000
N=5
V=2
width=[]
vOfRivers=[]
for i in range(N):
    s_river=random.randint(1,6)
    v_river=random.randint(1,4)
    width.append(s_river)
    vOfRivers.append(v_river)
angels=[random.radint(0,90) for i in range(N)]
t,s=0,0
theta=1
for i in range(N):
    t+=s_river[i]/V*math.cos(math.radians(angels[i]))
    s+=(s_river[i]/V*math.cos(math.radians(angels[i])))*(v_river[i]+V*math.sin(math.radians(angels[i])))
new_formula=s-theta*(t-T)