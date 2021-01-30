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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

TELEMARKETER_CODE       = "140"
FIXED_AREA_CODE_START   = "("
FIXED_AREA_CODE_END     = ")"
MOBILE_NUMBER_SEPARATOR = " "
BANGALORE_AREA_CODE     = "080"
MOBILE_CODE_SIZE        = 4

def is_fixed(phone_number):
  return phone_number.startswith(FIXED_AREA_CODE_START)

def get_area_code(phone_number):
  """Returns the area code for a fixed phone number."""
  if (is_fixed(phone_number) == False):
    raise ValueError("Number {0} is not a fixed number.".format(phone_number))

  return phone_number[1 : phone_number.find(FIXED_AREA_CODE_END)]

def is_from_area_code(phone_number, expected_area_code):
  """Returns True if the phone belongs to the given area code. Otherwise, false."""
  area_code = get_area_code(phone_number)
  return area_code == expected_area_code

def is_telemarketer(phone_number):
  """Returns True if the phone is by a telemarketer. Otherwise, false."""
  return phone_number.startswith(TELEMARKETER_CODE)

def is_mobile(phone_number):
  """Returns True if the phone is a mobile. Otherwise, false."""
  clean_phone_number = phone_number.strip(MOBILE_NUMBER_SEPARATOR)
  result             = False

  if (len(clean_phone_number) > 1):
    result = MOBILE_NUMBER_SEPARATOR in clean_phone_number

  return result

def get_mobile_code(phone_number):
  """Returns the mobile code for a mobile phone number."""
  if (is_mobile(phone_number) == False):
    raise ValueError("Number {0} is not a mobile number.".format(phone_number))

  return phone_number[0 : MOBILE_CODE_SIZE]

codes_set                   = set()
total_bangalore_calls       = 0
total_inner_bangalore_calls = 0

for record in calls:
  caller_number   = record[0]
  receiver_number = record[1]

  if (is_fixed(caller_number) == False):
    continue
  elif (is_from_area_code(caller_number, BANGALORE_AREA_CODE) == False):
    continue

  total_bangalore_calls = total_bangalore_calls + 1

  if is_fixed(receiver_number) == True and is_from_area_code(receiver_number, BANGALORE_AREA_CODE) == True:
    total_inner_bangalore_calls = total_inner_bangalore_calls + 1

  if is_mobile(receiver_number) == True:
    mobile_code = get_mobile_code(receiver_number)
    codes_set.add(mobile_code)
  elif is_telemarketer(receiver_number) == True:
    codes_set.add(TELEMARKETER_CODE)
  else:
    area_code = get_area_code(receiver_number)
    codes_set.add(area_code)

for code in sorted(codes_set):
  print(code)

percentage_inner_bangalore_calls = total_inner_bangalore_calls / total_bangalore_calls * 100

print("{0:.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(percentage_inner_bangalore_calls))

#The worst case complexity for this task would be O(n log n). The first loop to iterate and get the information in the set and the variables is O(n). The ordering would be O(n log n), and the printing
# would be O(n).
# For the whole task O(n + n log n + n) = O(2n + n log n). Simplified, would be O(n log n), because O(n log n) is bigger in orders of magnitude than O(2n).