def clean_name(name):
    # Remove numbers and symbols from the name
    cleaned_name = ''.join(char for char in name if char.isalpha() or char.isspace())
    return cleaned_name.strip()

def reverse_names(input_string):
    # Split the input string into individual names
    names = input_string.split(',')

    # Process each name
    formatted_names = []
    for name in names:
        # Split the name into surname and first name
        parts = name.split()
        if len(parts) >= 2:
            surname, first_name = parts[1], parts[0]
            # Clean the names
            surname = clean_name(surname)
            first_name = clean_name(first_name)
            # Reverse the order and format
            formatted_names.append(f"{surname}, {first_name}")

    # Join the formatted names with semicolons
    result = '; '.join(formatted_names)
    return result

while True:
    # Prompt user for input
    input_str = input("Enter the author names (Press 'x' to exit): ")
    
    # Check if user wants to exit
    if input_str.lower() == 'x':
        break
    
    # Process input and display result
    output_str = reverse_names(input_str)
    print(output_str)