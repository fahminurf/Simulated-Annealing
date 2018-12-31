
import numpy as no


def funct(xi,xii):
    return - (no.absolute(no.sin(xi)*no.cos(xii)*no.exp(no.absolute(1-(no.sqrt(xi**2+xii**2)/no.pi)))))
    
def prob(cs,ns,t):
    return (no.exp(no.negative(ns-cs/t)))

xi=no.random.uniform(no.negative(10),10)
xii=no.random.uniform(no.negative(10),10)
t=1000

cs=funct(xi,xii)
best=cs

while (t>0.1):
    nxi=xi+no.random.uniform(no.negative(10),10)
    nxii=xii+no.random.uniform(no.negative(10),10)
    if (nxi>10 or nxi< -10):
        nxi=no.random.uniform(no.negative(10),10)
    if(nxii>10 or nxii< -10):
        nxii=no.random.uniform(no.negative(10),10)
        
    ns=funct(nxi,nxii)
    if (ns<cs):
        cs=ns
        best=cs
        xi=nxi
        xii=nxii
    else:
        probs=prob(cs,ns,t)
        if (no.random.uniform(0,1)<probs):
            cs=ns
            xi=nxi
            xii=nxii
        #endif
    #endif
    t=t*0.99

print("Nilai Minimum : ",best)




    