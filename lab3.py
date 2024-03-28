from enum import *

class Director:
    def __init__(self, first_name: str, last_name: str, birth_year: int, birth_place: str):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year
        self.birth_place = birth_place

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.birth_year} {self.birth_place}'

class Genre(Enum):
    ACTION = 'Action'
    SCI_FI = 'Sci-Fi'
    DRAMA = 'Drama'
    THRILLER = 'Thriller'
    ADVENTURE = 'Adventure'
    FANTASY = 'Fantasy'

class Movie:
    def __init__(self, name: str, year: int, director: Director, rating: float, genre: list(Genre)):
        self.name = name
        self.year = year
        self.director = director
        self.rating = rating
        self.genre = [v.value for v in genre]

    def pretty_print(self):
        print(f'{self.name} ({self.year}), Director of film: {self.director.first_name} {self.director.last_name}, Genre: {", ".join(self.genre)}, Rating - {self.rating}')

d1 = Director("Andrew", "Nikol", 1964, 'New Zeland')
m1 = Movie('Lord of War', 2005, d1, 97.5, [Genre.ACTION, Genre.ADVENTURE])

m1.pretty_print()