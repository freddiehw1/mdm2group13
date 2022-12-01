#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 19:00:04 2022

@author: freddie
"""
# Adjustable Variables




hours_heating_on = 720
hours_door_opens = 140
time_open = 0.083       #This is a fraction of an hour representing time door open per hour
d = 30  # Days a month that the heating turns on


flow_velocity = 4       #This is wind speed in m/s

internal_temp = 20      # this is the desired internal temperature

external_temp = [5.26,5,7,9,12,15,17,17,15,11,8,6]     #This is the list of average temperatures - 1 for each month
ground_temp = 10.4
CSA = 1.6           # Area of the door



U_walls = 2
U_roof =  2.5
U_ground = 1.3


# Non Adjustable Variables

A_walls = 769.28
A_roof = 640
A_ground = 320


Cp = 1000
density = 1.204
Volume = 3694
M = density * Volume



time = list(range(0,12))





gas = 0.103
elec = 0.34

totalg = 0
totale = 0 
Ce_list = []
Cg_list = []

# Check UNits of Cp 

for x in time:
    

    
        
        Ht_walls = (A_walls * U_walls * (internal_temp - external_temp[x]))/1000
        Ht_roof = (A_roof * U_roof * (internal_temp - external_temp[x]))/1000
        Ht_ground = (A_ground * U_ground * (internal_temp - ground_temp))/1000
        
        Ht = Ht_walls + Ht_roof + Ht_ground
        
        
        vol_flow = flow_velocity * CSA
        Hv = (Cp * density * vol_flow*(internal_temp - external_temp[x]))/1000
        
        q = M * Cp * (internal_temp - external_temp[x])/(3600*1000)

        H_total = (Ht * hours_heating_on)+(time_open * Hv * hours_door_opens) + (d*q)
      
        
        Cost_gas = H_total * gas
        Cost_elec = H_total * elec
        
    
        Ce_list.append(Cost_elec)
        Cg_list.append(Cost_gas)
        totalg += Cost_gas
        totale += Cost_elec
        
        
        
    

print(totalg)    
print(totale)
