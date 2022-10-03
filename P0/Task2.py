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

longest_time = 0
tel_number = ""



for i in range(0, len(calls)):
    if int(calls[i][3]) > longest_time:
        longest_time = int(calls[i][3])
    

for i in range(0, len(calls)):
    if calls[i][3] == str(longest_time):
        tel_number = calls[i][1]
        
print(f"{tel_number} spent the longest time, {longest_time} seconds, on the phone during September 2016.")


# RUN TIME ANALYSIS
# O(2n)
