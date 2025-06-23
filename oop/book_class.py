class Book:
    def __init__(self, title, author, year):
        """"""
        self.title = title
        self.author = author
        self.year = year
        print(f"Book '{self.title}' created.") #added for clarity during book instantiation

    def __del__(self):
        print(f"Deleting {self.title}")

    def __str__(self):
        return f"Book('{self.title}', {self.year})"
    
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"
