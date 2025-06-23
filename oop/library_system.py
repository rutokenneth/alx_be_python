class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        if isinstance(book, Book):
            self.books.append(book)
            print(f"Added '{book.title}' to the library.")
        else:
            print("Invalid object. Only Book, EBook, or PrintBook instances can be added.")

    def list_books(self):
        if not self.books:
            print("The library is empty.")
            return

        print("\n--- Library Collection ---")
        for book in self.books:
            if isinstance(book, EBook):
                print(f"EBook: '{book.title}' by {book.author}, File Size: {book.file_size}KB")
            elif isinstance(book, PrintBook):
                print(f"PrintBook: '{book.title}' by {book.author}, Page Count: {book.page_count}")
            elif isinstance(book, Book):
                print(f"Book: '{book.title}' by {book.author}")
        print("--------------------------")

# # Example Usage (for testing purposes, you can put this in a separate main.py or directly below)
# if __name__ == "__main__":
#     my_library = Library()

#     book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
#     ebook1 = EBook("Dune", "Frank Herbert", 2048)
#     printbook1 = PrintBook("To Kill a Mockingbird", "Harper Lee", 320)
#     ebook2 = EBook("Neuromancer", "William Gibson", 1500)

#     my_library.add_book(book1)
#     my_library.add_book(ebook1)
#     my_library.add_book(printbook1)
#     my_library.add_book(ebook2)

#     # Attempt to add an invalid object
#     # my_library.add_book("Not a book")

#     my_library.list_books()

#     # Demonstrate an empty library
#     empty_library = Library()
#     empty_library.list_books()
