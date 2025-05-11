class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        
    def save_book(self):
        with open("Book.txt","a") as f:
            f.write(f"{self.title},{self.author},{self.isbn}\n")
            
class Library:
    def view_book(self):
        with open ("Book.txt", "r") as f:
            content = f.readlines()
            for line in content:
                print(line.strip())
            
    def search_book(self,title):
        with open ("Book.txt", "r") as f:
            lines = f.readlines()
            matches = [line.strip() for line in lines if title.lower() in line.lower()]
            if matches:
                print("Search Results:")
                for match in matches:
                    print(match)
            else:
                print("No book found with that title.")
            
    def delete_book(self,isbn):
        with open ("Book.txt", "r") as f:
            lines = f.readlines()
        line = [line for line in lines if isbn not in line]
        with open ("Book.txt", "w") as f:
            f.writelines(line)
        print(f"Book with ISBN {isbn} has been deleted (if it existed).")
            
    def count_books(self):
        with open ("Book.txt", "r") as f:
            lines = f.readlines()
        print(f"Total books: {len(lines)}")
            
            
# Create and save 5 books
b1 = Book("The Alchemist", "Paulo Coelho", "9780061122415")
b2 = Book("1984", "George Orwell", "9780451524935")
b3 = Book("To Kill a Mockingbird", "Harper Lee", "9780060935467")
b4 = Book("Pride and Prejudice", "Jane Austen", "9780141439518")
b5 = Book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565")

b1.save_book()
b2.save_book()
b3.save_book()
b4.save_book()
b5.save_book()

# Create Library object and perform operations
lib = Library()

print("\n📚 Viewing all books:")
lib.view_book()

print("\n🔍 Searching for 'pride':")
lib.search_book("pride")

print("\n🗑️ Deleting book with ISBN '9780451524935':")
lib.delete_book("9780451524935")

print("\n📚 Viewing all books after deletion:")
lib.view_book()

print("\n🔢 Counting total books:")
lib.count_books()

        
        
            