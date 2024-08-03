"""
Find number of days above average temperature.

How many day's temperature? 2
Day 1's high temp: 1
Day 2's high temp: 2

Output:
Average = 1.5
1 day(s) above average
"""

days = int(input('How many day\'s temperature? '))
values = []

for day in range(1, days + 1):
    data = int(input('Day {}\'s high temp: '.format(day)))
    values.append(data)

average = sum(values)/len(values)
print('\nAverage =', average)

above = 0
for value in values:
    if value > average:
        above += 1

print('{} day(s) above average'.format(above))
