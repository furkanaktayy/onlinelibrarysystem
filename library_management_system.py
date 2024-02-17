class Library:
    def __init__(self):
        self.file = open('books.txt', 'a+')

    def __del__(self):
        self.file.close()

    def list_books(self):
        self.file.seek(0)
        book_lines = self.file.read().splitlines()
        if not book_lines:
            print("There is no book in the list. You're redirecting to the menu...")
        else:
            for book in book_lines:
                book_name, author, release_date, number_page = book.split(',')
                print(f"{book_name},{author}")

    def add_book(self):
        book_name = input("Please enter book name: ")
        author = input("Please enter author: ")
        release_date = input("Please enter release date: ")
        number_page = input("Please enter book's number of page: ")
        book_info = f"Book name: {book_name}, Author: {author}, Release date: {release_date}, Number of page: {number_page}\n"
        self.file.write(book_info)
        print("Book is successfully added! You're redirecting to the menu...")

    def remove_book(self):
        while True:
            selected_book = input("Please enter the name of book for delete: ")
            self.file.seek(0)
            lines = self.file.readlines()

            if not lines:
                print("There are no books in the library. You're redirecting to the menu...")

            self.file.seek(0)
            self.file.truncate()

            book_removed = False

            for line in lines:
                if selected_book not in line:
                    self.file.write(line)
                else:
                    book_removed = True

            if book_removed:
                print("The book deleted successfully!")
                return
            else:
                print("The selected book was not found in the library.")


lib = Library()

while True:
    menu_select = input("***MENU***\n1)List Books\n2)Add Book\n3)Remove Book\n4)Exit\nYour Selection: ")
    if menu_select == '1':
        lib.list_books()
    elif menu_select == '2':
        lib.add_book()
    elif menu_select == '3':
        lib.remove_book()
    elif menu_select == '4':
        exit()
    else:
        print("Please enter valid value and try again!")