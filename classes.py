class User:

    def setUserName(self):
        """ A method to set the name property """
        name = input("What would you like the name to be? ")
        self._userName = name 

    def getUserName(self):
        """ A method to get the name property """
        return self._userName


class Car: 

    def setCarType(self):
        pass 


def main():
    u1 = User()
    u1.setUserName()
    print(" The set name was", u1.getUserName())


if __name__ == '__main__': main()