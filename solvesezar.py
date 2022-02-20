maxsus_soz = "ABCDEFGHIJKLMNOPQRTUSTVWXYZ"

numbers = [12, 4, 13, 8, 13, 6, 8, 20, 12, 8, 12, 19, 18, 10, 8, 17, 1, 4, 10]

result = ''

for x in numbers:
    result+=str(maxsus_soz[x])

print(result)
