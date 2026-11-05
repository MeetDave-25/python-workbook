lst = [1,2,3,4,5,6]
sq = list(map(lambda x : x * x,lst))
print(sq)

num = lambda x : "even" if (x % 2 == 0) else "odd"
print(num(int(input("enter number to enter :- "))))
