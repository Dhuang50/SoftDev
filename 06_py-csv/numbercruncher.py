"""
PD + Princeden Hom and Danny Huang
SoftDev
K06 - CSV!
2024-09-19
Time Spent: 1 hour
"""

import csv

all_occupations = []

with open("occupations.csv", mode = "r") as file:
    lines = file.readline()
    pSum = 0
    for line in lines:
        pSum += float(line[1])*10
        all_occupations.append({"Job Class": line[0], "Percentage": float(line[1]), "pSum": pSum})
        
print(all_occupations)