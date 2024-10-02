'''
Wen Zhang, Jackie Zeng, Danny Huang
Made in Africa
SoftDev
K13 -- creating template to make html table
2024-09-30
Time spent: 30 mins
'''

import random
import csv

occupation_dict = []
occupation_list = []
percentages = []
links=[]

with open('data/occupations.csv', newline ='') as csvfile:  #Reading csv and assigning values to their respective lists
    file = csv.DictReader(csvfile)
    for row in file:
        occupation_list.append(row['Job Class'])
        percentages.append(float(row['Percentage']))
        links.append(row['Helpful Link'])
        occupation_dict.append([row['Job Class'], float(row['Percentage']),row["Helpful Link"]]) 
        

occupation_dict = occupation_dict[0:-1]  #Splicing lists and dictionaries
occupation_list = occupation_list[1:-1]
percentages = percentages[1:-1]

def select_occupation(occupation_list, percentages):
    return random.choices(occupation_list, weights=percentages, k=1)   #Randomly selecting occupation based on percentages
     
    # -------------------------------------------------------------



from flask import Flask, render_template
app = Flask(__name__)

@app.route("/wdywtbwygp")      #Flask and jinja using template
def page():
    head = "A table of job occupation with helpful links to help you get started with that guide"
    tnpgroster = "Made In Africa - Wen, Jackie, Danny"
    occupation = select_occupation(occupation_list, percentages)
    
    return render_template('tablified.html', title = "Job Table", Heading = head, TNPGROSTER = tnpgroster, Job = "Chosen Job: " + str(occupation[0]), Occ = "Jobs", collection = occupation_dict)
    
    
if __name__ == "__main__":      
    app.debug = True            
    app.run()
