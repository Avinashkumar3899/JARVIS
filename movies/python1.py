# a = "this is my first python program"
# print( len(a))
# print("the is file is", len(a), "words")
# a=input("enter your name")
# print("your name is",a)
# b= len(a)
# if(b>= 5 ):
#  print("your name is strong")
# elif( b < 5):
#  print("good enought name")

# this is if else loop
# a=int(input("enter your age"))
# print("your age is", a)
# if(a>18):
#     print("you can watch this video")
# elif(a>15):
#     print("you can watch this movie with your parents or guardians")
# else:
#     print("you cannot watch this movie")


# this is for importing time in the code
# import time
# )

# this is for for loop
# a=" this"
# for i in a:
#     print(i)
# x=int(input("enter your number"))

# this is for while loop 
# while(x<=45):
#     x=int(input("enter your number:"))
#     print(x)
    
# print("done with the loop")
# count=5
# while(count>0):
#     print(count)
#     count=count-1

# these are for break and continue operations
# for i in range(50):
#  if(i==10):
#   continue
#  print("5 x",i+1,"=",5*(i+1))
# for i in range(20):
#     if(i==15):
#         break
#     print(5*i)

# this is for making any function in python
# def average(a=1,b=1,c=1):
#      print("the average is:", (a+b+c)/3)
# average(6,6,6)()
# def mean(a,b):
#     print("gmean=", ((a*b)/(a+b)))
# mean(6,5)


#for variable length argument
# def average(*numbers):
#     sum = 0
#     for i in numbers:
#         sum = sum + i
#     print("average is: ", sum/len(numbers))

# average(4,4,4,4,4)
# average( 5,6,7,8,9,4,3,4,5,6,7,7,7,7,6,5,4,4)


# def name(**name):
#     print(type(name))
#     print("hello,",name["fname"], name["mname"], name['lname'])

# name(lname="prasad", fname="avinash", mname="kumar")
# print(type(name))

# this code is used to find the type of any code argument
# a=int(input("enter number: "))
# if( a>0):
#     print("a is greater than zero")
# else:
#     print("a is smaller than zero")
# print(type(a))

# for list making and its operations
# lists are ordered collections of data items , they are separated by coma, and enclosed by square brackets , they can be changed.
# l=[1,2,3,3,44,5,5,3,]
# print(l)
# print(l[1:5])
# print(l[3:])
# print(l[1:-1])
# for i in l:
#     print(l)
# for l in l:
#     print(l)

# for sorting in ascending order
# l.sort()

# for sorting in descending order
# l.sort(reverse=True)
# print(l)

# for adding any item to the list in the last position
# l.append(6)
# print(l)

#for reversing the orignal list
# l.reverse()
# print(l)    

# print(l.index(1))
# print(l.count(3))
# print(l.count(9))

# this is for changing the contents in m but not in l 
# m=l.copy()
# m[1]=0
# print(l)

# l.insert(2,566)  #for changing the content of index 2 by 566 is written as(2,566)
# print(l)

#for putting the value of other list to the end of list 
# m=[222,333,444,555]  #suppose this is a list 
# l.extend(m)
# print(l)

#for merging one list to another list and creating a new list
# k=l+m
# print(k)

# for making tuples
#tuples are ordered collection of data items, they are separated by coma and enclosed in small brackets.
#difference between list and tuple is that we cannot change the elements of tuple, i.e they are unchangable
# tup=(13,66,98,"green","eduh")
# print(tup)
# print(type(tup),tup)

# count shows the no. of occurances in tuple
# tuple1=(1,2,2,3,3,4,565,34,453,544,33,4,4,5,)
#  res= tuple1.index(5)
# res = tuple1.count(3)
# print('the count of tuple1 is:',res )

#for ai chat bot for begineers

# print("welcome to chatbot.ai")
# answer = input("are oyu excited")
# if(answer=="yes"):
#     print("i am happy too")
# elif(answer=="no"):
#     print("sure,hope you are doing well")
# elif(answer=="i dont know"):
#     print("let me help you")
# else: print("i dont get you, could you please elaborate")
