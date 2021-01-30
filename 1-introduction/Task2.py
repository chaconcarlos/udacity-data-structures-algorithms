"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".
"""

time_on_phone_list = dict()
longest_duration   = 0
longest_caller     = str()

for record in calls:
  caller_number    = record[0]
  receiver_number  = record[1]
  duration_seconds = int(record[3])

  if (caller_number in time_on_phone_list):
    time_on_phone_list[caller_number] = time_on_phone_list[caller_number] + duration_seconds
  else:
    time_on_phone_list[caller_number] = duration_seconds

  if (receiver_number in time_on_phone_list):
    time_on_phone_list[receiver_number] = time_on_phone_list[receiver_number] + duration_seconds
  else:
    time_on_phone_list[receiver_number] = duration_seconds

  caller_total_time   = time_on_phone_list[caller_number]
  receiver_total_time = time_on_phone_list[receiver_number]

  if (caller_total_time > longest_duration):
    longest_duration = caller_total_time
    longest_caller   = caller_number

  if (receiver_total_time > longest_duration):
    longest_duration = receiver_total_time
    longest_caller   = receiver_number

print("{0} spent the longest time, {1} seconds, on the phone during September 2016.".format(longest_caller, longest_duration))

# The worst case of my implementation for this task is: O(n). I only need to iterate through the list of calls once.
# The time complexity for the insertion and item lookup on a dict is constant, O(1).