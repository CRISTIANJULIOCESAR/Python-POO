# SeatClass.py

class Seat:
    def __init__(self, row, number):
        self.row = row
        self.number = number
        self.occupied = False

    def mark_occupied(self):
        self.occupied = True
   

   