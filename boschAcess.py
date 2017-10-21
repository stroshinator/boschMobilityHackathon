#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 20:31:53 2017

@author: Drew
"""

import gmplot

def readfile(filepath, delim):
    """Extracts coordinates from a text file

    Reads a text file in the format of the files given for this programming 
    assignment, and extracts the ordered pairs of the coordinates stored in the 
    file.
    
    Args:
        filepath: A string representing the file path of the text file to read.
        
    Returns:
        A list of integer tuples where each tuple is an ordered pair for an 
        (x, y) coordinate.
    """
    
    with open(filepath, 'r') as f:
        data = f.readlines()
        
        coordinates = []        
        
        for line in data:
            temp = line.split('\t')
            temp = [float(val) for val in temp] 
            temp = tuple(temp)
            coordinates.append(temp)
        
        return coordinates
    
    
def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

        
def is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
   
"""/***************************** MAIN DRIVER *****************************/"""
with open('data/ridership.txt', 'r') as f:
    data = f.readlines()
    
    ridership = []        
    
    for i in range(1, len(data)):
        flag = True
        innerTuple = []
        temp = data[i].split('\t')
        
        if is_int(temp[3]):
            innerTuple.append(int(temp[3]))
        else:
            flag = False
        
        if is_float(temp[4]):
            innerTuple.append(float(temp[4]))
        else:
            flag = False    
        
        # Coordinate processing
        tempCoord = temp[8]
        tempCoord = tempCoord.split(',')
        
        tempLat = tempCoord[0]
        
        for j in range(0, len(tempLat)):
            if tempLat[j] == '(':
                lats = tempLat[j+1:len(tempLat)]
        
        if is_float(lats):
            innerTuple.append(float(lats))
        else:
            flag = False        
            
        tempLong = tempCoord[1]
        
        for j in range(0, len(tempLong)):
            if tempLong[j] == ')':
                longs = tempLong[1:j]        
        
        if is_float(longs):
            innerTuple.append(float(longs))
        else:
            flag = False          
        
        if flag:
            ridership.append(tuple(innerTuple))
        

""" DRAW HEAT MAP """   
# Ridership 
filteredLats = []
filteredLongs = []

for i in ridership:
    for j in range(0, int(i[1])):
        filteredLats.append(i[2])
        filteredLongs.append(i[3])

gmap = gmplot.GoogleMapPlotter(41.8781, -87.6298, 11)

gmap.heatmap(filteredLats, filteredLongs, radius=15)

gmap.draw("ridership.html")


# All stops
filteredLats = []
filteredLongs = []

for i in ridership:
    filteredLats.append(i[2])
    filteredLongs.append(i[3])

gmap = gmplot.GoogleMapPlotter(41.8781, -87.6298, 11)

gmap.heatmap(filteredLats, filteredLongs, radius=10)

gmap.draw("stops.html")


# Above average ridership
filteredLats = []
filteredLongs = []

sumRiders = 0
for i in ridership:
    sumRiders += i[1]

avgRiders = sumRiders / len(ridership)

for i in ridership:
    if i[1] > avgRiders:
        filteredLats.append(i[2])
        filteredLongs.append(i[3])

gmap = gmplot.GoogleMapPlotter(41.8781, -87.6298, 11)

gmap.heatmap(filteredLats, filteredLongs, radius=10)

gmap.draw("aboveAverage.html")




#coords = readfile('data/coordinates.txt', '\t')
#
#lats = []
#longs = []
#
#for i in coords:
#    longs.append(i[0])
#    lats.append(i[1])
#
#gmap = gmplot.GoogleMapPlotter(41.8781, -87.6298, 11)
#
#gmap.heatmap(lats, longs, radius=5)
#
#gmap.draw("test.html")


    







    
    
    
    
    
    
    
    
  
    
    
    
    
    
    