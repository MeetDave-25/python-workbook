print("==========================")
print(" MATHS PRACTICE TRACKER ")
print("==========================")

name = input("student name :- ")
topic = input("Entre Topic :- ")
que = int(input("question attemped :- "))
ans = int(input("Correct answer :- "))

if (que > 0):
    per = (ans/que)*100
else:
     print("Questions must be greater than zero")

if ans > que:
    print("Correct answers cannot exceed attempted questions")

print("\n")

print("==========================")
print(" PRACTICE MODULE ANS ")
print("==========================")
print("Student :- ",name)
print("topic :- ",topic)
print("attemped :- ",que)
print("correct :- ",ans)
print("wrong ans :- ",que - ans)
print(f"Accuracy: {per:.2f}%"))
print("==========================")

if(per < 70):
    print("perfomance :- keep practicing...!!!")
else:
    print("keep going good one next topics")
