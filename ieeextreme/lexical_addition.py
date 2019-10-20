x = input()

xarr = x.split()

n = int(xarr[0])
a = int(xarr[1])
b = int(xarr[2])

flist = []


if ((2*a)<=n):
    for i in range(b,a-1,-1):
        while(n>0):
            if (i >n):
                i -= 1
            elif (((n-i) < (a)) and (i!=a)):
                i -= 1 
            if (i>n and n in list(range(b,a-1,-1))):
                i=n
            n -= i
            flist.append(i)
            

flist.sort()

if (len(flist)==0):
    print('NO')
else:
    print('YES')
    for i in flist:
        print(i,end=' ')

print()