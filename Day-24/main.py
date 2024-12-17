# with open('my_file.txt') as file:
#     content = file.read()
#     print(content)
#

with open('my_file.txt', "w") as file:
    content = file.write("This is to test file writing")
    print(content)
