"""Danny Huang
CAD
SoftDev
K05 - Parsing Lists and Random Selection of Devos and their duckies
2024-09-17
time spend: 1"""

import random
krewes = []

def createList():
    List = open("krewes.txt", "r")
    ind = List.read().split("@@@")
    for ppl in ind:
        info = ppl.split("$$$")
        krewes.append({"pd" : info[0], "devo" : info[1], "ducky" : info[2]})

def randomDevo():
    choice = random.randint(0, len(krewes)-1) 
    devo = krewes[choice]
    print(devo["devo"] + " " + devo["pd"] + " " + devo["ducky"])
  
createList()

randomDevo()
