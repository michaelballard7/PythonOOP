
class Library:

    def __init__(self, *args):
        self.available_books = []

        for arg in args:
         self.available_books.append(arg)


    def displayBooks(self):
       return self.available_books

    def lendBook(self):
        pass
        

    def returnBook(self):
        pass

class TestClass():

    global_attr = "A global class attribute"

    def test_method(self    ):
        print("Hello")

class NamingClass():
    def __init__(self, first, last):
        self.first_att = first 
        self.last_att = last 

    def name_print(self):
        return "First Name {} , Last Name {}".format(self.first_att, self.last_att)



class Customer:
    def requestBook(self):
        pass

    def returnBook(self):
        pass

library = Library("test","test2","test3")
customer = Customer()

print(library.displayBooks())


namer = NamingClass("Michael", "Ballard")
print(namer.name_print())