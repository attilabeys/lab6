from functools import reduce
def multi(numbers):
  return reduce(lambda x, y: x * y, numbers)
 
myList = [1, 4,6,3,6,3]
a = multi(myList)
print(a)

    