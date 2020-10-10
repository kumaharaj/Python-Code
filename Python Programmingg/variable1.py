c = 20         #global variable C
def func():    #defining function func
    c = 10     #Redefining variable C, this is called local variable because it is present under a function
    print(c)   #printing local value of variable C
func()         #calling function which is defined 
print(c)       #printing the global variable
#this program will print both the local and global value of variable C
# If you remove the last time, it will only print local value of variable c which is 10
#if you remove print(c) in line 4 then the global value will be printed