#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 14:46:01 2022

@author: freddie
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 15:35:39 2022

@author: freddie
"""

import numpy
import matplotlib.pyplot as plt
external_temp = [3, 3, 2, 2, 3, 4, 5, 6, 6, 6 , 8, 10,11, 10, 9, 7, 5, 5, 5, 4, 3, 3 , 3, 3]
ground_temp = 10


flow_velocity = 4
internal_temp = 20
door_open = [3, 4, 5]
CSA = 1.6
time = list(range(0,24))
heat_on = 0
heat_off = 100
time_open = 0.083
Cp = 1000
density = 1.204

A_walls = 769.28
A_roof = 640
A_ground = 320


U_walls = 2
U_roof =  2.5
U_ground = 1.3



gas = 0.103
elec = 0.34


totalg = 0
totale = 0 
Ce_list = []
Cg_list = []




for x in time:
    
    if time[x] in door_open:
    
        
        
        Ht_walls = (A_walls * U_walls * (internal_temp - external_temp[x]))/1000
        Ht_roof = (A_roof * U_roof * (internal_temp - external_temp[x]))/1000
        Ht_ground = (A_ground * U_ground * (internal_temp - ground_temp))/1000
        
        Ht = Ht_walls + Ht_roof + Ht_ground
        
        vol_flow = flow_velocity * CSA
        Hv = (time_open * Cp * density * vol_flow*(internal_temp - external_temp[x]))/1000

        H_total = Hv +Ht
        
        
        Cost_gas = H_total * gas
        Cost_elec = H_total * elec
        
    
        Ce_list.append(Cost_elec)
        Cg_list.append(Cost_gas)
        totalg += Cost_gas
        totale += Cost_elec
       
    else:
        
     
        Ht_walls = (A_walls * U_walls * (internal_temp - external_temp[x]))/1000
        Ht_roof = (A_roof * U_roof * (internal_temp - external_temp[x]))/1000
        Ht_ground = (A_ground * U_ground * (internal_temp - ground_temp))/1000
        
        Ht_total = Ht_walls + Ht_roof + Ht_ground
        
        Cost_gas = Ht_total * gas
        Cost_elec = Ht_total * elec
        
    
        Ce_list.append(Cost_elec)
        Cg_list.append(Cost_gas)
        totalg += Cost_gas
        totale += Cost_elec
    

print(totalg)    
print(totale)


M = 4514
C = 700






# can plot time of day on x axis and temp and cost on y axis


plt.plot(time, Ce_list, label = "Cost of Electric Heating")
plt.plot(time, Cg_list, label = "Cost of Gas Heating")
plt.xlabel('24 Hour Time')
plt.ylabel('Cost (pounds)')

plt.xlim([0,23])
plt.legend()
plt.show()

plt.plot(time, external_temp, label = "External Temperature")
plt.xlabel('24 Hour Time')
plt.ylabel('Temperature')

plt.xlim([0,23])
plt.legend()
plt.show()