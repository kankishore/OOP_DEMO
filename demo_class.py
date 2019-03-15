class Employee():

    #one Special method called __init__(). This is similar to a constructor in Java
    # It executes at the time of creating an object/instance
    def __init__(self,E_ID,E_NAME,E_DEPT):
        print("Executing init")
        EID=E_ID
        NAME=E_NAME
        DEPT=E_DEPT
        print("Employee Created - ",EID)

    def not_init(self):
        print("this is not __init__()")


e1=Employee("101",'Charles',"IT")
e2=Employee("102",'Blake','MKT')
e3=Employee("103",'Ben','''IT''')
e4=Employee("104",'Jane','IT')

e1.not_init()

a='5'
b='5'
print('a'+'b')


sal=30000*1.1
print('''My Monthly Salary is ''',sal,'/- Rupees')
print('''My Annual Salary is ''',sal*12,'/- Rupees')