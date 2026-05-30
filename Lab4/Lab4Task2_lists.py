maxRows = 5
table = maxRows*[0]
rowNumber = 0

while rowNumber < maxRows:
    temp = input("enter some numbers:").split()
    table[rowNumber] = len(temp) * [0]
    for colNumber in range(len(temp)):
        table[rowNumber][colNumber] = float(temp[colNumber])
    rowNumber = rowNumber + 1
print(table)