a = 7
if a>1:
    for x in range(2,a):
        if(a%x)==0:
            print("NOT PRIME")
            break
        else:
            print("Prime")       
else:
    print("value of a <=1")

            