

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

#==========================================================
students = {}
courses = {}

with open('students.csv', newline='') as csvfile:
    students = csv.DictReader(csvfile)
    
with open('courses.csv', newline='') as csvfile:
    courses = csv.DictReader(csvfile)
    
diffcourses = []
for i in courses:
    if not(i["code"] in courses):
        diffcourses.append(i["code"])
        
studentlists = []
for student in students:
    studentdata = {}
    
    
    for i in courses:
        if(i["id"] = student["id"]):
            


command = ""          # test SQL stmt in sqlite3 shell, save as string
c.execute(command)    # run SQL statement

#==========================================================

db.commit() #save changes
db.close()  #close database
