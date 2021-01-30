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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

first_text_message_format = "First record of texts, {0} texts {1} at time {2}"
last_call_message_format  = "Last record of calls, {0} calls {1} at time {2}, lasting {3} seconds"
first_text                = texts[0]
first_text_message        = first_text_message_format.format(first_text[0], first_text[1], first_text[2])
last_call                 = calls[len(calls) - 1]
last_call_message         = last_call_message_format.format(last_call[0], last_call[1], last_call[2], last_call[3])

print(first_text_message)
print(last_call_message)

# The worst case of my implementation for this task is: O(1). Both lookup operations are constant, as the get item operation
# for a list in Python is O(1)