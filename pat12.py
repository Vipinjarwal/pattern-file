n = int(input("enter no of rows: "))

#  acs order alphabets down piramet pattern

for i in range(n):
    print(" "*i, end="")
    for j in range(n-i):
        print(chr(65+j),end=" ")
    print()    

# * pattern

for i in range(n):
    print(" "*i, end=' ')
    for j in range(n-i):
        print("*", end=" ")
    print()      