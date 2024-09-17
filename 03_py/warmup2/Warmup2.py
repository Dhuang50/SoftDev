def string_times(str, n):
  final = ""
  for i in range(n):
	final += str
  return final

'''
Given a string and a non-negative int n, return a larger string that is n copies of the original string.

string_times('Hi', 2) → 'HiHi'
string_times('Hi', 3) → 'HiHiHi'
string_times('Hi', 1) → 'Hi'
'''

def front_times(str, n):
  if len(str) < 3:
	return str * n
  else:
	return (str[:3]) * n

'''
Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars, or whatever is there if the string is less than length 3. Return n copies of the front;

front_times('Chocolate', 2) → 'ChoCho'
front_times('Chocolate', 3) → 'ChoChoCho'
front_times('Abc', 3) → 'AbcAbcAbc'
'''

def string_bits(str):
  final = ""
  n = 0
  for i in range(len(str)):
	if i % 2 == 0:
  	final += str[i]
  return final

'''
Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".

string_bits('Hello') → 'Hlo'
string_bits('Hi') → 'H'
string_bits('Heeololeo') → 'Hello'
'''

def string_splosion(str):
  result = ""
  for i in range(len(str)):
	result += str[:i+1]
  return result

'''
Given a non-empty string like "Code" return a string like "CCoCodCode".

string_splosion('Code') → 'CCoCodCode'
string_splosion('abc') → 'aababc'
string_splosion('ab') → 'aab'
'''

def last2(str):
  l2 = str[len(str)-2:]
  counter = 0
  for i in range(len(str)-2):
	if str[i:i+2] == l2:
  	counter += 1
  return counter

'''
Given a string, return the count of the number of times that a substring length 2 appears in the string and also as the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring).

last2('hixxhi') → 1
last2('xaxxaxaxx') → 1
last2('axxxaaxx') → 2
'''

def array_count9(nums):
  counter = 0
  for i in nums:
	if i == 9:
  	counter+=1
  return counter

'''
Given an array of ints, return the number of 9's in the array.

array_count9([1, 2, 9]) → 1
array_count9([1, 9, 9]) → 2
array_count9([1, 9, 9, 3, 9]) → 3
'''

def array_front9(nums):
  end = min(len(nums), 4)
  
  for i in range(end):
      if nums[i] == 9:
          return True
  return False

'''
Given an array of ints, return True if one of the first 4 elements in the array is a 9. The array length may be less than 4.

array_front9([1, 2, 9, 3, 4]) → True
array_front9([1, 2, 3, 4, 9]) → False
array_front9([1, 2, 3, 4, 5]) → False
'''

def array123(nums):
  for i in range(len(nums) - 2):
      if nums[i:i+3] == [1, 2, 3]:
          return True
  return False

'''
Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.

array123([1, 1, 2, 3, 1]) → True
array123([1, 1, 2, 4, 1]) → False
array123([1, 1, 2, 1, 2, 3]) → True
'''

def string_match(a, b):
  min_length = min(len(a), len(b))
  
  count = 0
  
  for i in range(min_length - 1):
      if a[i:i+2] == b[i:i+2]:
          count += 1
  
  return count

'''
Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring. So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both strings.

string_match('xxcaazz', 'xxbaaz') → 3
string_match('abc', 'abc') → 2
string_match('abc', 'axc') → 0
'''
