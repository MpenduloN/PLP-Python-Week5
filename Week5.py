# Movie Class
class Movie:
    genre = "romantic"  # Class Attribute

    def play(self):
        print("The movie is playing.")

# Creating an Object
my_movie = Movie()
print(my_movie.genre)  # Output: romantic
my_movie.play()        # Output: The movie is playing.

# Another Movie Class with Constructor
class MovieDetails:
    def __init__(self, title, genre, producer):
        self.title = title
        self.genre = genre
        self.producer = producer

# Creating objects with unique attributes
movie1 = MovieDetails("The Secret", "Romantic", "Stephanie")
movie2 = MovieDetails("Action Blast", "Action", "Will")

print(movie1.genre)      # Output: Romantic
print(movie1.producer)   # Output: Stephanie

# Extended Movie Class with methods
class FullMovie:
    def __init__(self, title, genre, producer, year):
        self.title = title
        self.genre = genre
        self.producer = producer
        self.year = year
        self.playing = False

    def start(self):
        if not self.playing:
            self.playing = True
            print(f"Now playing: {self.title} ({self.genre}, {self.producer}, {self.year})")

    def stop(self):
        if self.playing:
            self.playing = False
            print(f"{self.title} has stopped.")

    def show_details(self):
        print("Movie Details:")
        print(f"Title: {self.title}")
        print(f"Genre: {self.genre}")
        print(f"Producer: {self.producer}")
        print(f"Year: {self.year}")

movie3 = FullMovie("Secretary", "Thriller", "Ghosted", 2024)
movie3.show_details()
movie3.start()
movie3.stop()

# Inheritance Example
class RatingMovie(FullMovie):
    def __init__(self, title, genre, producer, year, rating):
        super().__init__(title, genre, producer, year)
        self.rating = rating

rated_movie = RatingMovie("Epic Movie", "Comedy", "Someone", 2023, 4)
print(f"Movie Rating: {rated_movie.rating}")

# Polymorphism Example
class Music:
    def play(self):
        return "Playing music"

class Person:
    def speak(self):
        return "Hi"

# Demonstrating method calling
items = [Music(), Person()]
for item in items:
    if hasattr(item, 'play'):
        print(item.play())
    elif hasattr(item, 'speak'):
        print(item.speak())

# Inheritance with Animal Classes
class Animal:
    def move(self):
        print("Animal is moving")

class Bird(Animal):
    def move(self):
        print("Bird is flying in the sky")

class Dog(Animal):
    def move(self):
        print("Dog is walking in the field")

class Fish(Animal):
    def move(self):
        print("Fish is swimming in the sea")

# Create instances and demonstrate movement
for creature in [Bird(), Dog(), Fish()]:
    creature.move()

input("Press Enter to Exit...")

