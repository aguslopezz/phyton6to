from operator import indexOf


arr = []
i = 1
for i in range(0, 1000):
    arr.append(i)


for e in arr:

    if e % 2 != 0:
        print(e, ": impar")
    else:
        print(e ,": par")
        arr.pop(arr.index(e))
        
        

print(arr)