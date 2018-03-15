

def  main():
     n = True
     while(n):
         age = input("enter your age or enter 0 to exit : ")
         try:
          if(int(age)>=18):
            print("welcome")
          elif(int(age)>15 and int(age)<18):
              print("hi")
          elif(int(age)>10):
            print("not welcome")
          elif(int(age)>0 and int(age)<=10):
            print(" you a kid")
          else:
              n=False
         except:
             print("error")







if __name__ == '__main__':main()
