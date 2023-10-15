def so_lan_xuat_hien(s1, s2):
    i = 0
    count = 0
    while (i < len(s1)):
        if (s1[i] == s2):
            count += 1
        i += 1
    
    return count