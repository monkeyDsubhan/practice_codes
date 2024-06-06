class Student:
    def __init__(self,name,roll_number,password):
        self.name=name #public
        self._roll_number=roll_number #protected attribute
        self.__password=password #Private attribute
    def display_details(self):
        print("Name:",self.name)
        print("Roll Number:",self._roll_number)
        #Private attribute accessed within class
        print("Password:",self.__password)
    def get_password(self):
        return self.__password
    def set_password(self,new_password):
        self.new_password=new_password


student=Student("Subhan","007","NIka")
# print("Name (PUBLIC)",student.name)
# # ACCESSING PROTECTED ATTRIBUTES (NOT RECCOMMENED)
# print("Roll Number(Protected):",student._roll_number)

print("Password",student.__password)

# print("Password (Private):",student.get_password())

# print("Password (Private):",student.set_password("om123"))
student.display_details()




