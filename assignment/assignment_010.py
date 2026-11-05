matrix = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

#extract all number
result = [num for row in matrix for num in row]
print(result)

#extrct only even number
even_number = [num for row in matrix for num in row if num%2==0 ]
print(even_number)

#square of list and create new list
square = [num*num for row in matrix for num in row]
print(square)
