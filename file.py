
def  main():
    out = open("test.txt","w")
    out.write("zaid")
    out.write("\nfaisal")
    out.close()
    ape = open("test.txt","a")
    ape.write("\nfars")
    ape.write("\nfahd")
    ape.close()
    read = open("test.txt","r")
    for line in read:
        print(line,end="")
    read.close()


if __name__ == '__main__':main()

