#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
with open("./Input/Letters/starting_letter.txt") as letter_format:
    letter_content = letter_format.read()
#Replace the [name] placeholder with the actual name.
with open("./Input/Names/invited_names.txt") as name:
    names = name.readlines()
    for name in names:
        stripped_name = name.strip()
        with open(f"./Output/ReadyToSend/letter_{stripped_name}.txt", "w") as letter_file:
            letter_file.write(letter_content.replace("[name]", stripped_name))
