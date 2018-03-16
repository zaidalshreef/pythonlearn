
class car:
    def __init__(self,name):
        self._name = name
    def getOwner(self):
        print(" owner is {}".format((self._name)))
def  main():
    mycar = car("zaid")
    mycar.getOwner()
    farsCar = car("shreef")
    farsCar.getOwner()

if __name__ == '__main__':main()
