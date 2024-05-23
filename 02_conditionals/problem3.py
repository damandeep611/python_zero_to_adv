score = int(input("Enter your Marks to get Grade: "))

if score >= 101:
    print("abe jyada chana na ban sahi marks enter kar")
    exit()

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "Boombbaaya"

print("Grade: ", grade)