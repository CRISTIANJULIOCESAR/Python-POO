# MovieClass.py

class Movie:
    def __init__(self, name, description, genre, duration):
        self.name = name
        self.description = description
        self.genre = genre
        self.duration = duration

    def info(self):
        print(f"Movie: {self.name} \nDescription: {self.description} \nGenre: {self.genre} \nDuration: {self.duration}")