print("==========================")
print(" MATHS PRACTICE TRACKER ")
print("==========================")

name = input("student name :- ")
topic = input("Entre Topic :- ")
que = int(input("question attemped :- "))
ans = int(input("Correct answer :- "))

per = (ans/que)*100

print("\n")

print("==========================")
print(" PRACTICE MODULE ANS ")
print("==========================")
print("Student :- ",name)
print("topic :- ",topic)
print("attemped :- ",que)
print("correct :- ",ans)
print("wrong ans :- ",que - ans)
print("Accuracy :- ",per)
print("==========================")

if(per < 70):
    print("perfomance :- keep practicing...!!!")
else:
    print("keep going good one next topicS")
