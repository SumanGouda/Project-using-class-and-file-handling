# Contact Manager

A simple Python-based Contact Manager that allows users to store and retrieve contact information using file handling.

## 🚀 Features

- Add contact details and save them to a `.txt` file
- Retrieve and display all saved contacts
- Simple command-line interface
- Uses Python’s built-in file handling features

## 🛠 Technologies Used

- Python
- File Handling

## 📂 Project Structure

Contact_Manager.py
Contact.txt


- `Contact_Manager.py`: Main script to add and read contact info
- `Contact.txt`: Text file where contact information is stored

## 🔧 How It Works

1. Run the script.
2. Enter contact details.
3. The program saves the contact to `Contact.txt`.

## 💡 Example

Name: John Doe
Phone: 1234567890
Email: john@example.com

Saved to Contact.txt as:
John Doe,1234567890,john@example.com

## 📌 Requirements
Python 3.x

📄 License
This project is open source and available under the MIT License.








### 📚 **Library Book Manager - README.md**

# Library Book Manager

A Python project to manage a simple library system using classes and file handling.

## 📦 Features

- Add books with title, author, and ISBN
- View all books
- Search for a book by title
- Delete a book by ISBN
- Count the total number of books

## 💻 Technologies Used

- Python
- File Handling
- Object-Oriented Programming (OOP)

## 📂 File Structure
Library_Book_Manager.py
Book.txt


- `Library_Book_Manager.py`: Main script containing `Book` and `Library` classes
- `Book.txt`: Stores book data in CSV format

## 🔧 How It Works

1. **Add Book**: Uses the `Book` class to write to `Book.txt`
2. **View/Search/Delete/Count**: Uses the `Library` class to manage books

## 🧪 Sample
book1 = Book("1984", "George Orwell", "123456")
book1.save_book()

lib = Library()
lib.view_book()
lib.search_book("1984")
lib.delete_book("123456")
lib.count_books()

📌 Requirements
Python 3.x

📄 License
This project is licensed under the MIT License.






