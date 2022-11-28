#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 19:00:04 2022

@author: freddie
"""

external_temp = [5,5,7,9,12,15,17,17,15,11,8,6]
ground_temp = 10


flow_velocity = 4
internal_temp = 20
door_open = [3, 4, 5]
CSA = 1.6
time = list(range(0,12))
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
    

    
        
        Ht_walls = (A_walls * U_walls * (internal_temp - external_temp[x]))/1000
        Ht_roof = (A_roof * U_roof * (internal_temp - external_temp[x]))/1000
        Ht_ground = (A_ground * U_ground * (internal_temp - ground_temp))/1000
        
        Ht = Ht_walls + Ht_roof + Ht_ground
        Ht = Ht * 700
        
        vol_flow = flow_velocity * CSA
        Hv = (time_open * Cp * density * vol_flow*(internal_temp - external_temp[x]))/1000
        Hv = Hv * 30 
        H_total = Hv +Ht
      
        
        Cost_gas = H_total * gas
        Cost_elec = H_total * elec
        
    
        Ce_list.append(Cost_elec)
        Cg_list.append(Cost_gas)
        totalg += Cost_gas
        totale += Cost_elec
        print(Cost_gas)
        
        
    

print(totalg)    
print(totale)
