#Problem 7 (HTTPRouter using a Trie) solution
The time complexity for inserting in the Trie is **O(n)** (where n is the length of the path to insert), since in the worst case it's necessary to traverse all the elements of the input. The space complexity for the insertion is **O(n)** (where n is the number of parts in the path to insert).

The time complexity for the look up operation in the Trie is **O(n)** (where n is the length of the word to look up for), since it's also necessary to traverse all the elements of the input. The space complexity for the look operation is **O(1)**.

