#Problem 2 (Search in a Rotated Sorted Array) solution
I used binary search for both finding the pivot and the search, since it reduces the search space and matches the required time complexity. Also, can be used in place.

The time complexity of my solution O(log(n)), since I used binary search to search the pivot, and also used the same binary search to get the index of the value from the resulting list, which can be expressed:

**O(log(n) + log(n)) = O(log(n))**

The space complexity is **O(1)**, since the search is done in place, and no additional space is required. The search is done in constant space.