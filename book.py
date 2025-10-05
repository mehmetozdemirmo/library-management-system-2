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
