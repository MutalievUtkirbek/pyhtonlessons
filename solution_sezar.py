word = input("Enter a word: ")
direction=input('Enter a direction: ')
alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = input("Enter a key")
dencrypted_word=''
if direction.upper() == 'RIGHT':
    key = int(key)
else:
    key = -int(key)

for i in word:
    position = alphabet.find(i)
    new_position=(position-key)%len(alphabet)
    dencrypted_word+=alphabet[new_position]

print(dencrypted_word)