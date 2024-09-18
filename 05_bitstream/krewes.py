"""Danny Huang
CAD
SoftDev
K05: Parsing Lists and Random Selection of Devos and their duckies
2024-09-17
time spent: 1 hour"""




import random
krewes = []




def createList():
   List = open("krewes.txt", "r") #opens text file with read permissions
   ind = List.read().split("@@@") #splits into list of individuals
   for ppl in ind:
   	info = ppl.split("$$$") #splits into person, ducky, and pd
   	krewes.append({"pd" : info[0], "devo" : info[1], "ducky" : info[2]}) #list created




def randomDevo():
   choice = random.randint(0, len(krewes)-1) #random number in range 0 to length
   devo = krewes[choice] #choose random devo
   print(devo["devo"] + " " + devo["pd"] + " " + devo["ducky"]) #print all info for that devo
createList()

randomDevo()

