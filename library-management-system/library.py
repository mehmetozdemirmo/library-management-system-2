from book import Book

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, id, title, author):
        book = Book(id, title, author)
        self.books.append(book)
        print("Book added successfully.\n")

    def list_books(self):
        if not self.books:
            print("No books available.\n")
            return
        print("\nList of Books:")
        for book in self.books:
            print(book)
        print()

    def borrow_book(self, id):
        for book in self.books:
            if book.id == id:
                if not book.is_borrowed:
                    book.borrow()
                    print("Book borrowed successfully.\n")
                else:
                    print("Book is already borrowed.\n")
                return
        print("Book not found.\n")

    def return_book(self, id):
        for book in self.books:
            if book.id == id:
                if book.is_borrowed:
                    book.give_back()
                    print("Book returned successfully.\n")
                else:
                    print("Book was not borrowed.\n")
                return
        print("Book not found.\n")
