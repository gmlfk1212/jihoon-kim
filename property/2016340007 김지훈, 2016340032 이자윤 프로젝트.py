#!/usr/bin/env python
# coding: utf-8

# In[2]:   

import numpy as np
import matplotlib.pyplot as plt
from math import*
from scipy.special import lambertw

f = open("pure_property.txt", 'r')
lines = f.readlines()
linelist = []
count = 0

for i in range(619):
    if lines[i].count(',') == 26:
        linelist.append(lines[i].split(','))
    elif lines[i].count(',') == 27:
        linelist.append(lines[i].split(','))
        a = linelist[i][2]+','+linelist[i][3]
        linelist[i][2] = a
        del linelist[i][3]
    elif lines[i].count(',') == 28:
        linelist.append(lines[i].split(','))
        a = linelist[i][2]+','+linelist[i][3]+','+linelist[i][4]
        linelist[i][2] = a
        del linelist[i][3]
        del linelist[i][3]
    elif lines[i].count(',') == 29:
        linelist.append(lines[i].split(','))
        a = linelist[i][2]+','+linelist[i][3]+','+linelist[i][4]+','+linelist[i][5]
        linelist[i][2] = a
        del linelist[i][3]
        del linelist[i][3]
        del linelist[i][3]
    elif lines[i].count(',') == 30:
        linelist.append(lines[i].split(','))
        a = linelist[i][2]+','+linelist[i][3]+','+linelist[i][4]+','+linelist[i][5]+','+linelist[i][6]
        linelist[i][2] = a
        del linelist[i][3]
        del linelist[i][3]
        del linelist[i][3]
        del linelist[i][3]

def Cpdata(T, a, b, c, d):
    return a + b*T + c * (T**2) + d * (T**3)
def Cpdata2(e):
    coefficient = 20.8
    return coefficient


ANSWER = '\"%s\"' %str(input("물질의 화학식 혹은 화학명을 입력해주세요.\n"))
for l in range(619) :    
    for k in range(27) : 
        if linelist[l][k]:
            continue
        else :
            linelist[l][k] = "N/A"

for j in range(619) :
    if linelist[j][2] == ANSWER or linelist[j][1] == ANSWER  :
        print("Name : %s" % linelist[j][2][1:-1])
        print("Formula : %s" % linelist[j][1][1:-1])
        print("Molecular weight : %s" %linelist[j][3])
        print("Normal freezing point : %s (K)" %linelist[j][4])
        print("Normal boiling point : %s (K)" %linelist[j][5])
        print("Critical temperature : %s (K)" %linelist[j][6])
        print("Critical pressure : %s (bar)" %linelist[j][7])
        if str(linelist[j][8]) == "N/A" :
            print("Critical density does not exist")
        else :
            density = round((float(linelist[j][3])/float(linelist[j][8])),4)
            print("Critical density : %s (g/cm3)" %density)   
        print("Critical volume : %s (cm3/mol)" %linelist[j][8])
        print("Critical compressibility factor : %s" %linelist[j][9])
        print("Pitzer's acentric factor : %s" %linelist[j][10])
        print("Dipole moment : %s" %linelist[j][11])
        print("Isobaric heat capacity of the ideal gas (J/mol.K)" )
        print("Cp = A + B*T + C*T^2 + D*T^3") 
        print("CpA : %s" %linelist[j][12])
        print("CpB : %s" %linelist[j][13])
        print("CpC : %s" %linelist[j][14])
        print("CpD : %s" %linelist[j][15])
        print("Standard enthalpy of formation of the ideal gas at 298.2K  : %s (J/mol)" %linelist[j][16])
        print("Standard Gibbs energy of formation of the ideal gas at 298.2K and 1 atm : %s (J/mol)" %linelist[j][17]) 
        if float(linelist[j][18]) == 0.00 :
                print("A : %s" %linelist[j][19])
                print("B : %s" %linelist[j][20])
                print("C : %s" %linelist[j][21])
                print("D : %s" %linelist[j][22])
                print("Tmin : %s (K)" %linelist[j][23])
                print("Tmax : %s (K)" %linelist[j][24])
        if float(linelist[j][18]) == 1.00 :
                print("Vapor pressure:  equation type")
                print("ln (Pvap/Pc) = ( A*t + B*t^1.5 + C*t^3 + D*t^6 )/(1-t)  where t = 1-T/Tc")
                print("A : %s" %linelist[j][19])
                print("B : %s" %linelist[j][20])
                print("C : %s" %linelist[j][21])
                print("D : %s" %linelist[j][22])
                print("Tmin : %s (K)" %linelist[j][23])
                print("Tmax : %s (K)" %linelist[j][24])
        if float(linelist[j][18]) == 2.00 :
                print("Vapor pressure:  equation type")
                print("ln Pvap = A - B/T + C*ln T + D*Pvap/T^2")
                print("A : %s" %linelist[j][19])
                print("B : %s" %linelist[j][20])
                print("C : %s" %linelist[j][21])
                print("D : %s" %linelist[j][22])
                print("Tmin : %s (K)" %linelist[j][23])
                print("Tmax : %s (K)" %linelist[j][24])
        if float(linelist[j][18]) == 3.00 :
                print("Vapor pressure:  equation type")
                print("ln Pvap = A - B/(T + C)")
                print("A : %s" %linelist[j][19])
                print("B : %s" %linelist[j][20])
                print("C : %s" %linelist[j][21])
                print("D : %s" %linelist[j][22])
                print("Tmin : %s (K)" %linelist[j][23])
                print("Tmax : %s (K)" %linelist[j][24])
        print("Liquid density : %s (g/cm3))" %linelist[j][25])
        print("At temperature : %s (K)\n\n" %linelist[j][26].rstrip())

        if linelist[j][23] == "N/A" or linelist[j][24] == "N/A":
            print("Cp그래프를 그릴 수 없는 화합물입니다.")
            
        else:
            if linelist[j][12] == "N/A":
                print("Cp그래프를 그릴 수 없는 화합물입니다.")
            else:
                if linelist[j][13] == "N/A":
                    x = [float(linelist[j][23]), float(linelist[j][24])]
                    y = [20.8, 20.8]
                    plt.plot(x,y)
                    print("Graph of Cp")
                    plt.show()
                else:                            
                    a = float(linelist[j][12])
                    b = float(linelist[j][13])
                    c = float(linelist[j][14])
                    d = float(linelist[j][15])
        
                    x = np.linspace(float(linelist[j][23]), float(linelist[j][24]), 101)
                    y = Cpdata(x, a, b, c, d)
                    plt.plot(x,y)
                    print("Graph of Cp")
                    plt.show()
        def Pdata1(T, k, l, m, n):
            t = 1 - T/float(linelist[j][6])
            return np.exp(k*t + l*(t**1.5) + m*(t**3) + n*(t**6)) * float(linelist[j][7])
        
        def Pdata2(T, k, l, m, n):
            return - (T**2) / n * lambertw(- n * np.exp(k - l/T) * (T**(m-2)))
        
        def Pdata3(T, k, l, m):
            return np.exp(k - l/(T + m))
        
        if float(linelist[j][18]) == 0:
            print("Pvap그래프를 그릴 수 없는 화합물입니다.")
        
        elif float(linelist[j][18]) == 1:
            k = float(linelist[j][19])
            l = float(linelist[j][20])
            m = float(linelist[j][21])
            n = float(linelist[j][22])
            
            x = np.linspace(float(linelist[j][23]), float(linelist[j][24]), 101)
            z = Pdata1(x, k, l, m, n)
            plt.plot(x,z)
            print("Graph of Pvap")
            plt.show()
        elif float(linelist[j][18]) == 2:
            k = float(linelist[j][19])
            l = float(linelist[j][20])
            m = float(linelist[j][21])
            n = float(linelist[j][22])
            
            x = np.linspace(float(linelist[j][23]), float(linelist[j][24]), 101)
            z = Pdata2(x, k, l, m, n)
            plt.plot(x,z)
            print("Graph of Pvap")
            plt.show()
        elif float(linelist[j][18]) == 3:
            k = float(linelist[j][19])
            l = float(linelist[j][20])
            m = float(linelist[j][21])
            
            x = np.linspace(float(linelist[j][23]), float(linelist[j][24]), 101)
            z = Pdata3(x, k, l, m)
            plt.plot(x,z)
            print("Graph of Pvap")
            plt.show()
        break
    else:
        count = j
if count == 618:
    print("물질의 화학명 혹은 화학식을 다시 확인해주세요.")
    


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




