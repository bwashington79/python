import datetime as date
currentYear = date.datetime.today().strftime('%Y')

print(currentYear)

print("This program will calculate your age in decades.")
name: str = input("Please provide your name\n")
age: int = input("Please provide your curret age\n")
decades: int = age/100
print(decades)




