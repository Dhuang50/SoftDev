
import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

#==========================================================

studentcsv =  open('students.csv', newline='')
students = csv.DictReader(studentcsv)
    
coursescsv = open('courses.csv', newline='')
courselist = csv.DictReader(coursescsv)
    
courses= []
diffcourses = []
for i in courselist:
    courses.append(i)
    if not(i["code"] in diffcourses):
        diffcourses.append(i["code"])
  
studentlists = []
for student in students:
    studentdata = {}
    studentdata['name'] = student['name']
    studentdata['id'] = student['id']
    studentdata['age'] = student['age']
    individual_course =[]
    print(student['id'])
    for i in courses:
        print(i['id'])
        if i['id'] == student['id']:
            studentdata[f"{i['code']}"] = i['mark']
            individual_course.append(i['code'])
            
    for i in diffcourses:
        if not i in individual_course:
            studentdata[f'{i}'] = 'NULL'
    studentlists.append(studentdata)
print(studentlists)

c.execute("DROP TABLE IF EXISTS roster")
c.execute(f"CREATE TABLE roster(name TEXT, id INTEGER, age INTEGER, {diffcourses[0]}, {diffcourses[1]}, {diffcourses[2]}, {diffcourses[3]}, {diffcourses[4]})")
c.execute("SELECT * FROM roster")

for i in studentlists:
    c.execute(f"INSERT INTO roster VALUES ('{i['name']}', {i['id']}, {i['age']}, {i[diffcourses[0]]}, {i[diffcourses[1]]}, {i[diffcourses[2]]}, {i[diffcourses[3]]}, {i[diffcourses[4]]})")

    

command = "SELECT * FROM roster"          # test SQL stmt in sqlite3 shell, save as string
c.execute(command)    # run SQL statement

#==========================================================

db.commit() #save changes
db.close()  #close database
