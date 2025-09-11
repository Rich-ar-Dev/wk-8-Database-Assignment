# Assignment 1: Design Your Own Class! 🏗️

# Base Class: Book
class Book:
    def __init__(self, title, author, pages, genre):
        self.title = title
        self.author = author
        self.pages = pages
        self.genre = genre

    def read(self):
        print(f"Reading '{self.title}' by {self.author} 📖")

    def info(self):
        print(f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}, Genre: {self.genre}")


# Subclass: EBook (inherits from Book)
class EBook(Book):
    def __init__(self, title, author, pages, genre, file_size):
        super().__init__(title, author, pages, genre)
        self.file_size = file_size  # in MB

    # Polymorphism: overriding info() method
    def info(self):
        print(f"[E-Book] Title: {self.title}, Author: {self.author}, Pages: {self.pages}, "
              f"Genre: {self.genre}, File Size: {self.file_size}MB")

    def download(self):
        print(f"Downloading '{self.title}'... 💾")


# Example usage
book1 = Book("1984", "George Orwell", 328, "Dystopian")
book1.info()
book1.read()

ebook1 = EBook("Python Basics", "Jane Doe", 250, "Education", 5)
ebook1.info()
ebook1.download()
