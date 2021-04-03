P=10000
n=12
r=0.08
t_str=input("Number of years ? =")
t_float=float(t_str)

A=P*(1+(r/n))**(n*t_float)
print("Amount = ",A)
