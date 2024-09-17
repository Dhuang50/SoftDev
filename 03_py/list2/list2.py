def count_evens(nums):
  counter = 0
  for i in nums:
    if i%2 == 0:
      counter += 1
  return counter

def big_diff(nums):
  Mi = nums[0]
  Ma = nums[0]
  for i in nums:
    Mi = min(i, Mi)
    Ma = max(i, Ma)
  return Ma - Mi

def centered_average(nums):
  Mi = nums[0]
  Ma = nums[0]
  for i in nums:
    Mi = min(i, Mi)
    Ma = max(i, Ma)
  nums.pop(nums.index(Mi))
  nums.pop(nums.index(Ma))
  return sum(nums[:])/len(nums)

def sum13(nums):
  if len(nums) == 0:
    return 0
  sum = 0
  for i in range(len(nums)):
    sum += nums[i]
    if nums[i] == 13 and i != len(nums)-1 :
      sum -= 13
      if nums[i+1] != 13:
        sum -= nums[i+1]
    elif nums[i] == 13 and i == len(nums)-1:
      sum -= 13
  return sum

def sum67(nums):
  if len(nums) == 0:
    return 0
  else:
    sum = 0
    add = True
    for i in nums:
      if i == 6:
        add = False
      if add:
        sum += i
      if i == 7 and not add:
        add = True
    return sum
        

def has22(nums):
  for i in range(len(nums)-1):
    if nums[i] == 2 and nums[i+1] == 2:
      return True
  return False

