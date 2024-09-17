def string_times(str, n):
  final = ""
  for i in range(n):
    final += str
  return final

def front_times(str, n):
  if len(str) < 3:
    return str * n
  else:
    return (str[:3]) * n
  
def string_bits(str):
  final = ""
  n = 0
  for i in range(len(str)):
    if i % 2 == 0:
        final += str[i]
    return final

def string_splosion(str):
    result = ""
    for i in range(len(str)):
       result += str[:i+1]
    return result

def last2(str):
   l2 = str[len(str)-2:]
   counter = 0
   for i in range(len(str)-2):
    if str[i:i+2] == l2:
       counter += 1
    return counter

def array_count9(nums):
    counter = 0
    for i in nums:
       if i == 9:
         counter+=1
    return counter

def array_front9(nums):
  if len(nums) < 4:
    for i in nums:
      if i == 9:
        return True
    return False
  else:
    for i in range(4):
      if nums[i] == 9:
        return True
  return False

def array123(nums):
  for i in range(len(nums) - 2):
    if nums[i] == 1 and nums[i+1] == 2 and nums[i+2] == 3:
      return True
  return False

def string_match(a, b):
  count = 0
  for i in range(min(len(a), len(b))-1):
    if a[i:i+2] == b[i:i+2]:
      count += 1
  return count

