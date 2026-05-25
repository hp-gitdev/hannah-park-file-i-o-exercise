
scores = [88, 45, 92, 67, 73, 95, 81, 56, 78, 100, 62, 85, 90, 38, 71]

for score in scores:
    if 90 <= score <= 100:
        print(f"{score}: A")
    elif 80 <= score <= 89:
        print(f"{score}: B")
    elif 70 <= score <= 79:
        print(f"{score}: C")
    elif 60 <= score <= 69:
        print(f"{score}: D")
    elif score < 60:
        print(f"{score}: F")


print("\nGrade Distribution:")

letter_grades = {"A":0, "B":0, "C":0, "D":0, "F":0}

for score in scores:
    if 90 <= score <= 100:
        letter_grades["A"] += 1
    elif 80 <= score <= 89:
        letter_grades["B"] += 1
    elif 70 <= score <= 79:
        letter_grades["C"] += 1
    elif 60 <= score <= 69:
        letter_grades["D"] += 1
    elif score < 60: 
        letter_grades["F"] += 1

for letter, count in letter_grades.items():
    print(f"{letter}: {count} students")


print("\n=== Grade Analyzer ===")
print(f"Total scores: {len(scores)}")

total = sum(scores)
average = total / len(scores)
print(f"Average: {average:.1f}")

highest = max(scores)
print(f"Highest: {highest}")

lowest = min(scores)
print(f"Lowest: {lowest}")


passing = 0
failing = 0

for score in scores:
    if score > 60:
        passing += 1
    if score < 60:
        failing += 1

num_scores = len(scores)

pass_fail = {
    "Passing": passing,
    "Failing": failing
}

for category, count in pass_fail.items():
    percent = count / num_scores * 100
    print(f"{category}: {count} ({percent:.1f}%)")


print("\n--- Add More Scores ---")

new_score = input("New score: ")

try:
    new_score = int(new_score)
except ValueError:
    print("Enter a whole number.")


scores.append(new_score)

new_average = total / len(scores)
print(f"\n Updated average: {new_average}")


while True:
    entry = input("Enter a score (or 'done' to finish): ")
    
    if entry.lower() == "done":
        break
    
    try:
        score = int(entry)
        scores.append(score)
    except ValueError:
        print("Please enter a whole number or 'done'.")

if scores:
    average = sum(scores) / len(scores)
    print(f"Final average: {average:.1f}")

else:
    print("No scores entered.") 