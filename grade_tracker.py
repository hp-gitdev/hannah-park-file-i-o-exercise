import csv

def load_students(filepath):
    """Reads the CSV and returns a list of dictionaries."""
    students = []

    try:
        with open(filepath, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                students.append(row)
    
    except FileNotFoundError:
        print("Error: File Not Found.")
        return []
    return students

def get_valid_grade(subject_name):
    """Prompt the user for a single grade, validating it's a number between 0 and 100."""
    while True:
        raw = input(f"Enter {subject_name} grade (or press Enter for missing): ").strip()

        if raw == "":
            return ""
        
        try:
            number = float(raw)
        
        except ValueError:
            print(f"'{raw}' is not a valid number. Try again.")
            continue

        if 0 <= number <= 100:
            return str(int(number))
        
        else:
            print(f"Grade must be between 0 and 100. Try again.")


def add_student(students):
    """Prompt for a new student's info and add them to the student list."""
    while True:
        name = input("Enter student's name: ").strip()
        if name:
            break
        print("Name cannot be empty.")

    math = get_valid_grade("math")
    science = get_valid_grade("science")
    english = get_valid_grade("english")
    history = get_valid_grade("history")

    new_student = {
        "student_name": name,
        "math": math,
        "science": science,
        "english": english,
        "history": history,
    }

    students.append(new_student)
    print(f"{name} added to the class.")


def calculate_average(grades):
    """Calculate the average of a list of grades, skipping empty values."""
    valid = []

    for value in grades:        #skip empty strings and convert valid grades to integers
        if value:
            valid.append(int(value))

    if not valid:           #No valid grades means we can't compute an average
        return None
    
    return round(sum(valid)/len(valid), 1)



def get_letter_grade(average):
    """Convert a numeric average to a letter grade or N/A if average is None."""
    if average is None:
        return "N/A"
    
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    
    else:
        return "F"


def generate_report(students):
    """Build a summary dict with class stats and individual student results."""
    result = []

    for student in students:
        grades = [student["math"], student["science"], student["english"], student["history"]]
        average = calculate_average(grades)
        letter = get_letter_grade(average)

        result.append({
            "name": student["student_name"],
            "average" : average,
            "letter": letter

        })

    #filter out students with no valid grades before computing class stats
    averages = [r["average"] for r in result if r["average"] is not None]
  
    total_students = len(students)

    if averages: 
        class_avg = round(sum(averages)/len(averages), 1)
        highest_avg = max(averages)
        lowest_avg = min(averages)
    
    else:       #no students had any valid grades, so class are undefined
        class_avg = highest_avg = lowest_avg = None
    


    grade_distribution = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0, "N/A": 0}

    for r in result:
        grade_distribution[r["letter"]] += 1

    return {
        "total_students": total_students,
        "class_average": class_avg,
        "highest_average": highest_avg,
        "lowest_average": lowest_avg,
        "grade_distribution": grade_distribution,
        "individual_student_result": result
    }


def write_report(report, filepath):
    """Write a formatted class report to a text file."""
    with open(filepath, "w") as file:
        file.write("Class Report\n")
        file.write("="*40 + "\n\n")

        file.write(f"Total Students: {report['total_students']}\n")
        file.write(f"Class average: {report['class_average']}\n")
        file.write(f"Highest average: {report['highest_average']}\n")
        file.write(f"Lowest average: {report['lowest_average']}\n\n")
        
        file.write("Grade Distribution:\n")
        for letter, count in report["grade_distribution"].items():
            file.write(f"   {letter}: {count}\n")
        file.write("\n")

        file.write("Individual Results:\n")
        for entry in report["individual_student_result"]: 
            file.write(f"  {entry['name']}: {entry['average']} ({entry['letter']})\n")
    


def main():
    students = load_students("data/students.csv")
    print(f"Loaded {len(students)} students.")
    
    add_student(students)       
    print(f"Now have {len(students)} students.")   
    
    report = generate_report(students)
    print_summary(report)
    write_report(report, "grade_report.txt")
    print("Report written to grade_report.txt")

def print_summary(report):
    """Print a class summary including the top 5 students to the terminal."""
    print("Class Summary")
    print("="*40)
    print(f"Total students: {report['total_students']}")
    print(f"Class average: {report['class_average']}")
    print(f"Highest average: {report['highest_average']}")
    print(f"Lowest average: {report['lowest_average']}")
    print("\nGrade Distribution:")
    for letter, count in report["grade_distribution"].items():
        print(f"    {letter}: {count}")

    remaining = [r for r in report["individual_student_result"] if r["average"] is not None]

    top_5 = []
   
   #find the top 5 by repeatedly picking the highest remainig average
    for i in range(5):  
        if not remaining:
            break

        best = remaining[0]
    
        for student in remaining:
            if student["average"] > best["average"]:
                best = student

        top_5.append(best)
        remaining.remove(best)
    
    print("\nTop 5 Students:")
    for entry in top_5:
        print(f"    {entry['name']}: {entry['average']} ({entry['letter']})")

if __name__ == "__main__":
    main()

