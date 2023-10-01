# 1) tìm số lớn nhất trong list (list integer). VD: [5, 2, 8, 9] => 9

numbers = [8, 8, 8, 8]

if (len(numbers) == 0):
    print("Khong tim duoc so lon nhat")
else:
    max_number = numbers[0]
    for i in range(1, len(numbers)):
        if (numbers[i] > max_number):
            max_number = numbers[i]

print("So lon nhat la: ", max_number)