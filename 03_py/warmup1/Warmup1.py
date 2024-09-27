'''Returns true when it is a weekday or when we're on vacation
sleep_in(False, False) → True   Not a weekday 
sleep_in(True, False) → False   Weekday and not on vacation
sleep_in(False, True) → True    On vacation
'''
def sleep_in(weekday, vacation):
  return not weekday or vacation

""" Return true if a and b are both smiling or if neither are similing
monkey_trouble(True, True) → True     Both Smiling
monkey_trouble(False, False) → True   Neither are smiling
monkey_trouble(True, False) → False   Only one is smiling
"""
def monkey_trouble(a_smile, b_smile):
  return a_smile == b_smile

""" Return sum when a and b are diff, if a = b return double of their sum
sum_double(1, 2) → 3     Diff -> sum
sum_double(3, 2) → 5     Diff -> sum
sum_double(2, 2) → 8     a = b -> sum*2
"""
def sum_double(a, b):
  if a != b:
    return a + b
  else:
    return 2*(a+b)
  
""" |n-21| when n <= 21, when n>21 2*|n-21|
diff21(19) → 2    n<21
diff21(10) → 11   n<21
diff21(21) → 0    n=21
"""
def diff21(n):
  if n>21:
    return 2*(abs(21-n))
  else:
    return (abs(21-n))

"""We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23. We are in trouble if the parrot is talking and the hour is before 7 or after 20. Return True if we are in trouble.
parrot_trouble(True, 6) → True
parrot_trouble(True, 7) → False
parrot_trouble(False, 6) → False
"""
def parrot_trouble(talking, hour):
  if (hour < 7 or hour > 20) and talking:
    return True
  else:
    return False

"""Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.
makes10(9, 10) → True
makes10(9, 9) → False
makes10(1, 9) → True
"""
def makes10(a, b):
  if a == 10 or b == 10 or a + b == 10:
    return True
  else:
    return False
  
"""Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num) computes the absolute value of a number.
near_hundred(93) → True
near_hundred(90) → True
near_hundred(89) → False
"""
def near_hundred(n):
  return abs(100 - n) <= 10 or abs(200 - n) <= 10

"""Given 2 int values, return True if one is negative and one is positive. Except if the parameter "negative" is True, then return True only if both are negative.
pos_neg(1, -1, False) → True
pos_neg(-1, 1, False) → True
pos_neg(-4, -5, True) → True
"""
def pos_neg(a, b, negative):
  if negative:
    return a < 0 and b < 0
  else:
    return a/b < 0

"""Given a string, return a new string where "not " has been added to the front. However, if the string already begins with "not", return the string unchanged.
not_string('candy') → 'not candy'
not_string('x') → 'not x'
not_string('not bad') → 'not bad'
"""
def not_string(str):
  if str[:3] == "not":
    return str
  else:
    return "not " + str
  
"""Given a non-empty string and an int n, return a new string where the char at index n has been removed. The value of n will be a valid index of a char in the original string (i.e. n will be in the range 0..len(str)-1 inclusive).
missing_char('kitten', 1) → 'ktten'
missing_char('kitten', 0) → 'itten'
missing_char('kitten', 4) → 'kittn'
"""
def missing_char(str, n):
  return str[:n] + str[n+1:]

"""Given a string, return a new string where the first and last chars have been exchanged.
front_back('code') → 'eodc'
front_back('a') → 'a'
front_back('ab') → 'ba'
"""
def front_back(str):
  if len(str) <= 1:
    return str
  front = str[0]
  back = str[len(str)-1]
  if len(str) == 2:
    return back + front
  else:
    return back + str[1:len(str)-1] + front
  
"""Given a string, we'll say that the front is the first 3 chars of the string. If the string length is less than 3, the front is whatever is there. Return a new string which is 3 copies of the front.
front3('Java') → 'JavJavJav'
front3('Chocolate') → 'ChoChoCho'
front3('abc') → 'abcabcabc'
"""
def front3(str):
  rep = ""
  if len(str) < 3:
    rep = str
  else:
    rep = str[:3]
  return rep + rep + rep

