# library_system.py

class Book:
    """
    Base class for all books in the library system.
    Defines common attributes like title and author.
    """
    def __init__(self, title: str, author: str):
        """
        Initializes a new Book instance.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
        """
        self.title = title
        self.author = author

    def get_details(self) -> str:
        """
        Returns a string with the common details of the book.
        This method will be extended by derived classes.
        """
        return f"{self.title} by {self.author}"

class EBook(Book):
    """
    Derived class for electronic books.
    Inherits from Book and adds a file_size attribute.
    """
    def __init__(self, title: str, author: str, file_size: int):
        """
        Initializes a new EBook instance.

        Args:
            title (str): The title of the e-book.
            author (str): The author of the e-book.
            file_size (int): The file size of the e-book in KB.
        """
        # Call the base class (Book) constructor
        super().__init__(title, author)
        self.file_size = file_size

    def get_details(self) -> str:
        """
        Overrides the base class method to include e-book specific details.
        """
        return f"EBook: {super().get_details()}, File Size: {self.file_size}KB"

class PrintBook(Book):
    """
    Derived class for physical print books.
    Inherits from Book and adds a page_count attribute.
    """
    def __init__(self, title: str, author: str, page_count: int):
        """
        Initializes a new PrintBook instance.

        Args:
            title (str): The title of the print book.
            author (str): The author of the print book.
            page_count (int): The number of pages in the print book.
        """
        # Call the base class (Book) constructor
        super().__init__(title, author)
        self.page_count = page_count

    def get_details(self) -> str:
        """
        Overrides the base class method to include print book specific details.
        """
        return f"PrintBook: {super().get_details()}, Page Count: {self.page_count}"

class Library:
    """
    Represents a library that manages a collection of books.
    Demonstrates composition by holding a list of Book objects.
    """
    def __init__(self):
        """
        Initializes a new Library instance with an empty list of books.
        """
        self.books = []

    def add_book(self, book: Book):
        """
        Adds a book (Book, EBook, or PrintBook instance) to the library's collection.

        Args:
            book (Book): An instance of Book or one of its derived classes.
        """
        self.books.append(book)
        print(f"Added '{book.title}' to the library.")

    def list_books(self):
        """
        Prints the details of all books currently in the library.
        It leverages the polymorphic `get_details()` method of each book.
        """
        print("\n--- Books in the Library ---")
        if not self.books:
            print("The library is currently empty.")
            return

        for book in self.books:
            # Use type checking to display specific output for base Book class
            if isinstance(book, EBook):
                print(book.get_details())
            elif isinstance(book, PrintBook):
                print(book.get_details())
            elif isinstance(book, Book):
                # For the base Book class, format it as "Book: Title by Author"
                print(f"Book: {book.get_details()}")
