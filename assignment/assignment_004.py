def register(name, age, *subjects, course="BCA", **details):

    print("Name:", name)
    print("Age:", age)
    print("Course:", course)

    print("Subjects:")
    for subject in subjects:
        print("-", subject)

    print("Additional details:")
    for key, value in details.items():
        print(key, ":", value)


register(
    "Meet",
    20,
    "Python",
    "Machine Learning",
    "DSA",
    course="MCA",
    city="Ahmedabad",
    college="LJCCA"
)
