# main.py

from SeatClass import Seat
from TheaterClass import Theater
from MovieClass import Movie
from ScreeningClass import Screening
from CinemaClass import Cinema


# Creating seats
seatA1 = Seat("A", 1)
seatA2 = Seat("A", 2)
seatA3 = Seat("A", 3)
seatB1 = Seat("B", 1)
seatB2 = Seat("B", 2)
seatB3 = Seat("B", 3)

# Creating seat list
seats = [seatA1, seatA2, seatA3, seatB1, seatB2, seatB3]

# Creating theaters
theater1 = Theater("Theater A1", "Regular", seats)
theater2 = Theater("Theater A2", "VIP", seats)
theater3 = Theater("Theater A3", "3D", seats)

# Creating movies
movie1 = Movie("Inception", "A skilled thief enters people's dreams to steal valuable information.", "Sci-Fi, Action, Thriller", "2 hours 28 minutes")
movie2 = Movie("Jurassic Park", "A dinosaur-themed park turns chaotic when the dinosaurs escape.", "Sci-Fi, Action, Adventure", "2 hours 7 minutes")

# Creating screenings
screening1 = Screening(movie1, theater1, "12:00PM")
screening2 = Screening(movie2, theater2, "12:00PM")
screening3 = Screening(movie1, theater3, "12:00PM")
screening4 = Screening(movie2, theater3, "02:00PM")

# Creating screening list
screenings = [screening1, screening2, screening3, screening4]

# Creating cinema
cinema = Cinema("Cinépolis Diana", "Paseo Reforma", screenings)

# Using cinema functions
cinema.info()
cinema.show_screenings()

cinema.screenings[0].finish_screening()
cinema.show_screenings()

print("____________________________________________")
cinema.get_seat_status(0)

cinema.screenings[0].occupy_seat(0)
cinema.screenings[0].occupy_seat(3)
cinema.screenings[0].occupy_seat(4)

cinema.get_seat_status(0)