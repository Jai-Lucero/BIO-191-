age = int(input("What is your age? "))
own_license = input("Do you have a fishing license in MN (yes/no)? ").lower() == "yes"
parent_license = input("Does your parent have a fishing license (yes/no)? ").lower() == "yes"

legal = (age <= 15 and parent_license) or (age >=16 and own_license)

if legal:
    print("You are legal to fish in MN.") 
else:
    print("You are not legal to fish in MN.")