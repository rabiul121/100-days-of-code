# from turtle import Turtle, Screen
#
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("coral")
# timmy.forward(100)
#
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()


from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Name", ["Robiul", "Emon", "Kamal", "Ressma", "Ruhana", "Emu", "Alifa"])
table.add_column("Age", [25, 15, 35, 33, 11, 17, 4])
table.add_column("Gender", ["Male", "Male", "Male", "Female", "Female", "Male", "Female"])
table.align = "l"

table2 = PrettyTable()
table2.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table2.add_column("Type", ["Electric", "Water", "Fire"])

print(table)
print("\n")
print(table2)
