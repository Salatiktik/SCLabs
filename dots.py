import math
import time
from matplotlib import pyplot as plot
import random

ans = 1E20
dots = ()

def quadro():
    global dots
    min = math.pow(dots[0][0]-dots[1][0],2)+math.pow(dots[0][1]-dots[1][1],2)
    for i in dots:
        for j in dots:
            if(i!=j):
                if(math.pow(i[0]-j[0],2)+math.pow(i[1]-j[1],2)<min):
                    min = math.pow(i[0]-j[0],2)+math.pow(i[1]-j[1],2)

    return min

def sort(parmametr):
    global dots
    return sorted(dots,key = lambda x: x[parmametr])

def minRec(start,end):
    global ans
    global dots
    if math.fabs(end-start)>=3:
        minRec(start,int((start+end)/2))
        minRec(int((start+end)/2),end)
        return
    else:
        if(math.pow(dots[start][0]-dots[end][0],2)+math.pow(dots[start][1]-dots[end][1],2)<ans):
            ans = math.pow(dots[start][0]-dots[end][0],2)+math.pow(dots[start][1]-dots[end][1],2)
        return
        


def main():
    global dots
    y1 = []
    y2 = []
    x  = []
    for i in range (4,100):
        dots = [(random.uniform(0,1000000),random.uniform(0,1000000)) for g in range(0,i)]
        dots = set(dots)
        dots = list(dots)
        startQuadro = time.time()
        quadro()
        timeQuadro = time.time()-startQuadro
        startRec = time.time()
        minRec(0,i-1)
        timeRec = time.time()-startRec

        y1.append(timeQuadro)
        y2.append(timeRec)
        x.append(i)
        
    plot.plot(x,y1,'-',x,y2,':')
    plot.show()

main()