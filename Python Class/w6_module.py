import math
import random
import string

def pisagor(x,y):
    hip=((x**2)+(y**2))**0.5
    print(hip)

def taxi(km):
    dist=math.ceil((km*1000)/140)
    cost=4.00+dist*0.25
    print(cost)
    
def sorted_list(a,b,c):
    lst=[a,b,c]
    lst.sort()
    print(lst[1])
    
def license_plt():
    digit1=random.randint(0,9)
    digit2=random.randint(0,9)
    number=random.randint(0,99)
    letter1=random.choice(string.ascii_letters)
    letter2=random.choice(string.ascii_letters)
    letter3=random.choice(string.ascii_letters)
    print("License plate="+str(digit1)+str(digit2)+letter1.upper()+letter2.upper()+letter3.upper()+str(number))
