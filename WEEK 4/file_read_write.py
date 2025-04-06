# File Read & Write Challenge for PLP Python Assignment
# Purpose: Reads a file and writes a modified version (title case) to a new file

def read_and_write_file(input_filename="input.txt", output_filename="output.txt"):
    """
    Reads content from a file and writes a title-case version to a new file.
    
    Args:
        input_filename (str): Name of the input file (default: 'input.txt')
        output_filename (str): Name of the output file (default: 'output.txt')
    """
    # Read the input file
    with open(input_filename, 'r') as input_file:
        content = input_file.read()

    # Modify content to title case for a clean transformation
    modified_content = content.title()

    # Write the modified content to the output file
    with open(output_filename, 'w') as output_file:
        output_file.write(modified_content)

    # Success message
    print(f"Success! '{input_filename}' processed and saved as '{output_filename}'.")

# Main execution block
if __name__ == "__main__":
    print("=== File Read & Write Challenge ===")
    # Use default filenames for simplicity and consistency
    read_and_write_file()
    print("Task completed. Check 'output.txt' for the result!")
    print("Happy coding! 💻✨")