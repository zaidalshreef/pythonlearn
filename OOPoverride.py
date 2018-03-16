class Operation:
    def Sum(self,n1,n2):
        sumresult = n1+n2
        print("sum = {} ".format(sumresult))
    def Sub(self,n1,n2):
        subresult = n1-n2
        print("sub = {} ".format(subresult))

class OprationWithMul(Operation):
    def mul(self,n1,n2):
        mulresult = n1 * n2
        print("mul = {} ".format(mulresult))
    def Sub(self,n1,n2):
        super().Sub(n1,n2)

    #Override
    def Sum(self,n1,n2):
        sumresult = (n1+n2)**2
        print("sum = {} ".format(sumresult))


def main():
    op = Operation()
    op.Sub(5,2)
    op.Sum(45,10)
    opmul = OprationWithMul()
    opmul.Sum(2,2)
    opmul.Sub(3,2)
    opmul.mul(4,2)



if __name__ == '__main__': main()
