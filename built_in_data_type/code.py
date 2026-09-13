'''
    Given with a list of tuples with info(name,subject)

    list all unique courses
    list student enrolled in English
    create dictionary (student, set of courses)
'''

info = [
    ("Alice", "Math"),
    ("Bob", "Science"),
    ("Alice", "Science"),
    ("Charlie", "Math"),
    ("Bob", "Math"),
    ("Alice", "English"),
    ("Charlie", "English"),
]

courses_set = set()
student = []
std_courses = {}
for name,courses in info:
    # courses_set.add(tup[1])
    courses_set.add(courses)

    if courses == 'English':
        student.append(name)

    if std_courses.get(name):
        std_courses[name].add(courses)
    else:
        std_courses[name] = set()
        std_courses[name].add(courses)


print(courses_set)
print(student)
print(std_courses)
# print(bool(None))