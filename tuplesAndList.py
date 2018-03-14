
def main():
    #tuples (immutable: may not change)
    agestuple =(20,23,32,10)
    print(agestuple,type(agestuple))
    print(agestuple[0])#first item
    print(agestuple[0:3])#from first item to third item

    #list (mutable : the value may change)
    ageslist = [20,30,26,40,14,45,75]
    print(ageslist,type(ageslist))
    print(ageslist[3])
    ageslist.append(201)
    print(ageslist)
    ageslist.insert(0,500)
    print(ageslist)
    print(ageslist[0:2])
    print(ageslist[2:len(ageslist)])

    #String
    info = "computer since"
    print(info[9:len(info)])
    print(info.upper())





if __name__ == '__main__': main()
