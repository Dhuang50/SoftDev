def first_last6(nums):
  if len(nums) == 1:
    return nums[0] == 6
  else:
    return nums[0] == 6 or nums[len(nums) - 1] == 6
  
def same_first_last(nums):
  return len(nums) >= 1 and nums[0] == nums[len(nums) -1]

def make_pi():
  return [3, 1, 4]

def common_end(a, b):
  return a[len(a)-1] == b[len(b)-1] or a[0] == b[0]

def sum3(nums):
  sum = 0
  for i in nums:
    sum += i
  return sum

def rotate_left3(nums):
  nums.append(nums.pop(0))
  return nums

def reverse3(nums):
  count = 2
  result = []
  for i in range(3):
    result.append(nums.pop(count))
    count -= 1
  return result

def max_end3(nums):
  m = max(nums[0], nums[len(nums)-1])
  for i in range(len(nums)):
    nums[i-1] = m
  return nums

def sum2(nums):
  return sum(nums[:2])

def middle_way(a, b):
  result = []
  result.append( a[1]) 
  result.append(b[1])
  return result

def make_ends(nums):
  result = []
  result.append(nums[0])
  result.append(nums[len(nums)-1])
  return result

def has23(nums):
  for i in nums:
    if i == 2 or i == 3:
      return True
  return False

