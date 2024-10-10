expenses = [10.5, 8, 5, 15, 20, 5, 3]

intSum = 0

for x in expenses:
    intSum = intSum + x

print('You spent $', intSum, sep = '')

# or

total = sum(expenses)

print(total)