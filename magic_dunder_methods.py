class Book:
  def __init__(self,title,author,pages):
    self.title=title
    self.author=author
    self.pages=pages

  def __str__(self):
    return f"'{self.title} by {self.author}'"
  
  def __eq__(self, other):
    return ((self.author==other.author) and (self.title==other.title) )
  
  def __lt__(self,other):
    return (self.pages<other.pages)
  
  def __gt__(self,other):
    return (self.pages>other.pages)

  def __add__(self,other):
    return (f"{self.pages+other.pages} pages")
  
  def __contains__(self,keyword):
    return keyword in self.title or keyword in self.author
  
  def __getitem__(self,key):
    if key=='title':
      return self.title
    elif key=='author':
      return self.author
    elif key=='pages':
      return self.pages
    else:
      return f"Key '{key}' was not found"

book1=Book('Harry Potter','JK Rowling',300)
book2=Book('The Snake', 'ABC' ,225)
book3=Book('The Stone', 'Lawyer' ,173)
book4=Book('The Stone', 'Lawyer' ,173)

print(book1)
print(book3==book4)
print(book2>book4)
print(book1+book2)
print('Harry' in book1)
print('ABCD' in book2)
print(book1['title'])
print(book3['author'])
print(book4['Audio'])