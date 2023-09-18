n = int(input("enter n value: "))

for i in range(n):
    print("__"*(n-i-1),end="")
    for j in range(i+1):
        print(str(j+1),end=" ")
    print()    
  
 
for i in range(n-1):
    print("__"*(i+1),end="")
    for j in range(n-i-1):
        print(str(j+1),end=" ")
    print() 
    
    

# * pattern 

for i in range(n):
    print("__"*(n-i-1)+"* "*(i+1))

for i in range(n-1):
    print("__"*(i+1)+"* "*(n-i-1))    