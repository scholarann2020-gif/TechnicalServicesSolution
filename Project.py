print ("Hello")

class Student():
 def __init__(self,name,age,idNumber):
    self.name = name
    self.age = age
    self.idNumber = idNumber

    print(name)
    print(age)
    print(idNumber)

p1 = Student("John",20,2)
p2 = Student("JAMIL ",20,4)

print(p1.name,p1.age,p1.idNumber)
print(p2.name,p2.age,p2.idNumber)
