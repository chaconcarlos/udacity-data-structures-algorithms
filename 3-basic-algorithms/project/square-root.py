import math

def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    result = 0

    if number < 0:
      raise ValueError("'number' must be equals or greater than 0.")

    if number == 0:
      result = 0
    elif number == 1:
      result = 1
    else:
      lower_bound = 0
      upper_bound = number
      value       = 0

      while value != number:
        offset = (upper_bound - lower_bound) / 2
        center = lower_bound + offset
        value  = math.floor(center * center)

        if value > number:
          upper_bound = center
        elif value < number:
          lower_bound = center
        else:
          result = math.floor(center)
          break

    return result

# Regular number, 9. expected = 3
print ("Pass" if  (3 == sqrt(9)) else "Fail")
# 0, expected = 0
print ("Pass" if  (0 == sqrt(0)) else "Fail")
# 1, expected = 1
print ("Pass" if  (1 == sqrt(1)) else "Fail")
# Regular number, 4, expected = 16
print ("Pass" if  (4 == sqrt(16)) else "Fail")
# Regular number, 27, expected = 5
print ("Pass" if  (5 == sqrt(27)) else "Fail")
# Long number, 505652, expected = 711
print ("Pass" if  (711 == sqrt(505652)) else "Fail")

# Negative number, expected ValueError
try:
  sqrt(-1)
except ValueError as exception:
  print(exception)
