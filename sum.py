import os

folder_name = r'input'
file_format = '.txt'

files = [file for file in os.listdir(folder_name) if file.endswith(file_format)]

total_sum = 0

for file_name in files:
    file_name = os.path.join(folder_name, file_name)
    with open(file_name, 'r') as file:
        num_str = file.read()
        numbers = [float(num) for num in num_str.split()]
        total_sum += sum(numbers)

print(total_sum)