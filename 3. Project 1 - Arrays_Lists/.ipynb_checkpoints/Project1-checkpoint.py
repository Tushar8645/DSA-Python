# Calculate Average Temperature

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
