def print_squares(side_length):
 
  for i in range(side_length):
    for j in range(side_length):
      print("*", end="")
    print()  

  print(" ") 

  for i in range(side_length):
    print("*", end="")
    for j in range(1, side_length - 1):
      print(" " if i != 0 and i != side_length - 1 else "*", end="")
    print("*") 

side_length = int(input("Side length: "))

print_squares(side_length)