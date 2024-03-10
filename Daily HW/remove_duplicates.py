#initialize Function Remove Duplicate
def remove_duplicates(input_string):
    # Initialize an empty string to store the result
    result = ""
    
    # Iterate through the input string
    for char in input_string:
        # If the current character is not equal to the previous character, add it to the result
        if not result or char != result[-1]:
            result += char
    return result

# Example usage
input_str_1 = input("Enter Word: ")  #input: hello
output_1 = remove_duplicates(input_str_1)
print("output: "+ output_1)  # Output: "helo"
