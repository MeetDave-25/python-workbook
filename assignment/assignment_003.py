#default argument example
def default(name="meet"):
    print("name :- ",name)
default()

print("\n")
#postional argument example
def pos(name,age,marks):
    print("name :- ",name)
    print("age :- ",age)
    print("marks :- ",marks)

pos("meet",20,100)


print("\n")
#keyword argument example
def keyword(name,age,marks):
    print("name :- ",name)
    print("age :- ",age)
    print("marks :- ",marks)

keyword(age=20,name="meet",marks=100)

print("\n")
#variable-length argument
def pokey(*arg):
    total = sum(arg)
    print("total of numbers :- ",total)

pokey(10,20,40,30,50)

print("\n")
def var(**karg):
    print(karg)
var(name="meet",age=20,marks=100)
