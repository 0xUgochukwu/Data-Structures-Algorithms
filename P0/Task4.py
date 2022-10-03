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

def isTeleMarketerLine(number):
    if number[:3] == "140":
        return True
    return False

def checkCallReceipts(number):
    for i in range(0, len(calls)):
        if number == calls[i][1]:
            return True
    return False

def checkMessageSendingAndReceipts(number):
    for i in range(0, len(texts)):
        if number == texts[i][0] or number == texts[i][1]:
            return True
    return False

number = ""
telemarketers = []
for i in range(0, len(calls)):
    number = calls[i][0]
    if isTeleMarketerLine(number) and not checkCallReceipts(number) and not checkMessageSendingAndReceipts(number):
        if number not in telemarketers:
            telemarketers.append(number)


telemarketers.sort()

print("These numbers could be telemarketers: ")
for telemarketer in telemarketers:
    print(telemarketer)


# # Check 

# for i in range(0, len(texts)):
#     if texts[i][0] == "1409668775" or texts[i][1] == "1409668775":
#         print("found in texts")

# print("Check done!")

# RUN TIME ANALYSIS
# O(n)
