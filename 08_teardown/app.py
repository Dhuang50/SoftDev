'''
CAD - Caden Khu, Aditya Anand, Danny Huang
SoftDev
K08 - teardown - exploring flask through past experiences
2024 - 09 - 20
Time Spent: 1 hour 

'''

'''
DISCO:
 - Print() prints into the terminal whereas return is outputted through the local host page
 - Why does __name__ return __main__ instead of __return?
 - What exactly is a Flask object? 

QCC:
0. We have seen similar syntax in Java
1. When writing paths in the terminal and when referencing file paths in code.
2. This prints to the terminal
3. It will print __main__ which is the __name__
4. It will appear in the page opened by the local host link. We know because that is what happened. 
5. I have seen similar constructs in other object oriented languages like java and js where the methods for a class is called. 
 ...

INVESTIGATIVE APPROACH:
Our team used a virtual enviornment to download flask and ran the python file within the venv. We then used the output of the file to make inferences about the code.
'''


from flask import Flask

app = Flask(__name__)                    # Q0: Where have you seen similar syntax in other langs?

@app.route("/")                          # Q1: What points of reference do you have for meaning of '/'?
def hello_world():
    print(__name__)                      # Q2: Where will this print to? Q3: What will it print?
    return "No hablo queso!"             # Q4: Will this appear anywhere? How u know?

app.run()                                # Q5: Where have you seen similar constructs in other languages?



