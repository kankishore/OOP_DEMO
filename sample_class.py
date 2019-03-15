class Engineer():
    #Assumptions

    #Class Variables
    _COLLEGE_NAME="KSR"
    WEBSITE="www.ksrm.com"
    _UNIVERSITY="JNTUA"

    #Values have to be assigned at the time of object creation
    def __init__(self,rno,br,agg):
        self.ROLL_NO=rno
        self.BRANCH=br
        self.AGGREGATE=agg
        print("Er. Created with Roll#-",self.ROLL_NO," Branch:",self.BRANCH," with Aggregate ",self.AGGREGATE,'Percentage')

    def getAggregate(self):
        return self.AGGREGATE

    def getUniversity(self):
        return self._UNIVERSITY

e1=Engineer(201,"MECH",72)
e2=Engineer("202", "ECE",77)

print(e1.AGGREGATE)
e1_agg=e1.AGGREGATE=80
print(e1_agg)
print(e1.getAggregate())


# if e1.AGGREGATE>e2.AGGREGATE:
#     print("E1 scored more than E2")
# else:
#     print("E2 Scored more than E1")

print(e1._COLLEGE_NAME)
print(e2._COLLEGE_NAME)
print(e1._UNIVERSITY)
print(e2._UNIVERSITY)
e1._UNIVERSITY="AU"
print(e1._UNIVERSITY)
print(e1.getUniversity())
print(e2.WEBSITE)

print(e1==e2)

b=isinstance(e2,Engineer)
print(b)
print(type(b))