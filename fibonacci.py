def fibonacciLoop(length):
    lengtint = int(length)
    numOne = 1
    numTwo = 1
    print(str(numOne) + ", " + str(numTwo))
    for i in range(lengtint):
        if i % 2 == 0:
            numOne = numTwo + numOne
            print(str(numOne) + ", " + str(numTwo))
        elif i % 2 == 1:
            numTwo = numTwo + numOne
            print(str(numTwo) + ", " + str(numOne))
def fibonacciRecursive(length, numOne, numTwo):
    if length == 0:
        print(str(numOne) + ", " + str(numTwo))
        return "done"
    else:
        length -= 1
        print(str(numOne) + ", " + str(numTwo))
        temp = numOne
        numOne += numTwo
        numTwo = temp
        fibonacciRecursive(length, numOne, numTwo)
fibonacciLoop(10)
print("--------------------------------")
fibonacciRecursive(10,1,1)