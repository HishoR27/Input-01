import os

folder_path = r'inputs'
file_extension = '.txt'

files = [file for file in os.listdir(folder_path) if file.endswith(file_extension)]

total_sum = 0

for file_name in files:
    file_path = os.path.join(folder_path, file_name)
    with open(file_path, 'r') as file:
        num_str = file.read()
        numbers = [float(num) for num in num_str.split()]
        total_sum += sum(numbers)

print(total_sum)