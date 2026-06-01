def min_temperature(table):
    min_temp = table [0][2]
    for row in range(1,len(table)):
        if table[row][2] < min_temp:
            min_temp = table[row][2]
    return min_temp

def max_temperature(table):
    max_temp = table [0][2]
    for row in range(1,len(table)):
        if table[row][2] > max_temp:
            max_temp = table[row][2]
    return max_temp

infile = open("temperature.txt")
table = []
sum_temperature = 0 
for line in infile:
    line = line.split(",")
    line[2] = int(line[2])
    table.append(line)
print("minimum temperature:", min_temperature(table), "maximum temperature:", max_temperature(table))