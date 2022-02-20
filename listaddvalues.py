# Insert adds values to the specified position in the list.
#  names = ["John", "Bob", "Marry", "Jane"]
# print(names)
# names.insert(1, "Jack")
# print(names)

# Append  adds a new element to the end of the list
# names = ["John", "Bob", "Marry", "Jane"]
# print(names)

# names.append("Jack")
# print(names)


#nested list
names = ["John", "Bob", "Marry", "Jane"]
print(names)
# names.extend(["Jack", "Jill"])
# print(names)
names.append(["Jack", "Jill"])
for name in names:
    print(name)