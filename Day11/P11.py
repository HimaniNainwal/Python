name = "Himani"
friend  = "Aashita and Nidhi"
anotherFriend = "Sagar"

apple1  = 'Hi i am Himani, "Beautiful and healty as always".'
# Here above i am using single quote so able to use double quotes to highlight in the sentence instead of using \ (Backslash)
apple2 = '''Holaaaaaaa!!!!!!!!!!!!!!!
Guys! How you all doing?
Hope to see u all in high spirit 
and good health.'''
# here in above i am using triple single quotes to write in different lines for a single string apple2 and it won't give any error.
# instead of using single or double quotes which will give me error.

print("Hello"+name)
# print(apple1)
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])
# print(name[6])    # throws an error

print("Let's use a for loop")
for character in apple2:
    print(character)