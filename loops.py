
def  main():
    print("program start")
    i=0
    while(i<100):
        print("count {} ".format(i),end="")
        i+=2
        if(i%5==0 and i<100):
            print("\n")
    print("\nprogram end")

if __name__ == '__main__':main()

