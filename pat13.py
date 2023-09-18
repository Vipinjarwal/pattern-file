n = int(input("enter no of rows: "))


# full dimond pattern
for i in range(n):
    print(" "*(n-i-1), end= " ")
    for j in range(i+1):
        print(chr(65+j),end=" ")
    print()


for i in range(n):
    print(" "*(i+1), end=" ")
    for j in range(n-i-1):
        print(chr(65+j), end=" ")
    print()


#  * pattern


for i in range (n):
    print(" "*(n-i-1)+ "* "*(i+1))
    
for i in range(n-1):
    print(" "*(i+1)+ "* "*(n-i-1))
