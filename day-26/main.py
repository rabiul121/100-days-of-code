student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}
# Looping through dictionary
# for student, score in student_dict.items():
#     print(score)


import pandas

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)
# loop through rows of a dataframe
for index, row in student_data_frame.iterrows():
    print(row.score)
