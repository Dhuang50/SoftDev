"""
PD + Princeden Hom and Danny Huang
SoftDev
K06 - CSV!
2024-09-19
Time Spent: 1 hour
"""

import csv
import random

all_occupations = []

with open("occupations.csv", mode = "r") as file:
    csvFile = csv.reader(file)
    pSum = 0 
    for line in csvFile:
        if not(line[0] == "Job Class" or line[0] == "Total"):
            pSum += float(line[1])*10
            all_occupations.append({"Job Class": line[0], "Percentage": float(line[1]), "pSum": pSum})
        
job = random.randint(0, 998)
for i in all_occupations:
    if job < i["pSum"]:
        print(i)
        break