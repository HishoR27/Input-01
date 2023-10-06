file = open("sum.txt", "r")

num_str = file.read()

number = [float(num) for num in num_str.split()]

print(sum(number))

#  12 45 8 24 57 10 44 11 79 51 
