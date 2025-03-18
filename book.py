class Book:
    def __init__(self, title, author, category, year, ISBN):
        self.title = title
        self.author = author
        self.category = category
        self.year = year
        self.ISBN = ISBN
    def __str__(self):
        return f"Title: {self.title}, Author:{self.author}, Category:{self.category} Year:{self.year}, isbn:{self.ISBN}"
