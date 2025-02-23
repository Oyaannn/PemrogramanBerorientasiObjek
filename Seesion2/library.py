class Book:
    def __init__(self, title, author, ISBN):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.available = True

    def borrow_book(self):
        if self.available:
            self.available = False
            return f"You have borrowed {self.title} by {self.author}."
        else:
            return f"{self.title} by {self.author} is not available."

    def return_book(self):
        if not self.available:
            self.available = True
            return f"You have returned {self.title} by {self.author}."
        else:
            return f"{self.title} by {self.author} is already available."

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)

    def display_books(self):
        for book in self.books:
            print(f"Title: {book.title}, Author: {book.author}, ISBN: {book.ISBN}")

library = Library()
book1 = Book("Hello Cello", "Tere Liye", "3t71237920")
book2 = Book("Laskar Pelangi", "Andrea Hirata", "2371903298")

library.add_book(book1)
library.add_book(book2)
library.display_books()

print("-"*30)
print(book1.borrow_book())
print(book2.return_book())