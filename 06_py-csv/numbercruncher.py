"""
PD + Princeden Hom and Danny Huang
SoftDev
K06 - CSV!
2024-09-19
Time Spent: 1 hour
"""

import csv    # Import required libraries
import random

all_occupations = []  #Creates list of dictionaries for all occupations 

with open("occupations.csv", mode = "r") as file:  # Opens CSV File
    csvFile = csv.reader(file)   # Reads CSV File
    pSum = 0  #Creates pSum variable which will be used as divider
    for line in csvFile:   #Loops through CSV object
        if not(line[0] == "Job Class" or line[0] == "Total"):   #Takes out first and last row
            pSum += float(line[1])*10   #Calculates pSum value
            all_occupations.append({"Job Class": line[0], "Percentage": float(line[1]), "pSum": pSum})  #Creates dictionary and adds to list
        
job = random.randint(0, 998)   #Random Integer
for i in all_occupations:  #Loops through list
    if job < i["pSum"]:   #Finds range the random integer is in
        print(i) #Prints the selected occupation
        break   #Breaks out of loop as range was found