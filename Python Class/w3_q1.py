s= "Hello there! what should this string be?"

print("Length of string s = ",len(s))
print("İndex of first a = ",s.find('a'))
print("Count of letter a = ",s.count('a'))
print("First five char = ",s[0:5])
print("Next five char = ",s[5:10])
print("13th char = ",s[12])
print("Chars with odd index = ",s[1:len(s):2])
print("Last five char = ",s[-6:-1])
print("String Upper = ",s.upper())
print("String Lower = ",s.lower())
print("Start with 'str'  " if s.startswith('str') else "not starts with 'str'")
print("Start with 'str'  " if s.endswith('ome') else "not ends with 'ome'")
print("Split ' ' = ",s.split(' '))

