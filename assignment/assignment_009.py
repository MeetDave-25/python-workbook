marks = [45, 78, 92, 33, 67, 88, 29, 95, 56]

#pass or fail check
result = ["PASS" if x > 40 else "FAIL" for x in marks]
print(result)

#add bounce to them below 40 only
bouns = [x+5 if x < 40 else x for x in marks]
print(bouns)

# only marks from 60 to 90
marks_between = [x for x in marks if 60 <= x <= 90]
print(marks_between)

#marks in percentage assume out of 100
per = [x/100*100 for x in marks] 
print(per)

#grade
grade = ["A" if x >= 90 else
         "B" if x >= 80 else
         "C" if x >= 70 else
         "D" if x >= 60 else
         "F"
         for x in marks]
print(grade)
