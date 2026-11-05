#Test type: str (write text in single or double quotes)
namcode = "Bijoy123"
print(namcode)
print(type(namcode))

namcode2 = 'Bijoy123'
print(namcode2)

#Numeric types: int, float, complex
inttype = 84
print(inttype)
print(type(inttype))

yourName = "Ashikuzzaman"
myName = "Bijoy"
print(yourName + myName)  #concatenation of two strings
print(yourName * 3)  #repetition of string
print("My name is " + myName)
print("My name is" + ' ' + myName)  #concatenation of string with space     

floatingType = 3.14
print(floatingType)
print(type(floatingType))   

#complexType = 420i (just j is used in python to represent complex numbers)
complexType = 420j
print(complexType)  
print(type(complexType))    # when we input a data by default it is considered as string type.

#Boolean type: bool
booleanType = True # Python is case-sensitive so True and true are different. True is a boolean value but true is a string.
print(booleanType)
print(type(booleanType))    

x = 10
y = 10

x > y
print(x > y)  #comparison operator returns boolean value
print(x == y)
#Sequence types: list, tuple, range
#Mapping types: dict
#Set types: set, frozenset
#Binary types: bytes, bytearray, memoryview
#None type: NoneType
