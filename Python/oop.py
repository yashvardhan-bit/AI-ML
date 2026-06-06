# class laptop:
#     storage_type="SSD"
#     @classmethod #decorator to make the method a class method
#     def get_storage_type(cls):
#         print("storage type is ",cls.storage_type)
#     @staticmethod #decorator to make the method a static method
#     def cal_discount(price,discount):
#         final_price=price-(discount/100)*price
#         print("final price is ",final_price)
# l1=laptop()
# laptop.get_storage_type()
# l1.get_storage_type()
# l1.cal_discount(1000,10)
# class product:
#     count=0 #class variable
#     def __init__(self,name,price):
#         self.name=name
#         self.price=price
#         product.count+=1 #incrementing the count of products created
#     def get_info(self):
#         print(f"product name is {self.name} and price is Rs. {self.price}")
#     @classmethod
#     def get_count(cls):
#         print(f"total products createdd are{cls.count}")
#     @staticmethod
#     def cal_discounted_price(price,discount):
#         final_price=price-(discount/100)*price
#         print(f"final price after discount is Rs. {final_price}")
# p1=product("laptop",50000)
# p1.get_info()
# p2=product("mobile",20000)
# p3=product("tablet",15000)
# product.get_count()
# p1.cal_discounted_price(50000,10)
# p2.cal_discounted_price(p2.price,20)
'''1.Encapsulation'''
'''wrapping data and methods into single unit'''
# class bankAccount:
#     def __init__(self,name,balance,password):
#         self.name=name#public attribute
#         self._balance=balance#protected attribute
#         self.__password=password#private attribute
#     def get_password(self):
#         return self.__password
#     def set_password(self,new_password):
#         self.__password=new_password
# acc1=bankAccount("Alice",1000,"secret")
# # print(acc1.name) #accessing public attribute
# # # print(acc1.__password) #trying to access private attribute (will raise an error) 
# # print(acc1._balance) #accessing protected attribute (not recommended but possible)
# # print(acc1.get_password()) #accessing protected attribute (recommended)
# # acc1.set_password("new_secret") #modifying private attribute using setter method
# print(acc1.get_password()) #accessing modified private attribute
# print(acc1._bankAccount__password) #accessing private attribute using name mangling (not recommended)
'''2.inheritance'''
# class employee:
#     start_time="9:00 AM"
#     end_time="5:00 PM"
#     def change_time(self,new_end_time):
#         self.end_time=new_end_time
# class Teacher(employee):
#     def __init__(self,subject):
#         self.subject=subject
# class Role(employee):
#     def __init__(self,role_name):
#         self.role_name=role_name
# t1=Teacher("Math")
# t1.change_time("6:00 PM") #inherited method from employee class
# print(t1.start_time,t1.end_time,t1.subject) #inherited attributes from employee class
# t2=Role("manager")
# print(t2.start_time,t2.end_time,t2.role_name) #inherited attributes from employee class
# class employee:
#     start_time="9:00 AM"
#     end_time="5:00 PM"
# class admin(employee):
#     def __init__(self,role):
#         self.role=role
# class accountant(admin):
#     def __init__(self,salary,role):
#         self.salary=salary
#         super().__init__(role) #calling the constructor of admin class to initialize role attribute
# a1=accountant(24000,"CA")
# print(a1.start_time,a1.end_time,a1.role,a1.salary)
# class Teacher:
#     def __init__(self,salary):
#         self.salary=salary
# class Student:
#     def __init__(self,gpa):
#         self.gpa=gpa
# class TA(Teacher,Student):
#     def __init__(self,salary,gpa):
#         super().__init__(salary) #calling the constructor of Teacher class to initialize salary attribute
#         Student.__init__(self,gpa) #calling the constructor of Student class to initialize gpa attribute
# ta1=TA(15000,9.0)
# print(ta1.salary,ta1.gpa)
'''3.abstraction'''
'''hiding the internal details and showing only the functionality to the user'''
# from abc import ABC,abstractmethod
# class Animal(ABC):
#     @abstractmethod
#     def make_sound(self):
#         pass
# class Lion(Animal):
#     def make_sound(self):
#         print("roar")
# class Dog(Animal):
#     def make_sound(self):
#         print("bark")
# lion=Lion()
# lion.make_sound()
'''4.polymorphism'''
# class Shape:
#     def area(self):
#         print("area of shape")
# class Circle(Shape):
#     def area(self):#function overriding
#         print("area of circle is pi*r^2")
#  s1=Circle()
#  s1.area()
# class Employee:
#     def get_designation(self):
#         print("employee designation")
# class Acountant():
#     def get_designation(self):
#         print("accountant designation")
# t1=Employee()
# t2=Acountant()
# t1.get_designation() #employee designation
# t2.get_designation() #accountant designation