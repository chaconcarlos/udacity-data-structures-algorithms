"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
no_telemarketers       = set()
possible_telemarketers = set()

for record in calls:
  caller_number   = record[0]
  receiver_number = record[1]

  no_telemarketers.add(receiver_number)
  possible_telemarketers.discard(receiver_number)

  if (caller_number in no_telemarketers) == False:
    possible_telemarketers.add(caller_number)

for record in texts:
  sender_number   = record[0]
  receiver_number = record[1]

  no_telemarketers.add(sender_number)
  no_telemarketers.add(receiver_number)
  possible_telemarketers.discard(sender_number)
  possible_telemarketers.discard(receiver_number)

print("These numbers could be telemarketers: ")

for number in sorted(possible_telemarketers):
  print(number)

#The worst case complexity for this task would be O(n log n). The first loops to iterate and get the information in the set and the variables is O(2n). The ordering would be O(n log n), and the printing
# would be O(n).
# For the whole task O(2n + n log n + n) = O(3n + n log n). Simplified, would be O(n log n), because O(n log n) is bigger in orders of magnitude than O(3n).