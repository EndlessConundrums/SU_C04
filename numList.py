username = "Randall"
password = "correcthorsebatterystaple" #if you know, you are an awesome person
inUsername = input("Type username: ")
inPassword = input("Type password: ")
while ((inUsername == username) and (inPassword == password)) is False:
    print("You were incorrect.")
    inUsername = input("Type username: ")
    inPassword = input("Type password: ")
print("You (finally) got them correct! Commencing username + password scrambling...")