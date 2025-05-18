class Book:
    library_name = "Central Library"

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}")

    @classmethod
    def change_library_name(cls, new_name):
        cls.library_name = new_name
        print(f"Library name changed to: {cls.library_name}")

    @staticmethod
    def is_valid_isbn(isbn):
        """A simple check: ISBN should be a 13-digit number"""
        return isinstance(isbn, str) and len(isbn) == 13 and isbn.isdigit()

book1 = Book("Waktu Yang Salah", "Fiersa Besari")
book1.display_info()

# Using class method to change class variable
Book.change_library_name("Downtown Library")

# Using static method to validate ISBN
isbn = "9783161484100"
print(f"Is '{isbn}' a valid ISBN? {Book.is_valid_isbn(isbn)}")