class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    duplicates_dict = dict()
    union_list      = LinkedList()
    current_node    = llist_1.head

    while current_node != None:
      value = current_node.value

      if duplicates_dict.get(value) == None:
        duplicates_dict[value] = 1
        union_list.append(value)

      current_node = current_node.next

    current_node = llist_2.head

    while current_node != None:
      value = current_node.value

      if duplicates_dict.get(value) == None:
        duplicates_dict[value] = 1
        union_list.append(value)

      current_node = current_node.next

    return union_list


def intersection(llist_1, llist_2):
    duplicates_dict = dict()
    current_node    = llist_1.head
    result_list     = LinkedList()

    while current_node != None:
      value = current_node.value
      duplicates_dict[value] = 1
      current_node = current_node.next

    current_node = llist_2.head

    while current_node != None:
      value = current_node.value

      if duplicates_dict.get(value) != None:
        result_list.append(value)
        del duplicates_dict[value]

      current_node = current_node.next

    return result_list


# Test case 1
# 2 regular lists.

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

#Expected: 3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 21 -> 32 -> 9 -> 1 -> 11
print ("Test case 1 - UNION:        ", union(linked_list_1,linked_list_2))
#Expected: 6 -> 4 -> 21
print ("Test case 1 - INTERSECTION: ", intersection(linked_list_1,linked_list_2))

# Test case 2
# List 1 is empty

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = []
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

#Expected: 1 -> 7 -> 8 -> 9 -> 11 -> 21
print ("Test case 2 - UNION:        ", union(linked_list_3,linked_list_4))
#Expected: Empty list.
print ("Test case 2 - INTERSECTION: ", intersection(linked_list_3,linked_list_4))

# Test case 3
# List 2 is empty

linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = [1,7,8,9,11,21,1]
element_2 = []

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)

#Expected: 1 -> 7 -> 8 -> 9 -> 11 -> 21
print ("Test case 3 - UNION:        ", union(linked_list_5, linked_list_6))
#Expected: Empty list.
print ("Test case 3 - INTERSECTION: ", intersection(linked_list_5, linked_list_6))

# Test case 3
# Both lists are empty.

linked_list_7 = LinkedList()
linked_list_8 = LinkedList()

element_1 = []
element_2 = []

for i in element_1:
    linked_list_7.append(i)

for i in element_2:
    linked_list_8.append(i)

#Expected: Empty list.
print ("Test case 3 - UNION:        ", union(linked_list_7, linked_list_8))
#Expected: Empty list.
print ("Test case 3 - INTERSECTION: ", intersection(linked_list_7, linked_list_8))


