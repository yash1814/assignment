#with temp
a=input("Enter value:")
b=input("Enter value:")
temp=a
a=b
b=temp
print("a:",a)
print("b:",b)

#without temp
x=input("Enter value:")
y=input("Enter value:")
x,y=y,x
print("x:",x)
print("y:",y)
