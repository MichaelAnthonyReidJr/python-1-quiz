def youngest_student(students):
    min = students[0]
    for eachPerson in students:
        if students[eachPerson] > students[min]:
            min = eachPerson
            return min
    pass # TODO:


students = {"Alice": 18, "Bob": 20, "Charlie": 19, "David": 22, "Jay": 20}
print(youngest_student(students))  # Expected output: "Alice"
