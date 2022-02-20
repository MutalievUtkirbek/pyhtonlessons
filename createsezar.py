maxsus_soz = "ABCDEFGHIJKLMNOPQRTUSTVWXYZ"

sentence  = input("Enter a sentence: ")

sentence = sentence.upper()
arr = []

for x in sentence:
    if x in maxsus_soz:
        arr.append(maxsus_soz.index(x))

print(arr)
    