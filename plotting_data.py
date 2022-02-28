# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 10:58:51 2022

@author: deang
"""
import matplotlib.pyplot as plt
import numpy as np
import os

#speficying the locating Reading in the file
os.chdir(r"C:\Users\deang\OneDrive\Desktop\Python Programs\Data_Thermal")


#Reading in the file for each column
Room_Temp = np.genfromtxt("pcm data.csv", skip_header=0, delimiter = ",", usecols=(2))
slope = np.genfromtxt("pcm data.csv", skip_header=0, delimiter = ",", usecols=(3))
k_foam = np.genfromtxt("pcm data.csv", skip_header=0, delimiter = ",", usecols=(5))
r_int = np.genfromtxt("pcm data.csv", skip_header=0, delimiter = ",", usecols=(8))
T_145 = np.genfromtxt("pcm data.csv", skip_header=0, delimiter = ",",usecols=(6))
Temp_hs = np.genfromtxt("pcm data.csv", skip_header=0, delimiter = ",",usecols=(9))
Tlin_minus_Temp_hs_correct = np.genfromtxt("pcm data.csv", skip_header=0, delimiter = ",",usecols=(13))

print(Tlin_minus_Temp_hs_correct)

#print(Temp_hs)


"""
better_view = np.sort(r_int)
print(better_view)
count = len(better_view)
print(count)
#print(Thermal_Data[1,1])

"""
#create 1 dimensional array of 28 0's
empty_array = np.zeros(28)
print(r_int,'\n')

#This removes the first 4 elements and last 3 elements in the array
new_r_int = np.delete(r_int,[0,1,2,3,-1,-2,-3])
new_k_foam = np.delete(k_foam,[0,1,2,3,-1,-2,-3])
new_Tlin_minus_Temp_hs_correct = np.delete(Tlin_minus_Temp_hs_correct,[0,1,2,3,-1,-2,-3])
#print(new_r_int)

print("This is std k_foam",np.std(new_k_foam),"This is mean k_foam",np.mean(new_k_foam),'\n')

print("This is std r_int",np.std(new_r_int),"This is mean r_int",np.mean(new_r_int),'\n')

print("This is std new_Tlin_minus_Temp_hs_correct",np.std(new_Tlin_minus_Temp_hs_correct),"This is mean new_Tlin_minus_Temp_hs_correct",np.mean(new_Tlin_minus_Temp_hs_correct),'\n')








plt.figure(1)
plt.plot(empty_array,slope,'ro')
#plt.subplot(122)
plt.title("Slope Values",fontsize = 20)
plt.xticks(fontsize = 15)
plt.yticks(fontsize = 12)
plt.show()




plt.figure(2)
plt.plot(k_foam,empty_array,'go')
plt.title("k_foam Values",fontsize=20)
plt.xticks(fontsize = 15)
plt.yticks(fontsize = 15)
#plt.subplot(121)
plt.show()


plt.figure(3)
plt.plot(r_int,'bo')
plt.title("r_int Values")
#plt.subplot(121)
plt.show()



plt.figure(4)
plt.plot(k_foam,r_int,'ko')
plt.title("k_foam vs r_int")
#plt.subplot(121)
plt.show()

plt.figure(5)
plt.plot(k_foam,slope,'mo')
plt.title("k_foam vs slope")
#plt.subplot(121)
plt.show()


plt.figure(6)
plt.plot(Temp_hs,'mo')
plt.title("Temperature at heat sink")
#plt.subplot(121)
plt.show()

plt.figure(7)
plt.plot(Tlin_minus_Temp_hs_correct,empty_array ,'yo')
plt.title("Tlin - Temp_hs_corrected",fontsize=20)
plt.xticks(fontsize = 15)
plt.yticks(fontsize = 15)
#plt.subplot(121)
plt.show()

