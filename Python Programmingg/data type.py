#integer numbers
x = 19
y = -4
print(type(x), type(y)) 
 #float numbers
a = 12.1
print(type(a)) 
#complex number
b = 10+6j  
print(type(b))
#boolean number
c = 2>6    
print(type(c))
print(c)

#string
my_string = "Anjali"
print(my_string)
print(len(my_string)) #lenght of string
print (my_string[2:5]) #value from 2 to 5 index number

#List
Fruits = ['apple','kiwi','banana'] 
print(Fruits)
mylist = [10,20,30,'Anjali','Vadi']
print(mylist)
print(mylist[2:5])
mylist[2] = 35 
print(mylist)
mylist.append(40)
print(mylist)
mylist.insert(5,50)
print(mylist)
mylist.reverse()
print(mylist)

#Dictionary
Car = {'swift' : 'ModelA','Tata' : 'ModelB','Hyundai' : 'ModelC'}
print(Car) #this will print the value with key value pairs
print(Car['Tata']) #access the value with key value
print(Car.get('swift')) #usage of get function
Car['Tata'] = 'WahModel' #updating the value using key pair
print(Car['Tata'])

#Tuple
animals = (10,20,30,'cat','rat','horse','cat')
print(animals) #print the tuple
print(animals[2]) #print the value at index
print(animals.count('cat')) #print the number of times cat has been repeated

#Set
Mobile = {10,20,30,30,30,'iphone','nokia'}
print(Mobile)
#print(Mobile[2]) # cant access value through index number

#Range
range(10)
print(list(range(10)))

#Misc
j = [1,2,3,4]
k = {4,5,6,7}
l = [j,k]
print(l)
