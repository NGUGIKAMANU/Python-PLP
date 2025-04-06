# Error Handling Lab for PLP Python Assignment
# Purpose: Reads a user-specified file, modifies it, and handles errors gracefully

def process_file_with_error_handling():
    """
    Prompts for a filename, reads it, converts to uppercase, and writes to a new file.
    Includes comprehensive error handling with user-friendly feedback.
    """
    # Prompt user for input filename
    input_filename = input("Enter the filename to process (e.g., 'input.txt'): ")

    # Generate output filename by appending '_processed'
    output_filename = input_filename.rsplit('.', 1)[0] + '_processed.txt'

    try:
        # Read the input file safely
        with open(input_filename, 'r') as input_file:
            content = input_file.read()

        # Modify content to uppercase for clear transformation
        modified_content = content.upper()

        # Write to the output file
        with open(output_filename, 'w') as output_file:
            output_file.write(modified_content)

        # Success feedback
        print(f"Success! '{input_filename}' processed and saved as '{output_filename}'.")

    except FileNotFoundError:
        # Handle missing file error
        print(f"Error: '{input_filename}' not found. Please check the filename and path.")
    except PermissionError:
        # Handle access denial
        print(f"Error: Permission denied for '{input_filename}' or '{output_filename}'.")
    except IOError as e:
        # Handle I/O issues (e.g., corrupted file)
        print(f"Error: I/O issue occurred - {str(e)}. Check file integrity.")
    except Exception as e:
        # Catch-all for unexpected errors
        print(f"Unexpected error: {str(e)}. Please retry or seek assistance.")

# Main execution block
if __name__ == "__main__":
    print("=== Error Handling Lab ===")
    process_file_with_error_handling()
    print("Task completed. Happy coding! 💻✨")