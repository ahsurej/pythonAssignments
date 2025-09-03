# Parent class
class Book:
    def __init__(self, title, author, pages):
        self.title = title         # public attribute
        self._author = author      # protected attribute
        self.__pages = pages       # private attribute

    def read(self):
        print(f"Reading '{self.title}' by {self._author}.")

    def get_pages(self):
        return self.__pages

# Child class inheriting from Book
class ComicBook(Book):
    def __init__(self, title, author, pages, illustrator):
        super().__init__(title, author, pages)
        self.illustrator = illustrator

    def read(self):
        print(f"Reading comic '{self.title}' illustrated by {self.illustrator}.")

# Creating objects
book1 = Book("1984", "George Orwell", 328)
comic1 = ComicBook("Spider-Man", "Stan Lee", 45, "Steve Ditko")

# Using methods
book1.read()
comic1.read()
print("Comic pages:", comic1.get_pages())  # Encapsulation example
