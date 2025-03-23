from book import Book #importing Book class from book.py file
import json

class Library:
    def __init__ (self):
        self.books= [] #manages a list of books
    
    def add_books (self, book): #to add books
        self.books.append(book) #to add a new book object to the self.books list
        print(f"The book '{book.title}' is added to the library ")
     
    def display_all_books (self): #to view all the books
        if self.books:
            print("All the books in library")
            for book in self.books:
                print(book)
        else:
            print("This library is empty!")
    
    def search_books_by_title (self, title): #to search books by title
        search_book= [book for book in self.books if title.lower() in title.lower()] #using title.lower to make the search case sensetive
        if search_book:
            print(f"Found {len(search_book)} books by '{title}'.") #len returns the number of character in a text string.
        else:
            print(f"No books by the title '{title}' was found")         
               
        
    def __update__(self, ISBN, new_ISBN=None, new_title=None, new_author=None):
        for book in self.books:
            if ISBN == ISBN:
                if new_title:
                    book.title=new_title
                if new_ISBN:
                    book.ISBN=new_ISBN
                if new_author:
                    book.author=new_author
                    print(f"Book with isbn '{ISBN}' updated sucessfully!")
                else:
                    print(f"Cannot update books with isbn '{ISBN}' ")                               

    def __remove__ (self, ISBN):
        for book in self.books:
            if book.ISBN == ISBN:
                self.books.remove(book)
                print(f"book with isbn '{ISBN}'removed from the library ")
                return
            print(f"book with isbn '{ISBN}'failed to remove")
            
        




    


        
    


        
    


        
