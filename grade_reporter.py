# Grade Reporter

grades = [85, 72, 64, 48, 35, 90, 56]

total = 0
passed = 0
failed = 0

for grade in grades:
    total = total + grade

    if grade >= 80:
        print(f"{grade}: A")
    elif grade >= 70:
        print(f"{grade}: B")
    elif grade >= 60:
        print(f"{grade}: C")
    elif grade >= 50:
        print(f"{grade}: D")
    else:
        print(f"{grade}: F")

    if grade >= 50:
        passed = passed + 1
    else:
        failed = failed + 1

average = total / len(grades)

print("\n--- Grade Report ---")
print(f"Total marks: {total}")
print(f"Average: {average:.2f}")
print(f"Passed: {passed}")
print(f"Failed: {failed}")