"""Danny Huang
CAD
SoftDev
Parsing Lists and Random Selection of Devos and their duckies
2024-09-17
time spend: 1"""

krewes = []

def createList():
    List = open("krewes.txt", "r")
    ind = List.read().split("@@@")
    for ppl in ind:
        info = ppl.split("$$$")
        for i in info:
            p = {
                "pd" : i[0],
                "devo" : i[1],
                "ducky" : i[2]
                }
            krewes.append(p)
    
createList()
print(krewes)