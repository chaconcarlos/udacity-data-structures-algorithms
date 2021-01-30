#Problem 4 (Active Directory) solution
To solve this problem, I just used simple recursion. The time complexity would be O(n), being n the total number of users in the tree. For the worst case, the algorythm would have to iterate through all the users in every group.

Being n the number of groups, and g the toal number of groups inside each group, the time complexity could be described as:

**O(g1 + g2 + g3 + ... + gn) = O(gn) = O(n)**

The total **space complexity is O(n).**