heights = input("enter the height separated by Commas : ")
height_new = heights.split(",")
count = 0
for height in height_new:
    count += 1
print(count)
for i in range(count):
    height_new[i] = int(height_new[i])
print(height_new)
total = 0
for person in height_new:
    total += person
print("Sum of heights is : ", total)
avg = round(total/count)
print("Average of heights is : ", avg)

