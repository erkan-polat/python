import random
import os

while True:
    x=int(input("To create file (1), to read (2), threshold(3), Exit(4) : "))  
    if x==1:
        f= open("sensordata.txt","w")
        numbers=[]
        for i in range(0,100):
            numbers.append(random.randint(0,100))
            f.write(str(numbers[i])+"\n")  
        f.close()
    elif x==2:
        f=open("sensordata.txt","r")
        for i in range(0,100):
            number=f.readline()
            number=number[:-1]
            numbers.append(int(number))
        print("Max value is : ", max(numbers), " Min value is : " ,min(numbers), "Average is : ",sum(numbers)/len(numbers))
        f.close()
    elif x==3:
        os.remove("sensordata.txt")
        f=open("sensordata.txt","w")
        tr=int(input("Enter a number : "))
        i=0
        while (i<len(numbers)):
            if numbers[i]>tr:
                del numbers[i]
            else:
                i=i+1
        for i in range(0,len(numbers)):
            f.write(str(numbers[i])+"\n")
        f.close()
    elif x==4:
        break
        
        
        
