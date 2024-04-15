age = int(input("Please enter your age "))
natural_born = input("Are you a natural born citizen of the U.S. (yes/no)? ") == "yes"
residency = int(input("How many years have you resided in the U.S.? "))

eligible = (natural_born and age >=35 and residency >= 14)

if age <35:
    eligible = False
if natural_born == "no":
    eligible = False
if residency <14:
    eligible = False

if eligible:
    print("You can run for president of USA")
else:
    print("You cannot run for president of USA")