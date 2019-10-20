retstring = []
b = 4
x = 5
def printAllKLength(set, k): 
    n = len(set)  
    printAllKLengthRec(set, "", n, k) 
  
def printAllKLengthRec(set, prefix, n, k):   
    if (k == 0) : 
        retstring.append(prefix)
        return
  
    for i in range(n): 
        newPrefix = prefix + set[i] 
        printAllKLengthRec(set, newPrefix, n, k - 1) 
  
      
 
set2 = []


for i in range(b+1):
    set2.append(chr(i+97))

while (len(retstring) < x):
    for i in range(5):
        printAllKLength(set2,i)


print(''.join(retstring))
print(''.join(retstring)[x])
