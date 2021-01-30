def sorted_merge(left, right):
    merged      = []
    left_index  = 0
    right_index = 0

    # Move through the lists until we have exhausted one
    while left_index < len(left) and right_index < len(right):
        # If left's item is larger, append right's item
        # and increment the index
        if left[left_index] < right[right_index]:
            merged.append(right[right_index])
            right_index += 1
        # Otherwise, append left's item and increment
        else:
            merged.append(left[left_index])
            left_index += 1

    # Append any leftovers. Because we've broken from our while loop,
    # we know at least one is empty, and the remaining:
    # a) are already sorted
    # b) all sort past our last element in merged
    merged += left[left_index:]
    merged += right[right_index:]

    # return the ordered, merged list
    return merged

def mergesort(items):

  if len(items) <= 1:
      return items

  mid   = len(items) // 2
  left  = items[:mid]
  right = items[mid:]

  left  = mergesort(left)
  right = mergesort(right)

  return sorted_merge(left, right)

def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    result          = []
    size_input_list = len(input_list)

    if size_input_list == 1:
      result = [input_list[0], 0]
    elif len(input_list) > 1:
      sorted_input  = mergesort(input_list)
      first_number  = ""
      second_number = ""

      for i in range(size_input_list):
        value = str(sorted_input[i])

        if i % 2 == 0:
          first_number += value
        else:
          second_number += value

      result = [int(first_number), int(second_number)]

    print(result)

    return result

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5],    [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
test_function([[0, 0, 2, 5, 0, 0], [500, 200]])
test_function([[0, 1], [1, 0]])
test_function([[], []])
