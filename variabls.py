
def  main():
    #int and float
    numflot=31/5
    print(numflot)
    numint=int(numflot)
    print(numint)
    numWithouCasting=(5*10)
    print(numWithouCasting)
    numToflot=float(5*10)
    print(numToflot)
    #strig
    #asking for input from the user
    amont=input("enter intger : ")

    print(amont,type(amont))
    #changing the type of the input from string to int
    amont=int(amont)

    print(amont, type(amont))
    data="my name is \nzaid"
    print(data,type(data))
    data2 = "{} is high".format(amont)
    print(data2,type(data2))
    datalen = "is good"
    print(len(datalen))
    print(datalen[1])



if __name__ == '__main__':main()
