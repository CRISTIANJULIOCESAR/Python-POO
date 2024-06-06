# CinemaClass.py

class Cinema:
    def __init__(self, name, address, screenings):
        self.name = name
        self.address = address
        self.screenings = screenings
        self.open = True

    def info(self):
        print(f"Cinema: {self.name} \nAddress: {self.address}")

    def show_screenings(self):
        print("\nToday's available screenings:\n")
        for screening in self.screenings:
            if not screening.finished:
                screening.info()

    def get_seat_status(self, screening_index):
        self.screenings[screening_index].movie.info()
        for seat in self.screenings[screening_index].theater.seats:
            status = "Occupied" if seat.occupied else "Available"
            print(f"{seat.number}{seat.row} Status: {status}")