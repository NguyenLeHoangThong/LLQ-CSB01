# 4) tìm số lớn thứ nhì trong list (list integer). VD: [5, 2, 8, 9] => 8 

numbers = [9 ,234, 123, 12]

# TH1: i > max_1
# TH2: i <= max_1 and i > max_2

max_1 = ""
max_2 = ""

if (len(numbers) == 0):
    print("Khong co so lon thu nhi")
elif (len(numbers) == 1):
    print("So lon thu nhi: ", numbers[0])
else:
    if (numbers[0] > numbers[1]):
        max_1 = numbers[0]
        max_2 = numbers[1]
    else:
        max_1 = numbers[1]
        max_2 = numbers[0]

    for i in range(2, len(numbers)):
        if (numbers[i] > max_1):
            max_2 = max_1
            max_1 = numbers[i]
        elif (numbers[i] <= max_1 and numbers[i] > max_2):
            max_2 = numbers[i]

print(max_2)

