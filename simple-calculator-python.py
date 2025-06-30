#calculater project:
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b): 
    return a*b
def div(a,b):
    return a/b
def avg(a,b):
    return (a+b)/2

print("plz select a operation:\n" "1.add\n" "2.sub\n" "3.mul\n" "4.div\n" "5.avg")

select = int(input("select a operation from 1,2,3,4,5:"))
a=int(input("enter first no:"))
b=int(input("enter second no:"))

if select==1:
    print(add(a,b))
    
elif select==2:
    print(sub(a,b))
    
elif select==3:
    print(mul(a,b))
    
elif select==4:
    print(div(a,b))
    
elif select==5:
    print(avg(a,b))
    
else:
    print("Invalid operation!")