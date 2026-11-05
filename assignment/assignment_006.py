lst =  [12, 5, 8, 21, 30, 7, 16, 9]

#square
square = list(map(lambda x :x * x,lst))
print(square)

#check odd and even
check_number = list(filter(lambda x : x %2==0,lst))
print(check_number)

#check greater than 10
check_greater = list(filter(lambda x : x>10,lst))
print(check_greater)
