#Problem 1 (LRU Cache) solution
To solve this problem, I implemented the LRU cache following the requirements:
<ul>
<li>The LRU has a given capacity.</li>
<li>When the capacity is reached, the least used element has to be deleted.</li>
<li>The time complexity for the put, get and remove should be O(1).</li>
<li>Find a way to quickly mark and identify when an element was recently used, and update the cache.</li>
</ul>

## Code walkthrough
The code consists in 2 classes:
<ul>
<li>LRUCacheEntry: Represents an entry in the cache. Keeps the value, the key and node navigation.</li>
<li>LRUCache: Represents the LRU cache, with its corresponding operations. The LRUCache class is basically a doubly linked list.</li>
</ul>

I used a doubly linked list given the requirements that the time complexity for its insertion is  O(1). In this case, the elements are inserted in the head (like a queue) making the least recently used element to be the tail of the list. Removing the tail of the least has a time complexity of O(1), since it's not necessary to iterate on the list to get to the final element.

Additionally, I used a dictionary as way to speed up the look up for the elements of the LRU cache. The dictionary uses the cache's keys as its own keys, and for each element holds a reference to its corresponding node in the cache linked list. The time complexity for the get item operation for the Dictionary is O(1). Also, the delete item operation also has a time complexity of O(1).

**The space complexity for the LRU implementation is O(n), being n the number of elements in the structure.**

###Putting elements in the cache
As can be seen in the **put** function in the **LRUCache** class, the elements are being inserted by the head, being the tails the least used element.

	def put(self, key, value):
	    """
	    Creates a new entry in the cache.

	    Parameters:
	        key: The key for the entry.
	        value: The value the entry has.
	    """
	    new_entry = LRUCacheEntry(key, value)

	    if self.elements_root == None:
	      self.elements_root = new_entry
	      self.elements_tail = self.elements_root
	    else:
	      new_entry.set_next(self.elements_root)
	      self.elements_root.set_previous(new_entry)
	      self.elements_root = new_entry

	    self.elements_dict[key] = new_entry
	    self.elements_count += 1
	    self.maintain_capacity()

After putting an element in the cache, the **maintain_capacity** function is called, which checks if the cache is above the capacity set. If the cache it's over its capacity, the tail of the linked list is removed.

    def maintain_capacity(self):
	    """
	    Checks if the size is larger than capacity and removes the
	    least recently used element.
	    """
	    if self.size() > self.capacity:
	      lru_node = self.elements_tail

	      del self.elements_dict[lru_node.get_key()]

	      self.elements_tail = self.elements_tail.get_previous()
	      self.elements_count -= 1
	      self.elements_tail.set_next(None)

###Updating a recently used entry
When an element if recovered from the cache using the **get** function, the node corresponding to its key is get from the dictionary. After that, the element is moved to the top of the linked list, to signal that is the item that has been more recently used.

	def get(self, key):
	    """
	    Gets the value of an entry in the cache.
	    """
	    node  = self.elements_dict.get(key)
	    value = -1

	    if node != None:
	      self.move_to_top(node)
	      value = node.get_value()

	    return value

The **move_to_top**  function sets the node recently queried as the root of the list. Also, checks if the element was the tail, so it also can be reassigned.

    def move_to_top(self, node):
	    """
	    Moves a node to the top of the list.

	    Parameters:
	      node (LRUCacheEntry): The node to move to the top.
	    """
	    if node.has_previous():
	      previous = node.get_previous()
	      previous.set_next(node.get_next())

	      if self.elements_tail is node:
		self.elements_tail = previous

	      node.previous = None
	      node.set_next(self.elements_root)

	      self.elements_root = node

##Test cases
- **test_incorrect_capacity_value_error:** Tests that a ValueError exception is thrown when a capacity < 1 is set.

-  **test_put_when_capacity_not_reached:** Tests the insertion in the cache when the capacity has not been exceeded.

- **test_put_capacity_reached:** Tests the insertion in the cache when the capacity has been exceeded.

- **test_move_to_top:** Tests that getting the least recently used element and getting it puts it on top of the list.