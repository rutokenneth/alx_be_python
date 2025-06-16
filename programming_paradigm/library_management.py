class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False
    
    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
        return False
    
    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False
    
    def is_available(self):
        return not self._is_checked_out
    
    def __str__(self):
        status = "Available" if self.is_available() else "Checked out"
        return f"'{self.title}' by {self.author} - {status}"

class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self, book):
        if isinstance(book, Book):
            self._books.append(book)
    
    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return f"'{title}' checked out successfully."
        return f"'{title}' is not available."
    def return_book(self, title):
        """Return a book by title."""
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return f"'{title}' returned successfully."
        return f"'{title}' is not currently checked out."

    def list_available_books(self):
        """List all books that are currently available."""
        return [book for book in self._books if book.is_available()]

    def __str__(self):
        return "\n".join(str(book) for book in self._books) if self._books else "Library is empty."
