a = [1,2,3,3,6]

def is_increased(a):
    i = 0
    result = True

    while (i < len(a) - 1):
        if (a[i] > a[i+1]):
            result = False
            break
        i += 1
    
    return result

print(is_increased(a))
