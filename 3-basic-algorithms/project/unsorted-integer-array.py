import random
import sys

def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    result = None

    if len(ints) > 0:
      current_min = ints[0]
      current_max = ints[0]

      for i in range(1, len(ints)):
        value = ints[i]

        if value > current_max:
          current_max = value
        elif value < current_min:
          current_min = value

      result = (current_min, current_max)

    print(result)

    return result
## Example Test Case of Ten Integers

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)
print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

## Example Test Case of Ten Integers
l = [0, 0, 10, 1, 2, 9, 9, 9, 9, 0, 1, 9, 4, 6, 21350]
print ("Pass" if ((0, 21350) == get_min_max(l)) else "Fail")

#Example only one element list, 0, Expected: (0, 0)
l = [0]
print ("Pass" if ((0, 0) == get_min_max(l)) else "Fail")

#Example only one element list, 1
l = [1]
print ("Pass" if ((1, 1) == get_min_max(l)) else "Fail")

#Example, empty list, Expected: None.
l = []
print ("Pass" if (None == get_min_max(l)) else "Fail")