from book import Book
from library import Library  # Import the Library class from library.py
import json

def display_menu():
    """Display the main menu options."""
    print("\n--- Library Management System ---")
    print("1. Add a new book")
    print("2. View all books")
    print("3. Search for a book by title")
    print("4. Update a book")
    print("5. Remove a book")
    print("6. Exit")


def add_book_interactive(library):
    """Interactively add a new book to the library."""
    print("\nAdd a new book:")
    title = input("Enter the title: ")
    author = input("Enter the author: ")
    category = input("Enter the category: ")
    year = input("Enter the year: ")
    ISBN = input("Enter the ISBN: ")

    # Create a new Book object and add it to the library
    from book import Book  # Import the Book class
    new_book = Book(title, author, category, year, ISBN)
    library.add_books(new_book)


def search_book_interactive(library):
    """Interactively search for a book by title."""
    title = input("\nEnter the title to search: ")
    library.search_books_by_title(title)


def update_book_interactive(library):
    """Interactively update a book's details."""
    ISBN = input("\nEnter the ISBN of the book to update: ")
    new_title = input("Enter the new title (leave blank to keep current): ")
    new_author = input("Enter the new author (leave blank to keep current): ")
    new_ISBN = input("Enter the new ISBN (leave blank to keep current): ")

    # Call the __update__ method (assuming it's fixed in the Library class)
    library.__update__(ISBN, new_ISBN, new_title, new_author)


def remove_book_interactive(library):
    """Interactively remove a book from the library."""
    ISBN = input("\nEnter the ISBN of the book to remove: ")
    library.__remove__(ISBN)


def main():
    """Main function to run the interactive library management system."""
    library = Library()  # Create an instance of the Library class

    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_book_interactive(library)
        elif choice == "2":
            library.display_all_books()
        elif choice == "3":
            search_book_interactive(library)
        elif choice == "4":
            update_book_interactive(library)
        elif choice == "5":
            remove_book_interactive(library)
        elif choice == "6":
            print("\nExiting the program. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please try again.")


# Run the program
if __name__ == "__main__":
    main()



