X = ('A', 'B', 'C')
Y = ('', 'A', 'B', 'C')

for x in X:
    for y in Y:
        print(int(x =='A' and y == '' or x == 'A' and x == y or x == 'B' and y == '' or x == 'B' and x == y))
