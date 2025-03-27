schoolClassList = {"Time for Change":["Mr. Henry", "B"], "Myth and Meaning":["Mr. Bollag-Miller", "C"], "Algebra":["Ms. Williams", "A"], "Bio Foundations":["Ms. Wildes", "A"]}
whichClass = input("Which class do you want to modify? :")
newGrade = input("Now put in the new grade: ")
schoolClassList[whichClass][1] = newGrade
print(schoolClassList)