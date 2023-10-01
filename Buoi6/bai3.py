# 3) tìm phần tử đầu tiên của list có chuỗi bắt đầu là "abc" (list string). VD ["a", "abcdef", "agtfs"] => "abcdef"

strings = ["a", "abcdef", "agtfs"]

for i in strings:
    if (len(i) < 3):
        continue
    if (i[0:3] == "abc"):
        print(i)
        break



