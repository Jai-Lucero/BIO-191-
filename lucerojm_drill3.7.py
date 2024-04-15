def filled_diamond(side_length):
    for i in range(1, side_length + 1):
        print(" " * (side_length - i) + "*" * (2 * i - 1))
    for i in range(side_length - 1, 0, -1):
        print(" " * (side_length - i) + "*" * (2 * i - 1))

side_length = int(input("Side length: "))
filled_diamond(side_length)