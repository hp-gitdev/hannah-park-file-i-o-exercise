numbers = [85, 92, 78, 95, 88, 70, 93]

def calculate(numbers):
    if not numbers:
        return 0
        
    return sum(numbers)/len(numbers)

def max_and_min(numbers):
    if not numbers:
        return (None, None)
    
    max_number = numbers[0]        #[0] this means the index 0, thus, the first numer in the list, not the value of 0.
    min_number = numbers[0]
    
    for num in numbers:     #this literally means every number will be going through in the list of "numbers"
       if num > max_number:
           max_number = num
       if num < min_number:
           min_number = num
    return (max_number, min_number)


def count_occurences(numbers, target):
    count = 0
    for num in numbers:
        if num == target:
            count += 1
    return count


def create_report(numbers):
    
    calculate_average = calculate(numbers)
    highest, lowest = max_and_min(numbers)

    report = f"=== Report ===\n"
    report = report + f"Average: {calculate_average:.1f}\n"
    report = report + f"Highest score: {highest}\n"
    report = report + f"Lowest score: {lowest}\n"

    return report


def is_palindrome(text):
    text = text.lower()
    forward_text = ""
    for spelling in text:
        if spelling ==" ":
            continue
        forward_text = forward_text + spelling

    backward_text = ""
    for spelling in text:
        if spelling == " ":
            continue
        backward_text = spelling + backward_text

    return forward_text == backward_text
