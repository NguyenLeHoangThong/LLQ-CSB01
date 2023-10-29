students = [
    {
        "name": "Thong",
        "class": "10A5",
        "avg": 9
    },
    {
        "name": "Van",
        "class": "10A6",
        "avg": 8
    },
    {
        "name": "Tran",
        "class": "10A6",
        "avg": 9.5
    }
]

def calculate_avg_of_students(students):
    i = 0
    tong = 0
    while (i < len(students)):
        tong += students[i]["avg"]
        i += 1
    diem_trung_binh = tong / len(students)
    return diem_trung_binh


print(calculate_avg_of_students(students))