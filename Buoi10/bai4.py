a = [9,9,9,9,3]

i = 2
if (a[1] > a[0]):
    max_number = a[1]
    second_max_number = a[0]
else:
    max_number = a[0]
    second_max_number = a[1]

# ban dau: max_number = 123, second_max_number = 93

# TH1: neu nhu chay toi so nao do ma nho hon ca 1st 2nd hien tai => bo qua
# TH2: neu nhu chay toi so nao do ma > max_number => max_number = so do, va second_max_number = max_number cu~
# TH3: neu nhu chay toi so nao do ma > second_max_number va < max_number => gan cho so do thanh second_max_number
# TH4: neu nhu second_max_number = max_number ma gap so nao do nho hon ca 2 => gan cho second_max_number thanh so do
