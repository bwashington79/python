expenses = [10.5, 8, 5, 15, 20, 5, 3]

sum = 0

for x in expenses:
    sum = sum + x

print('You spent $', sum, sep = '')

# or

total = sum(expenses)

print(total)