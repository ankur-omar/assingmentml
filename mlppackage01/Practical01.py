import math
print(math.ceil(4.1))#print the greater number as compare to given number as a input
print(math.ceil(5.0))#print the greater number as compare to given number as a input
print(math.ceil(3.5))#print the greater number as compare to given number as a input
print(math.ceil(4.9))#print the greater number as compare to given number as a input
# return the floor of x as a floot
# the largest integer value less than the x
print(math.floor(4.6))

#math.pow(x,y) : return x raised to pow y
print("math.pow(2,4)=",math.pow(2,4))
#math.fabs(x) :return the absolute value of x
print("math.fabs(-5.1)=",math.fabs(-5.1))
#log function
print("math.log(8,2)=",math.log(8,2))
#sqrt function
print("math.sqrt(25)=",math.sqrt(25))



#import is use for import the helping library
import os
print("os.name=",os.name)
#output nt- new technologie
print("os.getenv('path')=",os.getenv('path'))
#  show the position of current working directory
print("os.getcwd()=",os.getcwd())
# cwd->creating a folder or make directory
#os.mkdir("ankurdir")
# chdir->change the directory
os.chdir("ankurdir")
# print the folder we have created
print("os.getcwd()=",os.getcwd())
# delete the folder (.. means 1 level up then delete the folder)
os.chdir("..")
os.rmdir('ankurdir')
print("folder deleted.")


# fetch the system information
import sys
print("sys.version = ",sys.version)
print("sys.version_info = ",sys.version_info)
print("sys.platform = ",sys.platform)
print("sys.path = ",sys.path)


# program for all arithematic operation

a = int(input("enter first number"))
b = int(input("enter the second number"))
s = a+b
print("addition of ",a,b," is equal to",s)
s =a*b
print("multiplication of ",a,b," is equal to",s)
s =a-b
print("subtraction of ",a,b," is equal to",s)
s = a/b
print("division of ",a,b," is equal to",s)
