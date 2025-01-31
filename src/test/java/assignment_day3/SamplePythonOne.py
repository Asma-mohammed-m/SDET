"""
print("Hello")
a=5
b=15
print("sum is:" +str(a+b))
print("difference is:" +str(a-b))
print("product is:" +str(a*b))
print("division is:" +str(a/b))
print("modulus is:" +str(a%b))
print("exponential is:" +str(a**b))
print("floor division is:" +str(a//b))

x = 8 #input("Enter a number: ") #2 will go for infinite loop-check on that
y = 4 #input("Enter another number: ")
print("you entered: " +str(int(x) + int(y)))

if x > y:
    print("x is greater than y")
    print("check if")
elif x < y:
    print("x is smallar than y")
    print("check elif")
else:
    print("x and y are equal")
    print("check else")
    
for i in range(10):
    print(i)
for i in range(10,20,2):
    print(i)
for i in range(10,0,-1):
    print(i)
while x<10:
    print(x)
    x += 1
    
mylist = ['Aaqil', 8, 'Chennai', '2nd']
print(mylist)
print(mylist[0])
print(mylist[1:])
print(mylist[1:3])
print(mylist[:-3])
print(mylist[:-2])
print(mylist[:-4])
print(mylist[-1:])

name = 'Asma'
print(name)
#reverse
print(name[::-1])

mylist.append('Java')
print(mylist)
mylist.remove('Chennai')
print(mylist)
mylist.remove(mylist[1])
print(mylist)
#mylist.remove(mylist[1:3])
mylist.reverse()
print(mylist)
mylist.sort(reverse=True)
print(mylist)

for x in mylist:
    print(x)
print(type(mylist))

for x in enumerate(mylist):
    print(x)
    
for index, value in enumerate(mylist):
    print(index, value)
    
print(len("aaqilSidraAli"))

mytuple = (23, 34)
#print(mytuple)
mytuple = (23, 43, 28, 'Asma')
print(mytuple)

def sum(a,b):
    return a + b

result = sum(10,20)
print("sum: " +str(result))  """


"""
number = 1
count = input("Enter a number ")
print(count.isdigit())
for i in range(int(count),0,-1):
# number=i*(i-1)*(i-2)*(i-3)
    number = number * i
print("fact is : "+str(number))

#factorial
#number = 1
def fact(number):
    #number = 1
    #count = input("Enter a number ")
    #print(count.isdigit())
    for i in range(int(count),0,-1):
    # number=i*(i-1)*(i-2)*(i-3)
        number = number * i
print("fact number: "+str(number))

while True:
    count = input("Enter a number ")
    if(count.isdigit()):
        fact(1)
        #print(fact())
        break
    else:
        print("Not a digit")    """

"""      
mydict = {
    'name' : 'Asma',
    'course' : 'Python',
    'year'  : 2025
}
print(mydict.items())
mydict["name2"] = "Mohammed"
print(mydict.items())
mydict["year"] = 2027

mydict.pop("year")
mydict.update({"year": 2030})
print(mydict.items())
print(mydict.keys())
print(mydict.values())
print(mydict["name"])

"""
"""    
mydict = {
    'name' : 'Asma',
    'course' : 'Python',
    'year'  : 2025
}

for x in mydict.items():
    print(x)  
print("**************") 
for x in mydict.keys():
    print(x) 
print("**************") 
for x in mydict.values():
    print(x)
print("**************") 
for x ,y in mydict.items(): 
    print(x) 
print("**************") 

"""
"""
myset = {1, 3, 4, 6,3, 6, 9}
print("Myset: " +str(myset))

myset.add(10)
print("Myset: " +str(myset))
myset.remove(3) #it will work only if myset has value else throw error
print("Myset: " +str(myset))
myset.discard(22) #it will work either have or have not values
print("Myset: " +str(myset))
#myset.update(2, 5)
myset.clear()
print("Myset: " +str(myset))

set1 = {1, 2, 4, 8}
set2 = {4, 7, 2, 9}
print(set1.union(set2))
print(set1.intersection(set2))
"""


    
print("Done!")
