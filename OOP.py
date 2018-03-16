
class car:
    def getOwner(self):
        print(" owner is {}".format((self._name)))
    def SetOwner(self,name):
        self._name = name

def  main():
    mycar = car()
    mycar.SetOwner("zaid")
    mycar.getOwner()
    farsCar = car()
    farsCar.SetOwner("fars")
    farsCar.getOwner()

if __name__ == '__main__':main()
