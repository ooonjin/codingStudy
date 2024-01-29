a=[1,5,4,2,3]

target = min(a)

for i in range(len(a)):

    a1 = a[i]

    if a1 > target:
        target = a1
    
print(target)