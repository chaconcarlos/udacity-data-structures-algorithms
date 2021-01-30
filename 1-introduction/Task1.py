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
TASK 1:
How many different telephone numbers are there in the records?
Print a message:
"There are <count> different telephone numbers in the records."
"""
phone_numbers_set = set()

for record in texts:
  phone_numbers_set.add(record[0])
  phone_numbers_set.add(record[1])

for record in calls:
  phone_numbers_set.add(record[0])
  phone_numbers_set.add(record[1])

print("There are {0} different telephone numbers in the records.".format(len(phone_numbers_set)))

# The worst case of my implementation for this task is: O(n). I have to iterate through both lists of calls and texts, and that's 2 not nested "for" loops. That
# would be O(n + n) = O(2n) = O(n). The time complexity for the insertion on a set is constant, O(1).