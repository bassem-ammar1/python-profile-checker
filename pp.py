name = input("name: ")
age = int(input("age: "))
input("fields of interests: ")
GPA = float(input("GPA: "))
graduated = input("graduated: ")

if age < 25:
    if GPA >= 3.5 and graduated == "yes":
        print("you are eligible for a scholarship")
elif age < 30:
    if GPA >= 2.5:
       print("you are eligible for an internship")
else:
    print("try to apply later")