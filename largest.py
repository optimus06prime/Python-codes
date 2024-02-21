
def check_largest_num(numbers):
    if not numbers:
        return None  
# Assume the first number is the largest
    largest = numbers[0]  
# return largest if we find a larger number
    for num in numbers[1:]:
        if num > largest:
            largest = num  
    
    return largest

# Use 'split() function' to accept user's input as a list'
sequence = [int(x) for x in input("Enter a sequence of integers separated by space: ").split()]
largest_number = check_largest_num(sequence)
print("The largest number in the sequence is:", largest_number)
