from email import message


birthyear  = input("Enter your birthyear: ")

txt = "My name is John, and I was born in {1}, and I am {0} years old"
print(txt.format(2020-int(birthyear), birthyear))