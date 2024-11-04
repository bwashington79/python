moviesAndShowtimes = {'The Matrix': "3:00 pm",
          'The Matrix Reloaded': "6:00 PM",
          'The Matrix Revolutions': "8:00 PM"} 


print("The current movies showing are...\n")
for x in moviesAndShowtimes:
    print(x)

movieSelection = input("\nWhat movie do you want showtimes for? ")

while moviesAndShowtimes.get(movieSelection) == None:
    movieRetry  = input("Please enter a valid movie ")
    if moviesAndShowtimes.get(movieRetry):
        print(movieRetry + " begins at " + moviesAndShowtimes.get(movieRetry))
        break

