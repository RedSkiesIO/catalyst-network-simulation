from scipy.stats import hypergeom
from scipy.stats import binom
from decimal import *
import numpy as np
import os
import math
from cycler import cycler
#%matplotlib inline  
#import matplotlib as mpl
#mpl.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib.ticker import FormatStrFormatter

#N: total number of nodes in pool (validators)
#V: total number of working validators nodes (workers) 
#O: total number of malicious nodes in pool (malicious validators)
#p: total number of malicious nodes selected for validation (malicious workers)
#Vmin: mininim number of validating nodes (minimum hashes collected by a worker for a valid ratio r_i = m/V_i where V_min <= V_i <= V)

def plot_ratio_VoverN(rO,rN,thre):
        pH=[]
        for rNi in rN:
            O=rNi*rO
            print("N, O: ",rNi,", ",O,". Varying V to find proba ~ 10-9")
            Vmin = math.floor(0.001*rNi)
            Vmax = math.floor(0.2*rNi)
            rangeV = range(Vmin,Vmax,100)
            proba_thre = 1
            rVi = Vmin
            Vbin = 10
            V_thre = 0
            while proba_thre > thre:
                p = math.floor(rVi/2) + 1
                proba_thre = hypergeom.sf(p, rNi, O, rVi)
                V_thre = rVi
                #print(rVi,", prob --> ",proba_thre)
                rVi = rVi + Vbin
            #print("--> ",V_thre/N) 
            pH.append(V_thre/N)
        return (pH)


N = 10000
V = 2000
rR = [0.1,0.2,0.3,0.4,0.45]


proba_thre = 0.000000001
rangeN = range(5000,100000,1000)
rO=0.2
p1VoN_1 = plot_ratio_VoverN(rO,rangeN,proba_thre)
rO=0.3
p1VoN_2 = plot_ratio_VoverN(rO,rangeN,proba_thre)
rO=0.4
p1VoN_3 = plot_ratio_VoverN(rO,rangeN,proba_thre)
rO=0.45
p1VoN_4 = plot_ratio_VoverN(rO,rangeN,proba_thre)
plt.plot(rangeN,p1VoN_1, label='20% malicious')
plt.plot(rangeN,p1VoN_2, label='30% malicious')
plt.plot(rangeN,p1VoN_3, label='40% malicious')
plt.plot(rangeN,p1VoN_4, label='45% malicious')
plt.title('V/N threshold needed for a probability of attack < $10^{-9}$')
plt.xlabel('N')
plt.ylabel('V/N (prob < $10^{-9}$)')
plt.legend(loc='center right')
plt.savefig('Graphs/ratioVOverNRation10-9.png')