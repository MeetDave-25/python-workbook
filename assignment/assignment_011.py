students = [
    [85, 90, 78],
    [45, 67, 39],
    [92, 88, 95],
    [30, 55, 60]
]

#avg
avg = [
    sum(x)/len(x)
    for x in students
]
print(avg)

#extract student who has 80 plus
more_than_80 = [
    x
    for row in students
    for x in row
    if x > 80
]
print(more_than_80)

#falied student who has 40 less
less_than_40 = [
    x
    for row in students
    for x in row
    if x < 40
]
print(less_than_40)

#create new list with plus 5 to all
plus_list= [
    [x+5 for x in row]
    for row in students
]
print(plus_list)


