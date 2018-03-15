
num1 = 0
num2 = 0
result = 0


def display():
    print("{} + {} = {} ".format(num1,num2,result))


def sum(n1,n2):
    r = n2+n1
    return r

def  main():
    global num1
    global num2
    global result
    while(True):
     try:
      num1, num2 = input("enter tow number or any key to exit : ").split()
      result = sum(int(num1),int(num2))
      display()
     except:
           print("you exit")
           break



if __name__ == '__main__':main()

