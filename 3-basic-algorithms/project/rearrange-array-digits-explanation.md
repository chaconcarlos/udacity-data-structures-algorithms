#Problem 3 (Rearrange Array Elements) solution
Since it's easier to get the max numbers to build the max sum from a sorted list, I used a merge sort first on the list, which matches the required complexity. Then, I built the numbers using its most significant digit first, using the max value on each step. 

The time complexity of my solution **O(nlog(n)),** since I used merge sort to sort the list. Then, the algorithm traverses through the list to build the result.

**O(n log(n) + log(n)) = O(n log(n))**

The space complexity is **O(n)**, since the result contains the same elements as the input list.