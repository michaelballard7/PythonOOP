

""" In python one class can be extended by more than one class """

class Person:

    def __init__(self, personName, personAge):
        self.name = personName
        self.age = personAge

    def showName(self):
        return self.name

    def showAge(self):
        return self.age

    def setName(self, name):
        self.name = name 

    def setAge(self, age):
        self.age = age

class Student:

    def __init__(self, studentId):
        self.studentId = studentId

    def getId(self):
        return self.studentId


class Resident(Person, Student):
    """ This class inherits from person and student classes """

    def __init__(self, name, age, id):
        Person.__init__(self,name, age)
        Student.__init__(self, id)


resident1 = Resident('Michael', 28, '007')
print(resident1.showName())
print(resident1.showAge())