#funkyNumList = [(5, 3), (2, 7), (4, 8), (10, 11)]
#funkySortedList = sorted(funkyNumList, key=lambda x: x[1])
#print(funkySortedList)
def denester(nestedList):
    if isinstance(nestedList, list) is False:
        print("Can't fool me")
        return 0
    unnestedList = []
    for i in range(len(nestedList)):
        if isinstance(nestedList[i], list):
            for j in range(len(nestedList[i])):
                if isinstance(nestedList[i][j], list):
                    for k in range(len(nestedList[i][j])):
                        unnestedList.append(nestedList[i][j][k])
                else:
                    unnestedList.append(nestedList[i][j])
        else:
            unnestedList.append(nestedList[i])
    return unnestedList
funkyList = ["a",[[[[[[[[[["b"]],"c"]]]]]]]],[1,2,3],"d","e",[[True],[False]]]
denestedFunkyList = denester(funkyList)
print(denestedFunkyList)