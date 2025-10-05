import tkinter as tk
from tkinter import messagebox, simpledialog

class Book:
    def __init__(self, id, title, author):
        self.id = id
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow(self):
        self.is_borrowed = True

    def give_back(self):
        self.is_borrowed = False

    def __str__(self):
        status = " (Borrowed)" if self.is_borrowed else ""
        return f"{self.id} - {self.title} by {self.author}{status}"

class LibraryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")

        self.books = []

        self.book_listbox = tk.Listbox(root, width=60)
        self.book_listbox.pack(pady=10)

        self.add_button = tk.Button(root, text="Add Book", command=self.add_book)
        self.add_button.pack(pady=5)

        self.borrow_button = tk.Button(root, text="Borrow Book", command=self.borrow_book)
        self.borrow_button.pack(pady=5)

        self.return_button = tk.Button(root, text="Return Book", command=self.return_book)
        self.return_button.pack(pady=5)

        self.refresh_books()

    def refresh_books(self):
        self.book_listbox.delete(0, tk.END)
        for book in self.books:
            self.book_listbox.insert(tk.END, str(book))

    def add_book(self):
        try:
            id = int(simpledialog.askstring("Input", "Enter Book ID:", parent=self.root))
            title = simpledialog.askstring("Input", "Enter Book Title:", parent=self.root)
            author = simpledialog.askstring("Input", "Enter Book Author:", parent=self.root)
            if title and author:
                self.books.append(Book(id, title, author))
                self.refresh_books()
        except (ValueError, TypeError):
            messagebox.showerror("Error", "Invalid input.")

    def borrow_book(self):
        selected = self.book_listbox.curselection()
        if selected:
            book = self.books[selected[0]]
            if not book.is_borrowed:
                book.borrow()
                self.refresh_books()
            else:
                messagebox.showinfo("Info", "Book is already borrowed.")
        else:
            messagebox.showwarning("Warning", "No book selected.")

    def return_book(self):
        selected = self.book_listbox.curselection()
        if selected:
            book = self.books[selected[0]]
            if book.is_borrowed:
                book.give_back()
                self.refresh_books()
            else:
                messagebox.showinfo("Info", "Book was not borrowed.")
        else:
            messagebox.showwarning("Warning", "No book selected.")

if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryApp(root)
    root.mainloop()
