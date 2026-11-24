Election = int(input("Enter Numbers of votes to check the election result"))
if Election >= 100 or Election < 0:
    print("invalid votes")
elif Election >= 90 and Election <= 100:
    print("candidate A is winner, congratulations!")
else:
    print("candidate B is runner up; Candidate A is winner")