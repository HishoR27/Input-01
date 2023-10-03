file = open("D:\GOWREESAN\study\python\sum\Input-01\sum.txt", "r")

numbers_str = file.read()
numbers = [
            int(num) 
            for num in numbers_str.split()
       ]

print(sum(numbers))
