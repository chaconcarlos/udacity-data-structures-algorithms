#Problem 3 (Huffman Tree) solution
To solve this problem:
- I used a dictionary to keep count of the occurrences of each character. This was appropiate for that case, since all the required operations (insertion, look up) have a time complexity of O(1).
- A priority queue (based on a doubly linked list) to hold the frequencies queue. I needed the queue to hold a custom node, so this is why I build my own data estructure. The insertion in this priority queue has a worst case time complexity of O(n). Pop a node has a time complexity of O(1).
- I implemented the Huffman tree as specified, as a binary tree. The insertion of a node in the tree is in constant time O(1), since it doesn't required traverse the tree. When encoding, the tree is only traversed once to build the encoding the table. When decoding, the look up for values in the tree has a time complexity of O(n log n), since it's necessary to traverse the tree to lookup the value for each encoded token.
- The encoding table is a dictionary that holds the corresponding value in the tree for each character in the data. As commented previously, since all the required operations (insertion, look up) have a time complexity of O(1).

##Encoding
The total time complexity for the encoding operation could be expressed as the sum of the time complexity for each of the operations necessary for encoding:
**1. Iterate through the input data an calculate the frequencies:** O(n).
**2. Build the Huffman Tree:** In the worst case, the data could have n different characters, so the priority queue would consist of n different nodes that would require to proccess each to build the tree. Because of this, the complexity to build the tree would be O(n) in this case. Insertion in the tree has a complexity of O(1).
**3. Build the encoding table:** Requires to traverse the total elements of the tree, which in the worst case can be expressed as O(n).
**4. Encode the data:** Requires to iterate through every token in the input data and look up their corresponding value in the encoding table (that is a dictionary). The look up is in constant time O(1), so the total time complexity for the operation is O(n).

**Total time complexity for encoding:
O(step 1) + O(step 2) + O(step 3) + O(step 4)  = O(n) + O(n) + O(n) + O(n) = O(4n) = O(n)**

**Total space complexity for encoding: O(n).** This is because the memory use grows linearly with the input size.

##Decoding
To decode, it's necessary to traverse every token of the input, and lookup the value in the tree. Since the searching operation for the binary tree has a time complexity of O(log n), **the time complexity for the decoding operation is O(n log n).**

**Total space complexity for encoding: O(n).** This is because the memory use grows linearly with the input size.