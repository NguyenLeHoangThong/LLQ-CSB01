# 2) Tạo 1 dict kết hợp từ 2 list, ví dụ:
# list key = ["name", "age", "avg"]
# list value = ["Thong", 10, 9.5]

# dict ket_qua mong muốn = {
#     name: "Thong",
#     age: 10,
#     avg: 9.5
# }

key = ["name", "age", "avg"]
value = ["Thong", 10, 9.5]

def create_dictionary_by_2_list(key, value):
    if (len(key) != len(value)):
        return False
    result = {}
    i = 0
    while (i < len(key)):
        result[key[i]] = value[i]
        i += 1
    return result

print(create_dictionary_by_2_list(key, value))