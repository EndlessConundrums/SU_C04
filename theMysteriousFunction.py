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
    caeser = "nopqrstuvwxyzabcdefghijklm"
    text = list(plaintext)
    print(text)
    for i in range(len(text)):
        print("Moved on to next letter")
        for j in range(len(alphabet)):
            if alphabet[j] == text[i]:
                text[i] = caeser[j]
                print("Modified letter")
                break
    return text
sample = "hello world"
sample = encryptor(sample)
print(sample)
sample = encryptor(sample)
print(sample)