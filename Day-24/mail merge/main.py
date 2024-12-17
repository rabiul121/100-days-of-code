with open("template_letter.txt") as template:
    template_content = template.read()

with open("names.txt") as name_files:
    names = name_files.readlines()
    for name in names:
        stripped_name = name.strip()
        with open(f"letter_{stripped_name}.txt", "w") as letter_files:
            letter_files.write(template_content.replace("[name]", stripped_name))
