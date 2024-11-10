class Library:
  def __init__(self,name):
    self.name=name
    self.book_list=[]

  def add_book(self,book):
    self.book_list.append(book)

  def list_book(self):
    return [f'{book.title} by {book.author}'for book in self.book_list]

class Book:
  def __init__(self,title,author):
    self.title=title
    self.author=author

book1=Book('Harry Potter & the Deathly Hollows - 1','J.K. Rowling')
book2=Book('Some Horror Book','Narayan Dharap')
book3=Book("Vyakti ani Valli","P.L. Deshpande")

libray=Library('Vishwas Library')

libray.add_book(book1)
libray.add_book(book2)
libray.add_book(book3)

libray.list_book()

print(libray.name)
for book in libray.list_book():
  print(book)