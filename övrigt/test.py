import tkinter as tk
from tkinter import messagebox, simpledialog

class Book:
    """Class representing a book."""
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.utlanda = False

    def __str__(self):
        return f"{self.title} by {self.author} ({self.year})"


class Library:
    """Class representing the library collection."""
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def delete_book(self, book_index):
        if 0 <= book_index < len(self.books):
            del self.books[book_index]
        else:
            raise IndexError("Book not found")

    def update_book(self, book_index, title, author, year):
        if 0 <= book_index < len(self.books):
            self.books[book_index].title = title
            self.books[book_index].author = author
            self.books[book_index].year = year
        else:
            raise IndexError("Book not found")

    def get_books(self):
        return self.books

class LibraryGUI:
    """GUI class for the Library Management System."""
    def __init__(self, root, library):
        self.root = root
        self.library = library
        self.root.title("Library Management System")

        # Create and place listbox to display books
        self.book_listbox = tk.Listbox(root, width=50, height=15)
        self.book_listbox.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

        # Create buttons for CRUD operations
        self.add_button = tk.Button(root, text="Add Book", command=self.add_book)
        self.add_button.grid(row=1, column=0, padx=10, pady=10)

        self.update_button = tk.Button(root, text="Update Book", command=self.update_book)
        self.update_button.grid(row=1, column=1, padx=10, pady=10)

        self.delete_button = tk.Button(root, text="Delete Book", command=self.delete_book)
        self.delete_button.grid(row=1, column=2, padx=10, pady=10)

        # Refresh the listbox to display any existing books
        self.refresh_book_list()

    def refresh_book_list(self):
        """Refresh the listbox to display the updated list of books."""
        self.book_listbox.delete(0, tk.END)
        for index, book in enumerate(self.library.get_books()):
            self.book_listbox.insert(index, book)

    def add_book(self):
        """Add a new book to the library."""
        title = simpledialog.askstring("Input", "Enter the book title:")
        author = simpledialog.askstring("Input", "Enter the author:")
        year = simpledialog.askstring("Input", "Enter the publication year:")

        if title and author and year:
            new_book = Book(title, author, year)
            self.library.add_book(new_book)
            self.refresh_book_list()
            messagebox.showinfo("Success", "Book added successfully!")
        else:
            messagebox.showerror("Error", "All fields must be filled!")

    def delete_book(self):
        """Delete the selected book from the library."""
        selected_index = self.book_listbox.curselection()
        if selected_index:
            try:
                self.library.delete_book(selected_index[0])
                self.refresh_book_list()
                messagebox.showinfo("Success", "Book deleted successfully!")
            except IndexError:
                messagebox.showerror("Error", "Failed to delete book.")
        else:
            messagebox.showerror("Error", "Please select a book to delete.")

    def update_book(self):
        """Update the details of the selected book."""
        selected_index = self.book_listbox.curselection()
        if selected_index:
            book_index = selected_index[0]
            current_book = self.library.get_books()[book_index]

            # Prompt for new book details
            new_title = simpledialog.askstring("Input", f"Enter new title (current: {current_book.title}):")
            new_author = simpledialog.askstring("Input", f"Enter new author (current: {current_book.author}):")
            new_year = simpledialog.askstring("Input", f"Enter new year (current: {current_book.year}):")

            if new_title and new_author and new_year:
                try:
                    self.library.update_book(book_index, new_title, new_author, new_year)
                    self.refresh_book_list()
                    messagebox.showinfo("Success", "Book updated successfully!")
                except IndexError:
                    messagebox.showerror("Error", "Failed to update book.")
            else:
                messagebox.showerror("Error", "All fields must be filled!")
        else:
            messagebox.showerror("Error", "Please select a book to update.")


def main():
    root = tk.Tk()
    library = Library()
    app = LibraryGUI(root, library)
    root.mainloop()

if __name__ == "__main__":
    main()
