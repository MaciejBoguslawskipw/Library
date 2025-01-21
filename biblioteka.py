class Book: 
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        
    def __str__(self):
        
        return f"{self.title} {self.author} {self.year}"
    
class Reader:
    def __init__(self, name, surname, book):
        self.name = name
        self.surname = surname
        self.book = book
    def __str__(self):
        
        return f"{self.name} {self.surname}"
    
class PremiumReader:
    
    def __init__(self, name, surname, book, discount):
        self.name = name
        self.surname = surname
        self.book = book
        self.discount = discount
        
    def __str__(self):
        
        return f"{self.name} {self.surname}"
    
class Library:
    def __init__(self):
        self.books = []
        self.readers = []

    def add_book(self, book):
        self.books.append(book)

    def add_reader(self, reader):
        self.readers.append(reader)

    def list_books(self):
        return [str(book) for book in self.books]

    def list_readers(self):
        return [str(reader) for reader in self.readers]
    
def main():
    
    book1 = Book("Harry Potter", "J.K. Rowling", 1997)
    book2 = Book("The Lord of the Rings", "J.R.R. Tolkien", 1954)
    book3 = Book("The Catcher in the Rye", "J.D. Salinger", 1951)
    book4 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
    book5 = Book("To Kill a Mockingbird", "Harper Lee", 1960)
    reader1 = Reader("John", "Doe", book1)
    reader2 = Reader("Jane", "Doe", book2)
    premium_reader1 = PremiumReader("Alice", "Smith", book3, 0.1)
    premium_reader2 = PremiumReader("Bob", "Johnson", book4, 0.2)

    lib = Library()
    lib.add_book(book1)
    lib.add_book(book2)
    lib.add_book(book3)
    lib.add_book(book4)
    lib.add_book(book5)

    lib.add_reader(reader1)
    lib.add_reader(reader2)
    lib.add_reader(premium_reader1)
    lib.add_reader(premium_reader2)

    print("Books in library:")
    for book in lib.list_books():
        print(book)

    print("\nReaders in library:")
    for reader in lib.list_readers():
        print(reader)

if __name__ == "__main__":
    main()