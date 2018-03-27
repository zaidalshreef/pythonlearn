
class car:
    def __init__(self,**kwargs):
        self.data = kwargs
    def get(self):
           print(self.data)
    def setmodel(self,model):
        self.data["model"] = model
    def getmodel(self):
        print(" model : {}".format((self.data["model"])))
def  main():
    mycar = car(owner="zaid",model="corvet",year=2018,price=2012220,speed=300)
    mycar.get()
    farsCar = car(owner="fars",model="camry",year=2018)
    farsCar.get()
    mycar.setmodel("kia")
    mycar.getmodel()
    farsCar.setmodel("sany")
    farsCar.getmodel()
if __name__ == '__main__':main()
