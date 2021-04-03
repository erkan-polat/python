numbers = [1,5,2,3,4]
print("Numbers" , numbers)
inc_num=numbers.copy()
inc_num.sort()
print("Numbers increasing order" ,inc_num)
print("Originally order",numbers)
inc_num.reverse()
print("Numbers decreasing order" ,inc_num)
print("Originally order",numbers)
numbers.reverse()
print("Originally reversed order",numbers)
numbers.sort()
print("Sort numbers increasing order : " ,numbers)
numbers.reverse()
print("Sort numbers decreasing order : " ,numbers)




