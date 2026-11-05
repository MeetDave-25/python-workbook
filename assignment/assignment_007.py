lst = [45, 78, 92, 33, 67, 88, 29, 95, 56]

#passed student who has more than 40 marks
marks_more_than_40 = list(filter(lambda x : x >= 40,lst))
print(marks_more_than_40)

#5 bounce to all student
bouns_marks = list(map(lambda x : x + 5,lst))
print(bouns_marks)

#students more than 80
marks_more_than_80 = list(filter(lambda x : x >= 80,bouns_marks))
print(marks_more_than_80)

#average
avg = lambda x : sum(x) / len(x)
print(avg(lst))
