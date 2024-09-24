import datetime as date
currentYear = date.datetime.today().strftime('%Y')

'''
get current year
print(currentYear)
'''

print("This program will calculate your age in decades.")
name: str = input("Please provide your name\n")
age = int(input("Please provide your current age\n"))
decades: int = age // 10
years: int = age % 10
print("Hello " + name + " you are " + str(decades) + " decades AND " + str(years) + " years old!")
