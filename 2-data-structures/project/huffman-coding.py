import textwrap
import sys

class FrequencyQueueNode:
  """
    Class that represents node in the FrequencyQueue.

    Attributes:
        value: The value the entry has.
        frequency: The frequency.
        data: The data for the node.
        previous: The previous node.
        next: The next node.
  """
  def __init__(self, value, frequency, data):
    """
    Initializes an instance of the FrequencyQueueNode class.

    Args:
      value(str):     The value the entry has.
      frequency(int): The frequency.
      data(object):   The data for the node.
    """
    self.value     = value
    self.frequency = frequency
    self.data      = data
    self.previous  = None
    self.next      = None

  def get_value(self):
    """
    Gets the value of the node.
    """
    return self.value

  def get_frequency(self):
    """
    Gets the frequency of the node.
    """
    return self.frequency

  def get_data(self):
    """
    Gets the data of the node.
    """
    return self.data

  def has_next(self):
    """
    Returns True if the entry has a next entry. Otherwise False.
    """
    return self.next != None

  def get_next(self):
    return self.next

  def set_next(self, node):
    """
    Sets the next node in the list.

    Parameters:
        node (FrequencyQueueNode): The next node in the list.
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
        node (FrequencyQueueNode): The previous node in the list.
    """
    self.previous = node

  def __repr__(self):
    """
    Gets the string representation of the FrequencyQueueNode instance.
    """
    return "'{0}' - {1}".format(self.value, self.frequency)

class FrequencyQueue:
  """
    Class that represents a priority queue of nodes sorted by min frequency. It's implemented as a doubly
    linked list.

    Attributes:
        head: The head of the queue.
        tail: The tail of the queue.
        size: The size of the queue.
  """
  def __init__(self):
    """
    Initializes an instance of the FrequencyQueue class.
    """
    self.head = None
    self.tail = None
    self.size = 0

  def __push_sorted(self, node):
    """
    Pushes a new node on the linked list, placing it sorted by min frequency.

    Parameters:
        node (FrequencyQueueNode): The node to push.
    """
    if node.get_frequency() >= self.tail.get_frequency():
      node.set_previous(self.tail)
      self.tail.set_next(node)
      self.tail = node
    elif node.get_frequency() < self.head.get_frequency():
      self.head.set_previous(node)
      node.set_next(self.head)
      self.head = node
    else:
      current_node = self.head.get_next()

      while current_node:
        if node.get_frequency() < current_node.get_frequency():
          previous_node = current_node.get_previous()
          node.set_previous(previous_node)
          previous_node.set_next(node)
          current_node.set_previous(node)
          node.set_next(current_node)
          break

        current_node = current_node.get_next()

  def get_size(self):
    """
    Gets the size of the queue.
    """
    return self.size

  def push(self, value, frequency, data):
    """
    Pushes a new node on the linked list.

    Parameters:
        node (FrequencyQueueNode): The node to push.
    """
    new_node  = FrequencyQueueNode(value, frequency, data)

    if self.head == None:
      self.head = new_node
      self.tail = self.head
    else:
      self.__push_sorted(new_node)

    self.size += 1

  def pop(self):
    """
    Pops the element with the min frequency of the list.
    """
    node = self.head

    if (self.head):
      self.head  = self.head.get_next()
      self.size -= 1

    return node

  def to_list(self):
    """
    Gets the elements of the queue as a list.
    """
    output_list   = []
    current_node = self.head

    while current_node:
      value     = current_node.get_value()
      frequency = current_node.get_frequency()

      output_list.append((value, frequency))

      current_node = current_node.get_next()

    return output_list


class HuffmanTreeNode():
  """
    Class that represents node in the HuffmanTree.

    Attributes:
        value: The value the entry has.
        frequency: The frequency.
        data: The data for the node.
        previous: The previous node.
        next: The next node.
  """
  def __init__(self, character, value):
      self.value     = value
      self.character = character
      self.left      = None
      self.right     = None

  def get_value(self):
    """
    Gets the value of the node.
    """
    return self.value

  def get_character(self):
    """
    Gets the value of the character.
    """
    return self.character

  def set_left_child(self,left):
    """
    Sets the left child of the node.

    Parameters:
        left (HuffmanTreeNode): The previous node in the list.
    """
    self.left = left

  def set_right_child(self, right):
    """
    Sets the right child of the node.

    Parameters:
        right (HuffmanTreeNode): The previous node in the list.
    """
    self.right = right

  def get_left_child(self):
    """
    Gets the right child of the node.
    """
    return self.left

  def get_right_child(self):
    """
    Gets the right child of the node.
    """
    return self.right

  def has_left_child(self):
    """
    Returns True if the node has a left child. Otherwise, False.
    """
    return self.left != None

  def has_right_child(self):
    """
    Returns True if the node has a right child. Otherwise, False.
    """
    return self.right != None

  def is_leaf(self):
    """
    Returns True if the node is a leaf.
    """
    return not (self.has_left_child() or self.has_right_child())

class HuffmanTree():
  """
    Class that represents a Huffman tree.

    Attributes:
      data: The data to build the tree with.
      root: The root node of the tree.
      encoding_dict: The dictionary with the values for each character in the data.
      encoded_data: The encoded data.
  """
  def __init__(self, data):
    self.data          = data
    self.root          = None
    self.encoding_dict = dict()
    self.encoded_data  = None

    if data is not None:
      self.__load(data)

  def __get_frequencies(self, data):
    """
    Gets the frequencies priority queue from the data.

    Parameters:
        data (str): The data to build the tree with.
    """
    frequency_dict        = dict()
    frequency_sorted_list = FrequencyQueue()

    for token in data:
      if (frequency_dict.get(token) == None):
        frequency_dict[token] = 1
      else:
        frequency_dict[token] = frequency_dict[token] + 1

    for value in frequency_dict:
      node = HuffmanTreeNode(value,frequency_dict[value])
      frequency_sorted_list.push(value, frequency_dict[value], node)

    return frequency_sorted_list

  def __build(self, frequencies):
    """
    Builds the Huffman tree.

    Parameters:
        frequencies (FrequencyQueue): The frequencies priority queue.
    """
    if frequencies.get_size() > 1:
      while frequencies.get_size() > 1:
        first_node  = frequencies.pop()
        second_node = frequencies.pop()

        node_sum = first_node.get_frequency() + second_node.get_frequency()

        new_node = HuffmanTreeNode(None, node_sum)
        new_node.set_left_child(first_node.get_data())
        new_node.set_right_child(second_node.get_data())

        frequencies.push(None, node_sum, new_node)

      if (frequencies.get_size() > 0):
        self.root = frequencies.pop().get_data()
    else:
      node      = frequencies.pop()
      self.root = HuffmanTreeNode(None, node.get_frequency())

      self.root.set_left_child(node.get_data())

  def __build_encoding_table_recursive(self, current_node, current_code):
    """
    Builds the encoding table recursively.

    Parameters:
        current_node (HuffmanTreeNode): The current node of the tree.
        current_code (str): The current code string.
    """
    if current_node.is_leaf():
      character = current_node.get_character()
      self.encoding_dict[character] = current_code
    else:
      if current_node.has_left_child():
        self.__build_encoding_table_recursive(current_node.get_left_child(), current_code + "0")

      if current_node.has_right_child():
        self.__build_encoding_table_recursive(current_node.get_right_child(), current_code + "1")

  def __build_encoding_table(self):
    """
    Builds the encoding table.
    """
    self.__build_encoding_table_recursive(self.root, "")

  def __build_encoded_data(self):
    """
    Builds the encoded data.
    """
    self.encoded_data = ""
    encoded_tokens    = []

    for token in self.data:
      encoded_tokens.append(self.encoding_dict[token])

    self.encoded_data = self.encoded_data.join(encoded_tokens)

  def __load(self, data):
    """
    Loads the data and builds the tree.
    """
    frequencies = self.__get_frequencies(data)

    self.__build(frequencies)
    self.__build_encoding_table()
    self.__build_encoded_data()

  def get_root(self):
    """
    Gets the root node of the tree.
    """
    return self.root

  def get_encoded_data(self):
    """
    Gets the encoded data.
    """
    return self.encoded_data

  def decode(self, encoded_data):
    """
    Decodes data based on the tree.

    Parameters:
      encoded_data (str): The encoded data.

    Returns:
      The decoded data.
    """
    result         = ""
    decoded_tokens = []
    current_index  = 0
    current_node   = self.root
    data_length    = len(encoded_data)
    current_token  = encoded_data[0]

    while current_index <= data_length:
      if (current_node.is_leaf()):
        decoded_tokens.append(current_node.get_character())
        current_node = self.root
      elif current_token == "0":
        current_node = current_node.get_left_child()
        current_index += 1
      else:
        current_node = current_node.get_right_child()
        current_index += 1

      if current_index < data_length:
        current_token  = encoded_data[current_index]

    return result.join(decoded_tokens)


def huffman_encoding(data):
  """
  Encodes a data using a Huffman tree.

  Parameters:
    data (str): The data to encode.
  Returns:
    The encoded data and the Huffman tree instance.
  """
  if (len(data) > 0):
    huffman_tree = HuffmanTree(data)
    return huffman_tree.get_encoded_data(), huffman_tree
  else:
    return None, None


def huffman_decoding(data, tree):
  """
  Decode a data using a Huffman tree.

  Parameters:
    data (str): The data to decode.
    tree (HuffmanTreeNode): The Huffman tree corresponding to the input.
  Returns:
    The decoded data.
  """
  return tree.decode(data)


def run_test(data):
  """
  Runs a test using the given data.

  Parameters:
    data (str): The data to encode/decode.
  """
  print("  INPUT")
  print("  =====")
  print("  The content of the data is: {}".format(data))
  print("  The size of the data is:    {}\n".format(sys.getsizeof(data)))

  encoded_data, tree = huffman_encoding(data)

  if (encoded_data is not None):
    formatted_data = textwrap.wrap(encoded_data, width=120)

    print("  ENCODING")
    print("  ========")
    print("  The size of the encoded data is: {}".format(sys.getsizeof(int(encoded_data, base=2))))
    print("  The content of the encoded data is:")

    for line in formatted_data:
      print("    ", line)

    decoded_data = huffman_decoding(encoded_data, tree)

    print("\n")
    print("  DECODING")
    print("  ========")
    print("  The size of the decoded data is:    {}".format(sys.getsizeof(decoded_data)))
    print("  Is encoded data == decoded data?    {}".format(data == decoded_data))
    print("  The content of the decoded data is: {}\n".format(decoded_data))
    print("\n")
  else:
    print("  No result.\n")


if __name__ == "__main__":
  codes = {}

  #Text input validated with: https://www.dcode.fr/huffman-tree-compression

  print("TEST 1: Regular text.")
  print("=====================\n")

  # This test has a regular text as input.
  # Expected encode: SUCCESS, 1010101010101000100100111111111111111000000010101010101
  # Expected decode: SUCCESS
  run_test("AAAAAAABBBCCCCCCCDDEEEEEE")

  print("TEST 2: Regular text.")
  print("=====================\n")

  # This test has a regular text as input. However, this one has a longer variety of characters and frequencies.
  # Expected encode: SUCCESS, 01111010100010011010110111010101111100001100000111110100111100101001011100000101111000011111010011010
  # Expected decode: SUCCESS
  run_test("SUPERFRAGILISTICOESPIALIDOSO")

  print("TEST 3: Input string len = 2")
  print("============================\n")

  # This test has a regular text with only 2 characters has input.
  # Expected encode: SUCCESS, 01
  # Expected decode: SUCCESS
  run_test("I@")

  print("TEST 4: Long text.")
  print("==================\n")

  # This test has a regular text as input. However, this one has a longer variety of characters and frequencies. Also, mixes symbols, upper and loger characters.
  # Expected encode: SUCCESS
  # Expected decode: SUCCESS
  run_test("One morning when Gregor Samsa woke from troubled dreams he found himself transformed in his bed into a horrible vermin. He lay on his armour-like back, and if he lifted his head a little he could see his brown belly, slightly domed and divided by arches into stiff sections.")

  print("TEST 5: Input string len = 1")
  print("============================\n")

  # This test has a regular text with only 1 character has input.
  # Expected encode: No result.
  # Expected decode: No result.
  run_test("U")

  print("TEST 6: Input string len = 0")
  print("============================\n")

  # This test has an empty text has input.
  # Expected encode: No result.
  # Expected decode: No result.
  run_test("")

  print("TEST 7: Repetitive character ")
  print("============================\n")

  # This test has a string with only one character repeated multiple times.
  # Expected encode: SUCCESS, 0000000000000000000000000000000000000
  # Expected decode: SUCCESS
  run_test("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")


