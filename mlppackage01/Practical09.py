import datetime
import os
now = datetime.datetime.now()
d = input("enter the prefix")
os.mkdir("Assingment1")
os.chdir("Assingment1")
print("os.getcwd()=",os.getcwd())
a =str(now.year)
b =str(now.month)
count =1
while(count<=100):
    os.mkdir(a+b+d+str(count))
    count =count+1






