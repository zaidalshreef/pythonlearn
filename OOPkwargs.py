
class car:
    def __init__(self,**kwargs):
        self.data = kwargs
    def get(self):
        print(" owner {}".format((self.data["owner"])),end="")
        print(" car model {}".format((self.data["model"])),end="")
        print(" year {}".format((self.data["year"])))
    def setmodel(self,model):
        self.data["model"] = model
    def getmodel(self):
        print(" car model {}".format((self.data["model"])))


def  main():
    mycar = car(owner="zaid",model="ki",year=2018)
    mycar.get()
    farsCar = car(owner="fars",model="ki",year=2018)
    farsCar.get()
    mycar.setmodel("kia")
    mycar.getmodel()
    farsCar.setmodel("sany")
    farsCar.getmodel()

if __name__ == '__main__':main()
