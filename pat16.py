# Bottom hollow dimond pattern

n = int(input("enter no of rows: "))

# * Pattern


for i in range(n):
    print(" "*i + "* ", end="")
    if i !=(n-1):
        print(" "*(2*n-2*i-3)+"*",end=" ")
    print()    
    
    
 
for i in range(n):
    print("_"*i+ chr(65+i), end="")
    if i !=(n-1):
        print("-"*(2*n-2*i-3)+chr(65+i),end="")
    print()       