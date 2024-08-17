# to find the maximum number in a list created by user without len and max function
num = input("Enter the numbers( separated by comma's): ")
num_list = num.split(",")
print(num_list)

count = 0

for nums in num_list:
    count += 1
print(count)

for i in range(count):
    num_list[i] = int(num_list[i])
print(num_list)

max_num = num_list[0]
for number in num_list:
    if number > max_num:
        max_num = number
print(f'The maximum number is {max_num}')
