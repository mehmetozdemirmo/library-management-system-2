from library import Library

def main():
    library = Library()

    while True:
        print("===== Library Menu =====")
        print("1. Add Book")
        print("2. List Books")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            id = int(input("Enter book ID: "))
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            library.add_book(id, title, author)

        elif choice == "2":
            library.list_books()

        elif choice == "3":
            id = int(input("Enter book ID to borrow: "))
            library.borrow_book(id)

        elif choice == "4":
            id = int(input("Enter book ID to return: "))
            library.return_book(id)

        elif choice == "5":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
