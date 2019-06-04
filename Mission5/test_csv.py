import csv
import datetime
csv_file = csv.reader(open('test.csv', 'r'))
print csv_file
i = 0
for item in csv_file:
    if i == 0:
        print item
    str1 = ' '.join(item[0].split())
    # if "Process" in str1 or "Connection" in str1:
    #     print str1
    i += 1