score = input("请输入成绩:")
grade = int(score)

if grade<=100 and grade>90:
    print("A")

if grade<=90 and grade>80:
    print("B")

if grade<=80 and grade>=60:
    print("C")

if grade<60 and grade>=0:
    print("D")

if grade>100 or grade<0:
    print("输入有误")
