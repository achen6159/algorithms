values = [3, 93, 1, 20, 0, 7, 12, 17]

# iterate over a list with a for loop
''' print each item '''
for v in values:
    print(v)
print()

# count items in a list
def count_evens(nums):
    count = 0
    
    for n in nums:
        if n % 2 == 0:
            count += 1

    return count

# sum items in a list
''' sum is a built-in python function, don't do this '''
def sum(nums):
    total = 0

    for n in nums:
        total += n

    return total

# find the average value in a list
def mean(nums):
    return sum(nums) / len(nums)

# determine if a list has a value
def find(nums, value):
    for n in nums:
        if n == value:
            return True

    return False

# determine the max or min value in a list
''' this is also a built-in python function '''
def min(nums):
    low = nums[0]

    for n in nums:
        if n < low:
            low = n

    return low

def max(nums):
    high = nums[0]

    for n in nums:
        if n > high:
            high = n

    return high 

# test functions
num_evens = count_evens(values)
print(num_evens)
print()

total = sum(values)
print(total)
print()

avg = mean(values)
print(avg)
print()

has_four = find(values, 4)
print(has_four)
has_twenty = find(values, 20)
print(has_twenty)
print()

small = min(values)
print(small)
print()

big = max(values)
print(big)
print()
