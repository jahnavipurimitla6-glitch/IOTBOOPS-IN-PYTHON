

def __str__(self):
    status = "Avaliable"




    def add _book(slf, book):
        self.book.append(book)
        print|(f"'{book.title}' added to the library.")


    def remove _book(self, title):
        foe book in self.books:
            of book.title.lower() == title.lower():
                print(f"'{title


    def search_book(self, title):
        for book in self.books:
            if book.title.lowere() == title.lower():
                print(f"'Found: {book}")
                return book
         print(f"' {title}'not found.")
         return Nome


    def borrow_book(self, title):
        book = self.search_book(title)
        if book and book.is_available:
            book.is_available = False
            print(f"You borrowed '{book.title}'.")
       elif book:
           print(f"'{book.title}' was not borrowed.")


lib = Library()
lib.add_book(Book("Python Basics", "John Doe"))
lib.add_book(Book("Data Sciense", "Jane Smith"))
lib.add_book(Book("Machine Learing", "Alanb Turing"))

while True:
    choice == int(input('''
==== Library Menu =====
    1 -> Display All Books
    2 -> Add a Book
    3 -> Search a Book
    4 -> Borrow a Book
    5 -> Return a Book
    6 -> Remove a Book
    7 -> Exit
    Enter choice:'''))

    if choice == 1:
        print("/nLibrary Collection:")
        for b in lib.books:
            print(b)

    elif choice == 2:
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        lib.add_book(Book(title, author))

    elif choice == 3:
        title = input("Enter book title to remove: ")
        lib.remove_book(title)

     elif choice == 4:
         title = input("Enter book title to search: ")
         lib.search_book(title)


     elif choice == 5:
         title = input("Enter book title to borrow: ")
         lib.borrow_book(title)

     elif choice == 6:
         title = input("Enter book title to return: ")
         lib.return_book(title)

     elif choice == 7:
         print("Exiting Library Stsrem. Goodbye!")
         break
         



           
