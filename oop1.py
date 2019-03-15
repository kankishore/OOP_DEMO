from datetime import time
from datetime import datetime

class Teacher():
    HEAD_MASTER=""



class Student():

    #Class Variables
    SCHOOL_NAME="SN"
    UNIFORM_COLOR="BLUE"
    WORKING_DAYS=250
    #START_TIME=time.strftime('9:30:00','%H:%M:%S')

       #Instance Variables
    def __init__(self,cls,rno):
        self.CLASS=cls
        self.ROLL_NO=rno

s1=Student("I","25")
s2=Student("II","50")

print(type(s1))
print(type(s2))

print(s1.SCHOOL_NAME)
print(s2.SCHOOL_NAME)

print(s1.ROLL_NO)
print(s2.ROLL_NO)
print(s1.CLASS)
print(s2.CLASS)

print(isinstance(s1,Teacher))

t1=Teacher()
print(isinstance(t1,Teacher))