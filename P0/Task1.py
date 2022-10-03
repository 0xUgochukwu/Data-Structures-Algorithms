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

tel_numbers = []

for i in range(0,len(calls)):
    for j in calls[i][:2]:
        tel_numbers.append(j)
        
for i in range(0,len(texts)):
    for j in texts[i][:2]:
        tel_numbers.append(j)
        
count = len(set(tel_numbers))

print(f"There are {count} different telephone numbers in the records.")



# RUN TIME ANALYSIS
# O(2n**2 + n) 