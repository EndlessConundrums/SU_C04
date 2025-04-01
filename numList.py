numList = [5,4,6,10,222,67,0,42]
for i in numList:
    if i % 2 == 1:
        continue
    if i > 10:
        break
    print(i)