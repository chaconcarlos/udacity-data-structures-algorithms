import hashlib
from datetime import datetime

BLOCK_STRING_FORMAT = "{0};{1};{2};{3}"

def calculate_hash(data):
  sha = hashlib.sha256()

  sha.update(data.encode('utf-8'))

  return sha.hexdigest()

class Block:

  def __init__(self, timestamp, data, previous_hash):
    self.timestamp     = timestamp
    self.data          = data
    self.previous_hash = previous_hash

    hashable_data = self.data + str(self.timestamp)

    self.hash = calculate_hash(hashable_data)
    self.next = None

  def get_hash(self):
    return self.hash

  def get_next(self):
    return self.next

  def set_next(self, block):
    self.next = block

  def __repr__(self):
    return BLOCK_STRING_FORMAT.format(str(self.timestamp), self.data, self.hash, self.previous_hash)

class Blockchain:
  def __init__(self):
    self.head = None
    self.tail = None

  def add(self, data):
    if data:
      timestamp = datetime.utcnow()

      if self.head == None:
        new_block = Block(timestamp, data, None)
        self.head = new_block
        self.tail = self.head
      else:
        new_block = Block(timestamp, data, self.tail.get_hash())
        self.tail.set_next(new_block)
        self.tail = new_block

  def to_list(self):
    output_list   = []
    current_block = self.head

    while current_block:
        output_list.append(current_block)
        current_block = current_block.get_next()

    return output_list

#Test 1. Add 4 blocks with valid data.
blockchain_test1 = Blockchain()

blockchain_test1.add("Block 0")
blockchain_test1.add("Block 1")
blockchain_test1.add("Block 2")
blockchain_test1.add("Block 3")

#Expected: Prints the whole blockchain, with 4 blocks.
print("TEST 1 OUTPUT: \n", blockchain_test1.to_list())

#Test 2. Print the blockchain when no blocks were added.
blockchain_test2 = Blockchain()

#Expected: Prints an empty list.
print("TEST 2 OUTPUT: \n", blockchain_test2.to_list())

#Test 3. Call the add() function with None and an empty string as parameter.
blockchain_test3 = Blockchain()

blockchain_test3.add(None)
blockchain_test3.add("")

#Expected: Prints an empty list.
print("TEST 3 OUTPUT: \n", blockchain_test3.to_list())


