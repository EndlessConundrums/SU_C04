#password inputter time
endSession = False
username = input("Please input your username: ")
password = input("Now please enter your password: ")
while endSession is False:
    action = input("What would you like to do? : ")
    if action == "REVIEWPASS":
        testPass = input("Okay! Input your password: ")
        if testPass == password:
            print("Review successful!")
        else:
            print("That was incorrect. Did you write your password down somewhere?")
    elif action == "NEWPASS":
        testPass = input("Input your current password first: ")
        if testPass == "whte_rbt":
            print("Hello, Dennis. Your account is unfortunately not present. We THINK you forgot to say the magic word.")
        elif testPass == password:
            newPass = input("Please enter your new password here: ")
            password = newPass
        else:
            print("That was incorrect. Did you write your password down somewhere?")
    elif action == "NEWUSER":
        testPass = input("Input your current password first: ")
        if testPass == "whte_rbt":
            print("Hello, Dennis. Your account is unfortunately not present. We THINK you forgot to say the magic word.")
        elif testPass == password:
            newPass = input("Please enter your new username here: ")
            username = newPass
        else:
            print("That was incorrect. Did you write your password down somewhere?")
    elif action == "QUIT":
        print("Okay. Program quitting.")
        break
    else:
        print("Error: " + action + " was not recognized. Please try again.")