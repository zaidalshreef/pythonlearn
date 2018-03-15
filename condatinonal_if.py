

def  main():
     n = True
     while(n):
         age = input("enter your age or enter 0 to exit : ")
         if(int(age)>18):
            print("welcome")
         elif(int(age)>15):
              print("hi")
         elif(int(age)>10):
            print("not welcome")
         elif(int(age)>0):
            print(" you a kid")
         else:
             n=False





if __name__ == '__main__':main()
