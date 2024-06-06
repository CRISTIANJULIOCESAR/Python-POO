# ScreeningClass.py

class Screening:
    def __init__(self, movie, theater, schedule):
        self.movie = movie
        self.theater = theater
        self.schedule = schedule
        self.started = False
        self.finished = False

    def info(self):
        print(f"Movie: {self.movie.name}, Theater: {self.theater.name}, Type: {self.theater.type}, Schedule: {self.schedule}")

    def occupy_seat(self, seat_index):
        self.theater.seats[seat_index].mark_occupied()

    def start_screening(self):
        self.started = True

    def finish_screening(self):
        self.finished = True