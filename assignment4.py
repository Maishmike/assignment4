# Grading system
maths = 80
physics = 60
geo = 65
chem = 75

total = maths + physics + geo + chem
average = total / 4

if average > 100 or average < 0 or maths > 100 or maths < 0 or physics > 100 or physics < 0 or geo > 100 or geo < 0 or chem > 100 or chem < 0 :
    print(" Unrecognized marks / average")
else:
    if average > 70:
        print("A")
    elif average > 50:
        print("B")
    elif average > 30:
        print("C")
    else:
        print("D")