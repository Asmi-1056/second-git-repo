#Asmi Purarkar

#Library Management System

# Define a book
def add_book(Title, Author, Genre):
    # This creates a book tuple
    return (Title, Author, Genre)

#Add a book to Library
def add_to_library(tuple, Library):
    # To add a book to the library if the book is not already present by using set for the duplicates. 
    Library.append(tuple)
    myset = set(Library)  # << Converts the library list to the set to check the duplicates.
    print(f"Book '{tuple[0]}' is added successfully.") 

# Remove Books 
def remove_from_library(Title, Library):
    # To remove a particular book from the library by using the book's title
    for i, Book in enumerate(Library):
        if Book[0] == Title:
            Library.pop(i)
            print(f"Book '{Title}' is removed successfully.")
            return
    print(f"Book '{Title}' not found in the library.")

# Search Books
def search_books(search_term, library):
    # To search the book by Title and Author.
    results = []
    for Book in library:
        if search_term.lower() in Book[0].lower() or search_term.lower() in Book[1].lower():
            results.append(Book)
    if results:
        print(f"Matching Books found '{search_term}':")
        for Book in results:
            print(f"- {Book[0]} by {Book[1]}")
    else:
        print(f"No matching Books found '{search_term}'.")

# List Books
def list_books(Library):
    # To check all books and prints all books in the library.
    if Library:
        print("List of all the Books:")
        for Book in Library:
            print(f"- {Book[0]} by {Book[1]} ({Book[2]})")
    else:
        print("Library is currently empty.")

# Categorize Books
def categorize_books(Library):
    # This categorizes the books by genre using a dictionary. 
    categories = {}
    for Book in Library:
        Genre = Book[2]
        if Genre in categories:
            categories[Genre].append(Book)
        else:
            categories[Genre] = [Book]
    if categories:
        print("Books are categorized by the Genre:")
        for Genre, Books in categories.items():
            print(f"- {Genre}:")
            for Book in Books:
                print(f"  - {Book[0]} by {Book[1]}")
    else:
        print("No books are found in the library.")          

def asm():
    Library = []
    choice = None
    while choice != '7':
        print("\nLibrary Management System Menu:")
        print("1. Add Book")
        print("2. Add Book to Library")
        print("3. Remove Book")
        print("4. Search Book")
        print("5. List Books")
        print("6. Categorize Books")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            Title = input("Enter book title: ")
            Author = input("Enter book author: ")
            Genre = input("Enter book genre: ")
            Library.append(add_book(Title, Author, Genre))
        elif choice == '2':
            Title = input("Enter book title: ")
            Author = input("Enter book author: ")
            Genre = input("Enter book genre: ")
            tuple = (Title, Author, Genre)
            add_to_library(tuple, Library)
        elif choice == '3':
            Title = input("Enter book title to remove: ")
            remove_from_library(Title, Library)
        elif choice == '4':
            search_term = input("Enter search term (title or author): ")
            search_books(search_term, Library)
        elif choice == '5':
            list_books(Library)
        elif choice == '6':
            categorize_books(Library)
        elif choice == '7':
            print("Exiting Library Management System.")
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    asm()
