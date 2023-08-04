def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You didn't provide valid input."

    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"Result: {formatted_f_name} {formatted_l_name}"


print(format_name(f_name=input("Enter First Name: "), l_name=input("Enter Last Name: ")))
