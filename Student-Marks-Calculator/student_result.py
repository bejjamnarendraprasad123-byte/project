Name = input("Enter student name : ")
n = int(input("Enter number of subjects : "))

Total = 0
sub = []
marks = []
status = "Pass"

for i in range(n):
    sub.append(input("Enter subject : "))
    marks.append(int(input("Enter marks : ")))

print("\n------Student Report------")
print("Student Name :", Name)

for i in range(n):
    print(sub[i], ":", marks[i])
    Total = Total + marks[i]

    if marks[i] < 35:
        status = "Fail"

print("Total Marks :", Total)

percent = Total / n
print("Percentage :", percent)

print("Status :", status)

if percent >= 90:
    print("Grade : O")
elif percent >= 80:
    print("Grade : A")
elif percent >= 70:
    print("Grade : B")
elif percent >= 60:
    print("Grade : C")
elif percent >= 50:
    print("Grade : D")
else:
    print("Grade : F")