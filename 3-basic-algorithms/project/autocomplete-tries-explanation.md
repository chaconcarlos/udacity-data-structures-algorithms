#Problem 5 (Autocomplete with Tries) solution
The time complexity for inserting in the Trie is **O(n)** (where n is the length of the word to insert), since in the worst case it's necessary to traverse all the elements of the input. The space complexity for the insertion is **O(n)** (where n is length of the word to insert).

The time complexity for the look up operation in the Trie is **O(n)** (where n is the length of the word to look up for), since it's also necessary to traverse all the elements of the input. The space complexity for the look operation is **O(1)**.
