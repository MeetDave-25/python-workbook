numbers = [12, 5, 8, 21, 30, 7, 16, 9]

#square of numbers in list 
square = [x*x for x in numbers]
print(square)

#even numbers
#even_number = [x for x in numbers if x % 2 == 0]
#print(even_number)
number = ["even" if x % 2 == 0 else "odd" for x in numbers]
print(number)


#greater than 10
number_greater_than_10 = [x for x in numbers if x > 10]
print(number_greater_than_10)

#list each element multiple by 3
multiply_list = [x * 3 for x in numbers]
print(multiply_list)
