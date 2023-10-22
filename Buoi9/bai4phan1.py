s = "asdfm,asndf"

def is_palindrome(s):
    i1 = 0 # trái
    i2 = len(s) - 1 # phải
    middle = len(s) // 2
    result = True

    while (i1 < middle) and (i2 > middle):
        if (s[i1] != s[i2]):
            result = False
            break
        i1 += 1
        i2 -= 1

    return result


print(is_palindrome(s))
