# Student Marks Analyser
# Reads marks of students from a csv file and gives a small report.
# Subjects in my file are Maths, Physics and English.

import csv

FILE_NAME = "marks.csv"


def get_grade(average):
    if average >= 90:
        return "A"
    elif average >= 75:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 40:
        return "D"
    else:
        return "F"


def analyse_marks():
    students = []

    with open(FILE_NAME, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            maths = int(row["Maths"])
            physics = int(row["Physics"])
            english = int(row["English"])
            total = maths + physics + english
            average = total / 3
            students.append({
                "name": row["Name"],
                "total": total,
                "average": average,
                "grade": get_grade(average)
            })

    if len(students) == 0:
        print("No data in file.")
        return

    print("\nName          Total   Average   Grade")
    print("-" * 42)
    for s in students:
        print(f"{s['name']:13} {s['total']:5}   {s['average']:7.2f}   {s['grade']}")

    # class topper
    topper = students[0]
    for s in students:
        if s["total"] > topper["total"]:
            topper = s
    print(f"\nClass topper: {topper['name']} with {topper['total']} marks")

    # class average
    class_avg = sum(s["average"] for s in students) / len(students)
    print(f"Class average: {class_avg:.2f}")

    # save same report in a text file also
    with open("report.txt", "w") as out:
        out.write("Student Marks Report\n")
        for s in students:
            out.write(f"{s['name']} - Total: {s['total']}, Average: {s['average']:.2f}, Grade: {s['grade']}\n")
        out.write(f"\nTopper: {topper['name']}\n")
        out.write(f"Class average: {class_avg:.2f}\n")
    print("Report saved in report.txt")


if __name__ == "__main__":
    analyse_marks()
