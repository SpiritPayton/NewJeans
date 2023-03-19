"""Sorting a multi-dimensional list
"""
names_list = [
    ["Jo Onda serim", 209, "Otautahi"],
    ["Stu ros spirit", 234234, "aucky"],
    ["tsuki nadine dream payton", 454, "billie ring x ring"],
    ["chou tzuyu", 66, "tsuki"]
]

# sorting by city/town
names_list = sorted(names_list, key=lambda x: x[2])

for person in names_list:
    # prints the index number (+1) followed by each element
    print(f"{names_list.index(person)+1}")
