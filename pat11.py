n = int(input("enter no of rows: "))

# acs order alphabets half dimond pattern print
 
for i in range(n):
    for j in range(i+1):
        print(chr(65+j), end=' ')
    print()    

for i in range(n-1):
    for j in range(n-i-1):
        print(chr(65+j), end=' ')
    print()        
    
    
# * half dimaond pattern print
 
for i in range(n):
    print("* "*(i+1))
    
for i in range(n-1):
    print("* "*(n-i-1))        
    
  