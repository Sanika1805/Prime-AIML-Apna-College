info=[
    ("sanika","maths"),
    ("sanika","cpp"),
    ("kd","science"),
    ("divya","japanese"),
    ("vishu","python"),
    ("shruti","java"),
    ("pratik","python")
]


# for tup in info:
    # print(tup)
    # print(tup[0]) #name
    # print(tup[1]) #course

# #for unique courses:
unique_courses= set()
for tup in info:
    unique_courses.add(tup[1]) #courses

print(unique_courses)


# #list of students enrolled in python
# for name,course in info:
#     if (course == "python"):
#         print(name)

#create dictionary (student, set of courses)
# dict ={}
# for name,course in info:
#     if (dict.get(name)==None): #if name not present in dict then .get value gives none 
#         dict.update({name:set()})
#         dict[name].add(course)
#     else:
#         dict[name].add(course)
# print(dict)