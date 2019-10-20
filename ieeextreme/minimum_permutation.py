first = input()

arr = input().split()
b = input().split()
b.sort()

def magic(ls,num):
    #print(list(range(0,len(ls))))
    brute = []
    for i in range(0,len(ls)+1):
        temp = []
        for j in ls:
            temp.append(j)
        temp.insert(i,num)  
        brute.append(int(''.join(temp)))
    return min(brute)

def split(word): 
    return [char for char in word]  

for i in b:
    if (b.index(i) != len(b)-1):
        magic(arr,i)
        arr = split(str(magic(arr,i)))
    else:
        final = (split(str(magic(arr,i))))

for i in final:
    print(i,end=' ')