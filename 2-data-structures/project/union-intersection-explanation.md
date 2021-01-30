#Problem 6 (Union and Intersection) solution
For this problem, I used on both cases a dictionary to "mark" the nodes as visited. First, for the union, the dictionary was used to prevent duplicates. For the intersection, it was used to keep the check the values from the first list that match the second.

##Time complexity for union
The time complexity for the union implementation would be **O(n1 + n2) = O(n)**, being n1 the number of elements on the first list, and n2 the elements on the second list. This means that in the worse case, the algorithm would iterate through all the elements in both lists.

Considering that for each element of the first list there is a look up in the and an insertion in the dictionary, and also an insertion in a linked list, and that both these operations are done in constant time O(1), the cycle for the first list is still O(n1). Same applies for the second list.

    while current_node != None:
      value = current_node.value

      if duplicates_dict.get(value) == None:
        duplicates_dict[value] = 1
        union_list.append(value)

      current_node = current_node.next
      
**Space complexity for union is O(n).**
##Time complexity for intersection
The time complexity for the intersection implementation would be **O(n1 + n2) = O(n),** being n1 the number of elements on the first list, and n2 the elements on the second list. This means that in the worse case, the algorithm would iterate through all the elements in both lists.

Considering that for each element of the first list there is an insertion in the dictionary, that is done in constant time, the complexity for the first cycle would be O(n1).

    current_node    = llist_1.head

    while current_node != None:
      value = current_node.value
      duplicates_dict[value] = 1
      current_node = current_node.next

For the iteration through the elements in the second list, for each element there's a look up and a delete operation in the dictionary, and an insertion in a linked list. There operations are done in constant time, O(1), keeping the time complexity of the second cycle on O(n2).

    current_node = llist_2.head

    while current_node != None:
      value = current_node.value

      if duplicates_dict.get(value) != None:
        result_list.append(value)
        del duplicates_dict[value]

      current_node = current_node.next
 
**Space complexity for intersection is O(n).**