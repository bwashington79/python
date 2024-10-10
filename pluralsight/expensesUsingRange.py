total = 0

expenses = []
num_expenses = input("How man expenses do you need to enter? ")
for i in range(int(num_expenses)):
    expenses.append(float(input("Enter an expense ")))

total = sum(expenses)

print("The sum of all expenses is $", total, sep = '')