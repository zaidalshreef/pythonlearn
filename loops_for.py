
def  main():
    l = [1,2,3,"hi",4,5,5.4]
    print(len(l))
    for item in l:
        if(item==l[len(l)-1]):
            print(item)
        else:
            print(item,end=",")
# for using range
    for item in range(7):
        if(item==6):
            print(l[item])
        else:
            print(l[item],end=",")






if __name__ == '__main__':main()

