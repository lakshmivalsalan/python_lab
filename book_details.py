class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author

book1=Book("The Alchemist","Paulo Coelho")
book1.publisher="HarperCollins"

def print_book_details(book):
   if hasattr(book,"publisher"):
       print(f"{book.title} is written by {book.author} is published by {book.publisher}")

   else:
       print("Unknown publisher")

print_book_details(book1)

book2=Book("1984","George Orwell")
print_book_details(book2)
