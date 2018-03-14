import  datetime

def  main():
    dob = int(input("enter your DOB : "))
    yearNow = datetime.datetime.now().year
    print(yearNow,type(yearNow))
    myage = yearNow - dob
    print("your age is {}".format(myage))



if __name__ == '__main__':main()
