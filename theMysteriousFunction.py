#def calculateArea(whichShape, width, height):
    #if whichShape == "rectangle":
        #return width * height
    #elif whichShape == "square":
        #return width ** 2
    #elif whichShape == "circle":
        #return 3.1415 * (width ** 2)
    #elif whichShape == "triangle":
        #return (width * height) / 2
#rectArea = calculateArea("rectangle", 5, 4)
#triArea = calculateArea("triangle", 6, 3)
#print(rectArea)
#print(triArea)
def encryptor(plaintext):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    caeser = "fghijklmnopqrstuvwxyzabcde"
    text = list(plaintext)
    print(text)
    for i in range(len(text)):
        for j in range(len(alphabet)):
            if alphabet[j] == text[i]:
                text[i] = caeser[j]
    return text
sample = "hello world"
print(encryptor(sample))

