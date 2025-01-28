def calculate_range(numbers):
    # Checking for the list being less than 3 elements
    if len(numbers) < 3:
        return "Range determination not possible"
    # Calculates the range (max - min)
    range_of_list = max(numbers) - min(numbers)
    return range_of_list
# list of real numbers
input_list = [5, 3, 8, 1, 0,4]
result = calculate_range(input_list)
print("Range of the list:", result)
