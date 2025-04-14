#sillyList = [5,4,6,201,8]
#def numberModifier(inputNum):
    #return inputNum * 5

#def listContraption(inputList,inputFunc):
    #for i in range(len(inputList)):
        #inputList[i] = inputFunc(inputList[i])
    #return inputList

#print(listContraption(sillyList, numberModifier))
wordList = "HERE AT BVR HAX WE WANT THE MOST WORKING AND THE LEAST STANDING POSSIBLE"
#This sentence from the latest BVR HAX 
def listCombobulator(spacer):
    def wordCombobulator(string):
        string = string.split(" ")
        for i in range(len(string)):
            string[i] = spacer[i%len(spacer)](string[i])
        return string
    return wordCombobulator
exclaim = lambda word: "!" + word + "!"
descend = lambda word: word.lower()
pound = lambda word: "#" + word + "#"

print(listCombobulator([exclaim,descend,pound])(wordList))