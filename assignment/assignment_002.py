def calc_avg(marks):
    total = sum(marks)
    avg = total / len(marks)
    return avg
    
def assign_grade(avg):
    if(avg >= 90):
        return "A+"
    elif (avg>= 80):
        return "A"
    elif (avg>= 70):
        return "B"
    elif (avg>= 60):
        return "C"
    else:
        return "F"
student = {
    "Meet" : [70,80,90],
    "Shyam" : [50,60,70],
    "Kinjal" : [50,30,70]
}

print("\n student Result :- ")
print("===========================")

for name,marks in student.items():

    avg = calc_avg(marks)
    grade = assign_grade(avg)

    print("\n Student :- ",name)
    print("marks :- ",marks)
    print("Average :- ",avg)
    print("Grade :- ",grade)

#find topper

topper = ""
highest_average = -1

for name,marks in student.items():
    avg = calc_avg(marks)

    if avg > highest_average:
        highest_average = avg
        topper = name

print("\n==============================")
print("Class topper")
print("================================")

print("Class topper :- ",topper)
print("Highest average :- ",highest_average)

print("================================")

