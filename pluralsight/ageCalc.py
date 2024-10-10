import datetime as date
currentYear = date.datetime.today().strftime('%Y')

'''
get current year
print(currentYear)
'''

# using conditionals


print("This program will calculate your age in decades.")
name: str = input("Please provide your name\n")
age = int(input("Please provide your current age\n"))
decades: int = age // 10
years: int = age % 10
print("Hello " + name + " you are " + str(decades) +
      " decades AND " + str(years) + " years old!")

temp = int(input("What's the current temp where you are located?\n"))

if temp < 65:
    print(("It's cold!! put on a coat"))
elif temp > 65 or temp < 69:
      print(("You may want to consider a jacket"))

else:
    print("Enjoy the outdoors!")

