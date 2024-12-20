import pandas as pd
from pandas.core.interchange.dataframe_protocol import DataFrame

# data = pandas.read_csv("weather_data.csv")
#
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data['temp'].to_list()
# print(temp_list)
#
# average_temp = data['temp'].mean()
# print(average_temp)
# max_temp = max(data['temp'])
# print(max_temp)
# # Get data in columns
# print(data["condition"])
# print(data.condition)

# Get data in rows
# print(data[data.day == "Monday"])
# print(data[data.temp == max(data.temp)])

# monday = data[data.day == "Monday"]
# monday_temp_Celsius = monday.temp[0]
# monday_temp_fahrenheit = (monday_temp_Celsius * 9 / 5) + 32
# # print(monday)
# print(monday_temp_fahrenheit)

# Create dataframe from scratch
# data_dict = {
#     "student": ["Rakib", "Robi", "Shakib", "Moue", "Jahid"],
#     "scores": [58, 50, 77, 65, 33]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("scores.csv")
# print(data)

# data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20241219.csv")
# fur_color_counts = data["Primary Fur Color"].value_counts()
# fur_color_counts_df = pd.DataFrame({
#     "Fur Color": fur_color_counts.index,
#     "Count": fur_color_counts.values
# })
#
# fur_color_counts_df.to_csv("fur_color_counts.csv", index=False)
# print(fur_color_counts_df)


# v2
data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20241219.csv")
gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
}
data_df = pd.DataFrame(data_dict)
data_df.to_csv("squirrel_color_counts.csv")
