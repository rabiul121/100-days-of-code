# Python scope
enimies = 1


def increase_enimies():
    enimies = 2
    print(f"Enimies inside function: {enimies}")


increase_enimies()
print(f"Enimies outside function: {enimies}")

