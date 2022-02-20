word = input("Enter a word: ")
direction=input('Enter a direction: ')
alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = input("Enter a key")
encrypted_word=''
if direction.upper() == 'RIGHT':
    key = int(key)
else:
    key = -int(key)

for i in word:
    position = alphabet.find(i)
    new_position=(position+key)%len(alphabet)
    print(new_position)
    if new_position < 0:
        new_position = len(alphabet)+new_position
    encrypted_word+=alphabet[new_position]

print(encrypted_word)