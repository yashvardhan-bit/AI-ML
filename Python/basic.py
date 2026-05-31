# print("HELLO WORLD")
# print("hello world\t sup!")
# name = "Yashvardhan"
# print("my name is", name)
# print(type(name))
# num=6
# isPrime=None
# print(num)
# print(type(isPrime))
# print(isPrime)
#it is a single line comment
"""this is 
a multi line comment"""
# a=2
# b=3
# print(a+b)
# print(a%b) #modulo operator gives the remainder
# print(a**b) #exponentiation operator
# print(a//b) #floor division operator
# print(a==b) #comparison operator
# print(a!=b)#not equal to operator
# print(a>b)
# print(a<b)
# print(a>=b)
# print(a<=b)

# a=5
# a=a+1
# print(a)
# a+=1 #shorthand operator for a=a+1
# print(a)
# a=False
# print(not a)
# print(a and True)
# print(a or True)
# print(not(5>3 and 2<4))
# a=10
# b=5
# print(type(a/b))
# a="10"
# a=int(a) #typecasting string to integer
# print(type(a))
# val=bool(a) #typecasting integer to boolean
# print(val, type(val))
# a=input("Enter a number: ") #taking input from user
# print("You entered", a)
# print(type(a)) #input is always of string type
# b=input("Enter another number: ")
# print(a+b) #this will concatenate the two strings instead of adding them as numbers
# a=int(a)
# b=int(b)
# print(a+b) #this will add the two numbers
# a=int(input("Enter a number: "))#floating value will give an error
# print(a)
# a,b,c=2,3,4 #multiple assignment
# print((a+b+c)/3) #average of three numbers
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
a=[1,2,3,4,5]
print(type(a) , a)
a[2]=10 #modifying an element of the list
a.append(6) #adding an element to the end of the list
print(a)
print(a[::2])
a.sort(reverse=True) #sorting the list in ascending order
print(a) #sorting the list in descending order
a.insert(2,15) #inserting an element at a specific index
print(a)
a.remove(15) #removing an element from the list
print(a)
a.pop(2) #removing an element from a specific index
print(a)