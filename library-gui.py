import tkinter as tk
from tkinter import messagebox, simpledialog, ttk

class Book:
    def __init__(self, title, author, quantity):
        self.title = title
        self.author = author
        self.quantity = quantity
        self.borrowed = 0

    def borrow(self):
        if self.borrowed < self.quantity:
            self.borrowed += 1
            return True
        return False

    def give_back(self):
        if self.borrowed > 0:
            self.borrowed -= 1

class LibraryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.books = [
    Book("The Great Gatsby", "F. Scott Fitzgerald", 5),
    Book("To Kill a Mockingbird", "Harper Lee", 4),
    Book("1984", "George Orwell", 6),
    Book("Pride and Prejudice", "Jane Austen", 3),
    Book("The Catcher in the Rye", "J.D. Salinger", 2),
    Book("Moby Dick", "Herman Melville", 4),
    Book("War and Peace", "Leo Tolstoy", 3),
    Book("The Hobbit", "J.R.R. Tolkien", 5),
    Book("Crime and Punishment", "Fyodor Dostoevsky", 4),
    Book("Brave New World", "Aldous Huxley", 3),
    Book("The Odyssey", "Homer", 2),
    Book("Ulysses", "James Joyce", 3),
    Book("The Divine Comedy", "Dante Alighieri", 4),
    Book("Hamlet", "William Shakespeare", 5),
    Book("The Iliad", "Homer", 2),
    Book("One Hundred Years of Solitude", "Gabriel Garcia Marquez", 4),
    Book("The Brothers Karamazov", "Fyodor Dostoevsky", 3),
    Book("Wuthering Heights", "Emily Bronte", 2),
    Book("The Picture of Dorian Gray", "Oscar Wilde", 3),
    Book("Don Quixote", "Miguel de Cervantes", 4),
    Book("The Count of Monte Cristo", "Alexandre Dumas", 5)
    ]

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview.Heading", background="#4CAF50", foreground="white", font=('Arial', 12, 'bold'))
        style.configure("Treeview", rowheight=25, font=('Arial', 11))
        style.map('Treeview', background=[('selected', '#9ACD32')])

        # --- Frame ---
        main_frame = tk.Frame(root)
        main_frame.pack(padx=10, pady=10)

        # --- Treeview ---
        columns = ("Title", "Author", "Quantity", "Borrowed")
        self.tree = ttk.Treeview(main_frame, columns=columns, show="headings", height=15)
        for col in columns:
            self.tree.heading(col, text=col, command=lambda _col=col: self.sort_by_column(_col))
            self.tree.column(col, width=150, anchor=tk.CENTER, stretch=False)
        self.tree.pack(side=tk.LEFT)

        # Scrollbar
        scrollbar = tk.Scrollbar(main_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=tk.LEFT, fill=tk.Y)

        # Buttons
        button_frame = tk.Frame(root)
        button_frame.pack(pady=10)
        tk.Button(button_frame, text="Add Book", width=15, command=self.add_book).grid(row=0, column=0, padx=5)
        tk.Button(button_frame, text="Borrow Book", width=15, command=self.borrow_book).grid(row=0, column=1, padx=5)
        tk.Button(button_frame, text="Return Book", width=15, command=self.return_book).grid(row=0, column=2, padx=5)

        self.refresh_books()

    def refresh_books(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

        for book in self.books:
            # Her sütun için renkli hücre kullanımı
            # Treeview doğrudan sütun renklerini desteklemez, ama hücreleri farklı tag ile renklendirebiliriz
            self.tree.insert(
                "", tk.END,
                values=(book.title, book.author, book.quantity, book.borrowed),
                tags=("row",)
            )

        # Tag ile sütun bazlı renklendirme
        # Her sütun için farklı arka plan
        for i, item in enumerate(self.tree.get_children()):
            self.tree.tag_configure(item, background="white")  # Temel satır arka planı
            # Hücre bazlı renklendirme için tek tek değerleri alıp hücreye etki edemiyoruz,
            # fakat satırın tamamını tag ile renklendirebiliriz.
            # Bu yüzden farklı satırlara farklı renk atayabiliriz:
            if i % 2 == 0:
                self.tree.item(item, tags=("evenrow",))
            else:
                self.tree.item(item, tags=("oddrow",))
        self.tree.tag_configure("evenrow", background="#E8F6F3")  # Açık mavi
        self.tree.tag_configure("oddrow", background="#FDEBD0")   # Açık turuncu

    def add_book(self):
        title = simpledialog.askstring("Input", "Enter Book Title:", parent=self.root)
        author = simpledialog.askstring("Input", "Enter Book Author:", parent=self.root)
        try:
            quantity = int(simpledialog.askstring("Input", "Enter Quantity:", parent=self.root))
            if title and author and quantity > 0:
                for book in self.books:
                    if book.title.lower() == title.lower() and book.author.lower() == author.lower():
                        book.quantity += quantity
                        self.refresh_books()
                        return
                self.books.append(Book(title, author, quantity))
                self.refresh_books()
        except (ValueError, TypeError):
            messagebox.showerror("Error", "Invalid input.")

    def borrow_book(self):
        selected = self.tree.focus()
        if selected:
            item = self.tree.item(selected)
            title, author = item["values"][0], item["values"][1]
            for book in self.books:
                if book.title.lower() == title.lower() and book.author.lower() == author.lower():
                    if book.borrow():
                        self.refresh_books()
                    else:
                        messagebox.showinfo("Info", "No copies available to borrow.")
                    return
        else:
            messagebox.showwarning("Warning", "No book selected.")

    def return_book(self):
        selected = self.tree.focus()
        if selected:
            item = self.tree.item(selected)
            title, author = item["values"][0], item["values"][1]
            for book in self.books:
                if book.title.lower() == title.lower() and book.author.lower() == author.lower():
                    if book.borrowed > 0:
                        book.give_back()
                        self.refresh_books()
                    else:
                        messagebox.showinfo("Info", "Book was not borrowed.")
                    return
        else:
            messagebox.showwarning("Warning", "No book selected.")

    def sort_by_column(self, col):
        if col in ["Title", "Author"]:
            self.books.sort(key=lambda b: getattr(b, col.lower()).lower())
        elif col in ["Quantity", "Borrowed"]:
            self.books.sort(key=lambda b: getattr(b, col.lower()))
        self.refresh_books()
    
    
if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryApp(root)
    root.mainloop()
