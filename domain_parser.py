# test.py
from datetime import datetime as dt

f = open('domains.txt')
lines = f.readlines()

dates = []
for line in lines:
    line = line.split(';')
    # Domain, date.
    datestr = line[2].strip('"')
    domain = line[0].strip('"')
    datetime_obj = dt.strptime(datestr, '%Y-%m-%d')
    dates.append([datetime_obj, domain])

    # Line to print.
sorted_pairs = sorted(dates)
for pair in sorted_pairs:
    print "Expiring on " + dt.strftime(pair[0], '%Y-%m-%d') + ": " + pair[1]
