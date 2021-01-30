def find_pivot(input_list):
  pivot      = 0
  input_size = len(input_list)

  if input_size == 0:
    pivot = -1
  elif input_size > 1:
    first_element = input_list[0]
    upper_bound   = input_size - 1
    lower_bound   = 0

    while upper_bound >= lower_bound:
      offset = (upper_bound - lower_bound) // 2
      center = lower_bound + offset
      value  = input_list[center]

      if value < first_element:
        previous_value = input_list[center - 1]

        if previous_value > value:
          pivot = center
          break
        else:
          upper_bound = center
      elif value > first_element:
        lower_bound = center

  return pivot

def find_element(input_list, lower_bound, upper_bound, target):
  result = -1

  if target <= input_list[upper_bound]:

    while lower_bound <= upper_bound:
      center_index = (lower_bound + upper_bound) // 2
      center_value = input_list[center_index]

      if target == center_value:
        result = center_index
        break
      elif target < center_value:
        upper_bound = center_index - 1
      elif target > center_value:
        lower_bound = center_index + 1

  return result

def rotated_array_search(input_list, target):
  """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
      int: Index or -1
  """
  result     = -1
  input_size = len(input_list)

  if input_size == 1 and input_list[0] == target:
    result = 0
  elif input_size > 1:
    pivot = find_pivot(input_list)

    print(input_list, " pivot is: ", pivot)

    if target < input_list[0]:
      result = find_element(input_list, pivot, input_size - 1, target)
    else:
      result = find_element(input_list, 0, pivot - 1, target)

  return result

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

# Normal list, expected found, Pass
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
# Normal list, expected found, Pass
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
# Normal list, expected found, Pass
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
# Normal list, expected found, Pass
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
# Normal list, expected found, Pass
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
# One element list, expected -1, Pass
test_function([[6], 10])
# One element list, expected found, Pass
test_function([[6], 6])
# Empty list, expected -1, Pass
test_function([[], 6])
# Empty list, None target, expected -1, Pass
test_function([[], None])