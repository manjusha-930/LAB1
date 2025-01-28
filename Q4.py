def highest_occurrence(input_string):
    # Filtering out alphabets and convert to lowercase
    filtered_string = ''.join(char.lower() for char in input_string if char.isalpha())
    # Dictionary to store character frequencies
    char_count = {}
    # Counts occurrence of each character
    for char in filtered_string:
        char_count[char] = char_count.get(char, 0) + 1
    # Finding the character with the maximum occurrences
    max_char = max(char_count, key=char_count.get)
    max_count = char_count[max_char]
    return max_char, max_count
# Example
input_string = "hippopotamus"
max_char, max_count = highest_occurrence(input_string)
print(f"The maximally occurring character is '{max_char}' with an occurrence count of {max_count}.")
