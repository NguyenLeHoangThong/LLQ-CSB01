def print_fibonaci(n):
    s1 = 1
    s2 = 1
    print(s1)
    print(s2)
    i = 0
    while (i < n-2):
        s3 = s1 + s2
        print(s3)
        s1 = s2
        s2 = s3
        i += 1

print_fibonaci(1000)