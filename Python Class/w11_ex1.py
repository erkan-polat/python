while 1:
    try:
        n=input("Please enter an integer:")
        n=int(n)
        if (n%5==0 and n%6==0):
            print(str(n)+ "is divisible by both 5 and 6")
        elif (n%5==0 or n%6==0):
            print(str(n)+ "is divisible by 5 or 6, but not both")
        else:
            print(str(n)+ " is not divisible by either 5 or 6")
    except ValueError:
        print("No valid integer! Try again..!")
