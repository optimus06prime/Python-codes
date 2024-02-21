def find_largest_number(numbers):
    if not numbers:
        return None  # Return None if the sequence is empty
    
    largest = numbers[0]  # Assume the first number is the largest
    
    for num in numbers[1:]:
        if num > largest:
            largest = num  # Update largest if we find a larger number
    
    return largest

# Example usage
sequence = [int(x) for x in input("Enter a sequence of integers separated by spaces: ").split()]
largest_number = find_largest_number(sequence)
print("The largest number in the sequence is:", largest_number)
