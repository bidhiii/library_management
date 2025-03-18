from book import Book #importing from the book file
from library import Library #importing from the library file

if __name__ == "__main__": #if you want to run the script directly 
    library=Library()

    book1 = Book("Bell jar", "Sylvia Plath","literary fiction", "1963", "9780060133566")
    book2 = Book("The stranger", "Albert Camus","Existentialism","1942","9780394533056")
    book3 = Book("pride and prejudice", "Jane Austen", "Romance novel","1813", "9789387779679")



    library.add_books(book1)
    library.add_books(book2)
    library.add_books(book3)

    
    library.display_all_books()




