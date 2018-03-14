
def  main():
    Student = {"name":"zaid","age":24,"slary":20130}
    print(Student,type(Student))
    print(Student["name"])
    print(Student["slary"])

    #a new way to dictionary
    StudentNew = dict(name="zaid",age=30,slary = 2019)
    print(StudentNew)
    print(StudentNew['slary'])
    print(StudentNew['age'])
    StudentNew['age'] = 28
    StudentNew['dep'] = "CS"
    print(StudentNew)
    del StudentNew['dep']
    print(StudentNew)


if __name__ == '__main__':main()
