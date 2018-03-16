
import re
def  main():

    read = open("regfile.txt","r")
    for line in read:
        if re.search("(Za|Sa)(id|ad)",line):
            print(line,end="")
    read.close()


if __name__ == '__main__':main()
