# Top hollow dimond pattern

n = int(input("enter no of rows: "))

# * Pattern

for i in range(n):
    print("  "*(n-i-1)+ "* ",end="")
    if i >=1:
        print("  "*(2*i-1 )+ "*", end="")
    print()    
    
    
# acs order alphabet pattern 
for i in range(n):
    print("_"*(n-i-1)+(chr(65+i)),end="")
    if i >=1:
        print("-"*(2*i-1)+(chr(65+i)),end="") 
    print()

for i in range(n):
    print("  "*(n-i-1)+(chr(65+i)),end="")
    if i >=1:
        print("  "*(2*i-1)+(chr(65+i)),end="") 
    print()                         