marks = int(input("enter your marks"))
if marks >= 100  or marks < 0:
    print("invalid marks")
elif( marks >= 90 and marks <= 100):
    print("A grade")
elif marks >= 75 and marks < 90:
    print("B grade")
elif marks >= 40 and marks < 75:
    print("C grade")
else:
    print("FAILL!. Better luck next time")

