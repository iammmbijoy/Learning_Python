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

#Binary types: bytes, bytearray, memoryview
#bytes() function returns a bytes object. A bytes object is an immutable sequence of integers in the range 0 <= x < 256.

binaryList = [1, 2, 3, 4, 5, 121] # max 0 to 255
b = bytes(binaryList)
print(type(b)) # for compress image or work in image we use bytes data type.

#byteArray() function returns a bytearray object. A bytearray object is a mutable sequence of integers in the range 0 <= x < 256.

byteArrayList = [1, 2, 3, 4, 5, 121] # max 0 to 255
b1 = bytearray(byteArrayList)
#b1[1] = 100
print(b1[1])
print(type(b1)) 

#None type: NoneType

x = None
print(x)
print(type(x))  #None is a data type of its own (NoneType) and used to define a null value or no value at all. It is not the same as 0, False, or an empty string.

#Sequence types: list, tuple, range

li = ['Ashikuzzaman', 'Bijoy', 'Fardin', 'Alvee'] #it is mutable and can be changed after creation.
li[0] = 'Nazmul'
print(li)
print(type(li)) 

tupleType = ('5', '10', '20', 'Alvee') #it is immutable and cannot be changed after creation.
# tupleType[0] = 'Nazmul'  #this will give an error because tuple is immutable    
print(tupleType)
print(type(tupleType))  

rangeType = range(6) #it is immutable and cannot be changed after creation.
for i in rangeType:
    print(i)  #this will print the numbers from 0 to 5
print(rangeType)        
print(type(rangeType))  

#Mapping types: dict
#Set types: set, frozenset

