n = int(input("enter n value: "))

for i in range(n):
    print("_"*(n-i-1)+ "*", end="")
    if i >= 1:
        print("-"*(2*i-1)+ "*",end="")
    print()    

for i in range(n):
    print("_"*(i) + "*", end="")
    if i !=(n-1):
        print("-"*(2*n-2*i-3)+"*",end=" ")
    print()    
    