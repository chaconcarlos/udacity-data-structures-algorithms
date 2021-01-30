from collections import deque

class LRUCacheEntry:
  """
    Class that represents a cache entry.

    Attributes:
        key: The key for the entry.
        value: The value the entry has.
  """

  def __init__(self, key, value):
    self.key      = key
    self.value    = value
    self.next     = None
    self.previous = None

  def get_key(self):
    """
    Gets the key for the node.
    """
    return self.key

  def get_value(self):
    """
    Gets the value for the node.
    """
    return self.value

  def has_next(self):
    """
    Returns True if the entry has a next entry. Otherwise False.
    """
    return self.next != None

  def get_next(self):
    """
    Gets the next node in the list.
    """
    return self.next

  def set_next(self, node):
    """
    Sets the next node in the list.

    Parameters:
        node (LRUCacheEntry): The next node in the list.
    """
    self.next = node

  def has_previous(self):
    """
    Returns True if the entry has a previous entry. Otherwise False.
    """
    return self.previous != None

  def get_previous(self):
    """
    Gets the previous node in the list.
    """
    return self.previous

  def set_previous(self, node):
    """
    Sets the previous node in the list.

    Parameters:
        node (LRUCacheEntry): The previous node in the list.
    """
    self.previous = node

class LRUCache(object):
  """
    Class that represents a Least Recently Used (LRU) cache.

    Attributes:
        elements_dict (dict): The dictionary with the cached elements.
        elements_root (LRUCacheNode): The root node.
        elements_tail (LRUCacheNode): The tail node.
        elements_count (int): The number of elements in the list.
  """

  def __init__(self, capacity):
    if capacity < 1:
      raise ValueError("Capacity must be at least 1.")

    self.elements_dict = {}
    self.elements_root = None
    self.elements_tail = None
    self.elements_count = 0
    self.capacity = capacity

  def size(self):
    return self.elements_count

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

def test_incorrect_capacity_value_error():
  #Tests that a ValueError exception is thrown when a capacity < 1 is set.
  #Expected: Value error exception.
  try:
    cache = LRUCache(0)

    if cache != None:
      raise AssertionError("Expected ValueError for capacity = 0, none was thrown.")
  except ValueError:
    pass
  except AssertionError:
    raise
  except BaseException as exception:
    raise AssertionError("Expected ValueError for capacity = 0, but {0} was thrown: {1}".format(type(exception), exception))

def test_put_when_capacity_not_reached():
  #Tests that a ValueError exception is thrown when a capacity < 1 is set.
  #Expected: Success. A LRU with 4 elements is created. All the elements correspond to the ones inserted.
  expected_cache_size = 4
  cache = LRUCache(5)

  for i in range(1, 5):
    cache.put(i, i)

  assert cache.size() == expected_cache_size, "Wrong cache size. Expected {0}, Actual: {1}".format(expected_cache_size, cache.size())

  for i in range(1, 5):
    assert cache.get(i) == i, "Wrong value for element {0}. Expected {1}, Actual: {2}".format(i, i, cache.get(i))

def test_put_capacity_reached():
#Tests that a ValueError exception is thrown when a capacity < 1 is set.
#Expected: Success. A LRU with 5 elements is created. All the elements correspond to the ones inserted.
#          The least used element (the first one inserted) is deleted.
  expected_cache_size = 5
  cache = LRUCache(5)

  for i in range(1, 6):
    cache.put(i, i)

  cache.put(6, 6)

  assert cache.size() == expected_cache_size, "Wrong cache size. Expected {0}, Actual: {1}".format(expected_cache_size, cache.size())
  assert cache.get(1) == -1, "Wrong value for element {0}. Expected {1}, Actual: {2}".format(1, -1, cache.get(1))

  for i in range(2, 7):
    assert cache.get(i) == i, "Wrong value for element {0}. Expected {1}, Actual: {2}".format(i, i, cache.get(i))

def test_move_to_top():
#Tests that getting the least recently used element and getting it puts it on top of the list.
#Expected: Success. A LRU with 5 elements is created. All the elements correspond to the ones inserted.
#          The least used element (the second one inserted, since the first one is get from the LRU) is deleted.
  expected_cache_size = 5
  cache = LRUCache(5)

  for i in range(1, 6):
    cache.put(i, i)

  assert cache.get(1) ==  1, "Wrong value for element {0}. Expected {1}, Actual: {2}".format(1, 1, cache.get(1))

  cache.put(6, 6)

  assert cache.size() == expected_cache_size, "Wrong cache size. Expected {0}, Actual: {1}".format(expected_cache_size, cache.size())
  assert cache.get(1) ==  1, "Wrong value for element {0}. Expected {1}, Actual: {2}".format(1, 1, cache.get(1))
  assert cache.get(2) == -1, "Wrong value for element {0}. Expected {1}, Actual: {2}".format(2, -1, cache.get(2))

test_put_when_capacity_not_reached()
test_put_capacity_reached()
test_move_to_top()

print("success!")