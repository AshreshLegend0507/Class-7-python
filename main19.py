def check_alphabets(input_string):
    if input_string.isalpha():
        print("The text contains only alphabets.")
    else:
        print("The text does not contain alphabets.")

# Example usage
user_input = input("Enter text: ")
check_alphabets(user_input)