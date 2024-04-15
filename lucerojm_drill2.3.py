x = int(input("Please enter an integer: "))
y = int(input("Please enter another integer: "))
z = int(input("Please enter a third integer: "))

maxNum = x

if y > maxNum and y % 2 != 0: 
    maxNum = y
if z > maxNum and z % 2 != 0: 
    maxNum = z

if maxNum % 2 != 0:
    print(maxNum,"is the greatest.")
else:
    print("There are no odd integers.")

x = int(input("Please enter an integer: "))
y = int(input("Please enter another integer: "))
z = int(input("Please enter a third integer: "))

maxNum = None

if x % 2 != 0:
    maxNum = x
if y % 2 != 0 and (maxNum is None or y > maxNum):
    maxNum = y
if z % 2 != 0 and (maxNum is None or z > maxNum):
    maxNum = z

if maxNum is not None:
    print(maxNum, "is the greatest odd integer.")
else:
    print("There are no odd integers.")
