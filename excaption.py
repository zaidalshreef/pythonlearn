
def  main():
    try:
     read = open("test2.txt", "r")
     for line in read:
        print(line, end="")
     read.close()
    except IOError as err:
           print(err)


if __name__ == '__main__':main()

