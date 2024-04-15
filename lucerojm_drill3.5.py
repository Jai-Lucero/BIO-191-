def multiplication_table():
    table = [[str(i * j) for j in range(1, 11)] for i in range(1, 11)]
    for row in table:
        print(' '.join(row))

multiplication_table()



for i in range (1, 10):
    print(i, end="\t")
print ()

for j in range (1, 10):
    for k in range(1,10):
        print(j * k, end = "\t")
    print("\n")