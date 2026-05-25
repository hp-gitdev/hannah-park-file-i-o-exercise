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

letter_grade = {"A":0, "B":0, "C":0, "D":0,"F":0}

for score in scores:
    if 90 <= score <= 100:
        letter_grade['A'] += 1
    elif 80 <= score <= 89:
        letter_grade['B'] += 1
    elif 70 <= score <= 79:
        letter_grade['C'] += 1
    elif 60 <= score <= 69:
        letter_grade['D'] += 1
    elif score < 60:
        letter_grade['F'] += 1

# even if you don't define what letter or count is, python understands letters are letter grades, and count on its own.
for letter, count in letter_grade.items():      
    print(f"{letter}: {count} students")    #this is key-value pair

total_score = len(scores)
print(f"Total score: {total_score}")

average = sum(scores)/len(scores)
print(f"Average score: {average:.2f}")

highest = max(scores)
lowest = min(scores)
print(f"Highest score: {highest}")
print(f"Lowest score: {lowest}")

passing = 0
failing = 0

for score in scores:
    if score >= 60:
        passing += 1
    else:
        failing += 1

pass_fail = {
    "passing": passing,
    "failing": failing 
}

num_score = len(scores)


for category, count in pass_fail.items():  
    percent = count / len(scores) * 100    
    print(f"{category}: {count} students {percent}%") 


add_score = int(input("Enter a score: "))
if add_score:
    scores.append(add_score)
    new_average = sum(scores) / len(scores)
    print(f"Updated average: {new_average:.2f}")


while True:
    entry = input("Enter a score (or type 'done'):")

    if entry.lower() == "done":
        break

    try:
        score = int(entry)
        scores.append(score)

    except ValueError:
        print("Please enter a whole number.")

if scores:
    final_average = sum(scores)/len(scores)
    print(f"Final average: {final_average:.1f}")
else:
    print("done")