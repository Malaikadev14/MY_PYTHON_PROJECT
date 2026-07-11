subjects=["English","Maths","Computer","Science","G.K"]
marks=[]
print("===STUDENT RESULT SYSTEM===")
for subject in subjects:
    while True:
        try:
            mark=int(input(f"{subject} Enter marks:"))
            if 0<=mark<=100:
                marks.append(mark)
                break
            else:
               print("Write between 0 to 100")
        except ValueError:
            print("Only write numbers. Not alpha bets!")
total=sum(marks)
percentage=(total/500)*100
print("===STUDENT RESULT CARD===")
print(f"Total marks:{total}/500")
print(f"Percentage:{percentage:.2f}%")
if percentage >= 90:
        grade="A+"
elif percentage >= 80:
        grade="A"
elif percentage >= 70:
        grade="B"
elif percentage >= 60:
        grade="C"
else:
        grade="Fail"
print(f"Grade:{grade}")
if percentage >= 60:
        print("Status: PASS✔️")
else:
        print("Status: FAIL❌")
        