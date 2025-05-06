class Dog:
    def __init__(self, name):
        self.name =name
    def bark(self):
        print(f"{self.name} says woof")
dog = Dog('Allen')
dog.bark()

class Car:
    def __init__(self,make, owner):
        self.make = make
        self.owner = owner
    def driving(self):
            print(f"{self.owner} is driving {self.make}")
car = Car('Rover', 'Klein')
car.driving()            

class Book:
     def __init__(self, title, author, pages, current_page):
          self.title = title
          self.author = author
          self.pages = pages
          self.current_page = current_page
     def read(self):
          print(f" {self.current_page}")
     def bookmark(self):
          print(f'Bookmark set at page {self.pages} of {self.title}')
book_current_page = 0
for book_current_page in range (1, 2, 1):
     print(book_current_page)

bookmark_page = 0
for bookmark_page in range(1, 4, 1):
     print(bookmark_page)

where_i_am = Book('The Hobbit', 'Dan Brown', bookmark_page, book_current_page)
where_i_am.read()
where_i_am.bookmark()