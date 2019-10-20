#equation: (X^(goog+T)) mod 10^Y

#solution if y equals 1:
    #if x mod 10 equals 1, you have to minimize ((x mod 100 mod 10) * (T mod 10)) mod 10 

# for example input '31 1', 3 * (T mod 10) has to be least

n = input()
xylist = []
xylist2 = []
for i in range(int(n)):
        xy = input()
        xylist.append(xy)

for i in xylist:
    a = i.split()
    xylist2.append(a)

def func(x,y,t):
    return ((x**t) % (10**y))

def magic(x,y):
    array = []
    for i in range(y,10):
        array.append(func(x,y,i) % (100**y))
        return min(array)



for i in xylist2:
    print(magic(int(i[0]),int(i[1])))

