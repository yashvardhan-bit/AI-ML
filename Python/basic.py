print("HELLO WORLD")
print("hello world\t sup!")
name = "Yashvardhan"
print("my name is", name)
print(type(name))
num=6
isPrime=None
print(num)
print(type(isPrime))
print(isPrime)
# it is a single line comment
"""this is 
a multi line comment"""
a=2
b=3
print(a+b)
print(a%b) #modulo operator gives the remainder
print(a**b) #exponentiation operator
print(a//b) #floor division operator
print(a==b) #comparison operator
print(a!=b)#not equal to operator
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)

a=5
a=a+1
print(a)
a+=1 #shorthand operator for a=a+1
print(a)
a=False
print(not a)
print(a and True)
print(a or True)
print(not(5>3 and 2<4))
a=10
b=5
print(type(a/b))
a="10"
a=int(a) #typecasting string to integer
print(type(a))
val=bool(a) #typecasting integer to boolean
print(val, type(val))
a=input("Enter a number: ") #taking input from user
print("You entered", a)
print(type(a)) #input is always of string type
b=input("Enter another number: ")
print(a+b) #this will concatenate the two strings instead of adding them as numbers
a=int(a)
b=int(b)
print(a+b) #this will add the two numbers
a=int(input("Enter a number: "))#floating value will give an error
print(a)
a,b,c=2,3,4 #multiple assignment
print((a+b+c)/3) #average of three numbers
'''conditional statements'''
# age=int(input("Enter your age:"))
# if age>=18:
#     print("eligible to vote")
# else:
#     print("not eligible to vote")
# color=input("Enter a color: ")
# if color=="red":
#     print("stop")
# elif color=="yellow":
#     print("get ready")
# elif color=="green":
#     print("go")
# else:
#     print("invalid color")
# '''age'''
# age=int(input("Enter your age: "))
# if age in range(0,13):
#     print("child")
# elif age in range(13,20):
#     print("teenager")
# else:
#     print("adult")
# a="admin"
# p="password123"
# username=input("Enter your username: ")
# password=input("Enter your password: ")
# if username==a and password==p:
#     print("login successful")
# elif username!=a:
#     print("invalid username")
# elif password!=p:
#     print("invalid password")
'''practice problem'''
# n=int(input("Enter a number: "))
# if n%2==0:#reminder=0
#     print("even")
# else:
#     print("odd")
'''nesting'''
# u="admin"
# p="password123"
# username=input("Enter your username: ")
# password=input("Enter your password: ")
# if username==u and password==p:
#     print("login successful")
# else:
#     if username!=u:
#         print("invalid username")
#     else:
#         print("invalid password")
'''match case statement'''
#alternative to if-elif-else statement
# color=input("Enter a color: ")
# match color:
#     case "red":
#         print("stop")
#     case "yellow":
#         print("get ready")
#     case "green":
#         print("go")
#     case _:
#         print("invalid color")
'''loops'''
'''while loop'''
# while 1<2:
#     print("infinite loop")
# i=1 #iterator variable
# while i<=5:
#     print("hello", i)
#     i+=1
# print("loop ended")
'''practice problem'''
# i=5
# while i>0:
#     print(i)
#     i-=1
# print("loop ended")
'''table of a number'''
# n=int(input("Enter a number: "))
# i=0
# while i<10:#0-9
#     print(n*(i+1))
#     i+=1
# print(f"table of {n}")
'''break and continue'''
# i=1
# while i<=10:
#     if i%6==0:
#         break #breaks the loop when i is divisible by 6
#     print(i)
#     i+=1
# print("loop ended")
# i=1
# while i<=10:
#     if i%6==0:
#         i+=1
#         continue
#     print(i)
#     i+=1
# print("loop ended")
# i=1
# while i<=10:
#     if i%2==0:
#         i+=1
#         continue
#     print(i)
#     i+=1
# print("loop ended")
'''for loop'''
# st="hello"
# if "hell" in st:
#     print("hell exists in hello")
# for i in range(10): #0-9
#     print(i+1)#1-10
# for i in range(5):
#     print("5 baar badmashi", i+1)
# word="artificial intelligence"
# count=0
# for ch in word:
#     if ch=="i":
#         count+=1
# print(count)
# word="artificial intelligence"
# count=0
# for ch in word:
#     if (ch =="a" or ch =="e" or ch =="i" or ch =="o" or ch =="u"): #checking for vowels
#         count+=1
# print(count)
# for i in range(1,11,2):
#     print(i)
# n=int(input("Enter a number: "))
# sum=0
# for i in range(1,n+1):
#     sum+=i
# print(sum)
'''functions'''
# def hello():
#     print("hola")
# hello()  #function call
# def sum(a,b):
#     return a+b
# result=sum(2,3) #function call with arguments
# print(result)
# a=int(input("Enter a number: "))
# b=int(input("Enter another number: "))
# c=int(input("Enter a third number: "))
# def avg(a,b,c):
#     sum=a+b+c
#     return sum/3
# print(avg(a,b,c))
# def sum(a,b=12):
#     return a+b
# print(sum(1)) #using default value of b
# print(sum(1,2)) #overriding default value of b
'''lambda function'''
# avg= lambda a,b:(a+b)/2 #anonymous function that adds two numbers
# print(avg(12,1213))
# sum=lambda a,b:a+b
# print(sum(3,4))
# def factorial(n):
#     fact=1
#     for i in range (1,n+1):
#         fact*=i
#     return fact
# print(factorial(5))
'''assignment'''
# salary= int(input("Enter your salary: "))
# if salary<30000:
#     print("tax is =",salary*0.05)
# elif salary<70000:
#     print("tax is =",salary*0.15)
# elif salary>70000:
#     print("tax is =",salary*0.25)
# i=int(input("Enter a number: "))
# j=int(input("Enter another number: "))
# for num in range(i,j+1):
#     if num%2==0:
#         print(num)
# n=123
# for i in str(n):
#     print(i)
# print(n%10,n%100//10,n//100)
# n=str(input("Enter a number: "))
# print(len(n))
# a='yashvardhan'
# print(a[1])
# for i in a:
#     print(i)
# print(a[-1:0:-1])
# print(a[::-1])
# print(a[-1::-1])
# print(a[-1:0])
# a=10
# b=20
# sum=a+b
# print(f"sum of {a} and {b} is : {sum}")#f function
# print("sum is {}".format(sum))# format function
# print("sum of {} and {} is {}".format(a,b,sum))#format function with multiple placeholders
# print("sum of {1} and {0} is {2}".format(a,b,sum))#format function with indexes
'''list'''
# a=[1,2,3,4,5]
# print(type(a) , a)
# a[2]=10 #modifying an element of the list
# a.append(6) #adding an element to the end of the list
# print(a)
# print(a[::2])
# a.sort(reverse=True) #sorting the list in ascending order
# print(a) #sorting the list in descending order
# a.insert(2,15) #inserting an element at a specific index
# print(a)
# a.remove(15) #removing an element from the list
# print(a)
# a.pop(2) #removing an element from a specific index
# print(a)
# a.clear() #removing all elements from the list
# print(a)
# a=[1,2,3,4,5]
# for i in a:
#     print(i)
# x=5
# for i in a:
#     if i==x:
#         print("found")
#         break
#     i+=1
# else:
#     print("not found")
'''tuple'''
# t=(1,2,3,4,5)
# print(type(t), t)
# # t[2]=10#tuples are immutable, we cannot modify an element of a tuple
# # print(t)
# sum=0
# for ch in t:
#     sum+=ch
# print(sum)
# print(t.index(3)) #returns the index of the first occurrence of 3 in the tuple
# print(t.count(3)) #returns the number of times 3 occurs in the tuple
'''dictionary'''
d={
    "name":"yashvardhan",
    "age":21,
    "city":"pilani",
    "marks":[90,95,85]
}
# print(type(d), d)
# print(d["name"]) #accessing a value using its key
# d["age"]=20 #modifying a value using its key
# print(d)
# print(d.keys()) #returns all the keys of the dictionary
# print(d.values()) #returns all the values of the dictionary
# print(d.items()) #returns all the key-value pairs of the dictionary
# print(d.get("name")) #returns the value of the specified key
# d.update({"name":"yash"})
# print(d.get("name")) #returns the updated value of the specified key
'''sets'''
a={1,2,2,3,4,4,5}
# print(type(s), s) #sets do not allow duplicate values
# a={}
# print(type(a), a) #this is an empty dictionary, not an empty set
# a=set ()
# print(type(a), a) #this is an empty set
 # a.add(1) #adding an element to the set
# print(a)
# a.remove(1) #removing an element from the set
# print(a)
# a.pop() #removing random element
# print(a)
# a.clear() #removing all elements from the set
# print(a)
# a={1,2,3,4,5}
# b={4,5,6,7,8}
# print(a.union(b))  #returns a new set that contains all the elements of both sets
# print(a.intersection(b)) #returns a new set that contains only the common elements of both sets
# print(a.difference(b)) #returns a new set that contains only the elements that are in
info={
    ("Alice","Math"),
    ("Bob","Science"),
    ("Alice","Science"),
    ("Charlie","Math"),
    ("Bob","Math"),
    ("Alice","English"),
    ("Charlie","English"),
}
# unique_courses=set()
# for tup in info:
#     unique_courses.add(tup[1]) #tup[1] is the course name
# print(unique_courses)
# for name, courses in info:#unpacking the tuple into name and courses
#     # print(name, courses)
#     if courses=="English":
#         print(name)
# dict={}
# for name, course in info:
#     if dict.get(name) is None:
#         dict.update({name:set()})
#         dict[name].add(course)
#     else:
#         dict[name].add(course)
# print(dict)
'''oop'''
'''class'''
# class student:
#     subject="python"
#     college="bkbirla college"
#     year="fourth"
# a=10
# stu1=student()
# stu2=student() #creating an object of the student class
# print(stu1) #accessing the class variable using the object
# print(stu2.subject,stu2.college,stu2.year) #accessing the class variable using the object
# class student:
#     def __init__(self):
#         print("constructor called")
# stu1=student() #constructor is called when an object is created
# stu2=student() #constructor is called when an object is
# class student:
#     college="bkbirla college" #class variable
#     def __init__(self,name,cgpa):
#         self.name=name #instance variable
#         self.cgpa=cgpa #instance variable
#     def get_cgpa(self):
#         return self.cgpa
# st1=student("yash",8.5) #constructor is called when an object is created
# print(st1.name,st1.cgpa) #accessing the instance variable using the object
# print(st1.get_cgpa()) #accessing the instance variable using the method
# print(student.college) #accessing the class variable using the class name
# print(st1.college) #accessing the class variable using the object
# class laptop:
#     storage_type="SSD"
#     def __init__(self,RAM,storage):
#         self.RAM=RAM
#         self.storage=storage
#     def get_info(self):
#         print(f"laptop has {self.RAM} GB RAM and {self.storage} GB storage {self.storage_type}")
# l1=laptop(16,512)
# l1.get_info()
# try:
#     x= int(input("Enter a value: "))
#     ans=10/x
# except ZeroDivisionError:
#     print("not divisible by zero")
# except ValueError:
#     print("invalid input")
# else:
#     print(ans)
# finally:
#     print("end of program")
# squares=[]
# print(type(squares)) #
# for i in range(6):
#     squares.append(i**2)
# print(squares)
# sq=[i*i for i in range(6) if i%2!=0]
# print(sq)
# a=[-2,-4,-3,5,2,-1]
# a=[0 if i<0 else i for i in a]
# print(a)
# words=["hello","world","python"]
# words=[word.upper() for word in words] # change the words to uppercase
# print(words)
# import json
# json_str='{"name":"yash","age":21,"is_sigma":true}'
# print(type(json_str))
# py_obj=json.loads(json_str)
# print(type(py_obj),py_obj)
# import json
# py_obj={
#     "name":"yash",
#     "age":21,
#     "is_sigma":True,
#     "aura_lost":None
# }
# json_str=json.dumps(py_obj) 
# print(type(json_str),json_str) 
# import json 
# d={  
#     "name":"yash",
#     "age":21,a
#     "is_sigma":True
# }
# with open("data.json","w") as f: 
#     # py_obj=json.load(f)
#     # print(type(py_obj),py_obj)
#     json.dump(d,f,indent=4,sort_keys=True)  