

numbers = [88, 45, 92, 67, 73, 95, 88, 56, 78, 100, 62, 88, 90, 38, 71]

def calculate_average(numbers):
    """Calculate the average of the list."""

    if not numbers:
        return 0
    
    return sum(numbers)/len(numbers)

def find_max_and_min(numbers):
    """Find the maximum and the minimum number."""
    if not numbers:
        return (None, None)
    
    max_number = numbers[0]
    min_number = numbers[0]

    for num in numbers:
        if num > max_number:
            max_number = num
        elif num < min_number:
            min_number = num
    return (max_number, min_number)

def count_occurrences(items, target):
    """Count how many times a target value appears in the list"""

    count = 0   #this is counting. how many times the number showes up - not the indext of 0.
    for item in items:
        if item == target:
            count += 1

    return count


def is_palindrome(text):
    """Returns True if text reads the same forward and backward."""
    text = text.lower()
    
    forward_text = ""        #same as setting count = 0 for numbers.
    for char in text:
        if char == " ":
            continue
        forward_text = forward_text + char
    
    reversed_text = ""      
    for char in text:
        if char == " ":     
            continue
        reversed_text = char + reversed_text

    return forward_text == reversed_text


def create_report(title, scores):
    """Returns a formatted string report."""
    
    average = calculate_average(scores)
    highest, lowest = find_max_and_min(scores)

    report = f"=== {title} ===\n"
    report = report + f"Average: {average:.1f}\n"
    report = report + f"Highest: {highest}\n"
    report = report + f"Lowest: {lowest}\n"
    return report


if __name__ == "__main__":
    # Test each function
    test_scores = [85, 92, 78, 95, 88, 70, 93]
    
    print(f"Average: {calculate_average(test_scores)}")
    print(f"Max/Min: {find_max_and_min(test_scores)}")
    print(f"Count of 85: {count_occurrences(test_scores, 85)}")
    print(f"'racecar' palindrome: {is_palindrome('racecar')}")
    print(f"'hello' palindrome: {is_palindrome('hello')}")
    print()
    print(create_report("Class Scores", test_scores))


