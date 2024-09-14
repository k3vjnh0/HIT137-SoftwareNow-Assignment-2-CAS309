import os


def clear_screen():
    """
    Clear the terminal screen based on the operating system
    """
    os.system("cls" if os.name == "nt" else "clear")


def load_text_from_file(file_path):
    """
    Load text data from a file.

    Args:
        file_path (str): The path to the file to load.

    Returns:
        str: The text content of the file.
    """
    try:
        with open(file_path, "r") as file:
            text = file.read()
        return text
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return None
    except Exception as e:
        print(f"An error occurred while loading the file: {e}")
        return None


def ensure_paths(input_file_path, output_file_path):
    """
    Ensures the input file exists and the output directory is ready.
    Args:
        input_file_path (str): Path to the input file.
        output_file_path (str): Path to the output file.
    Returns:
        bool: True if the input file exists and the output directory is ready,
                False otherwise.
    """
    # Check if the input file exists
    if not os.path.isfile(input_file_path):
        print(f"Error: The file '{input_file_path}' does not exist.")
        return False

    # Check if the output directory exists, create it if not
    output_dir = os.path.dirname(output_file_path)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Created the output directory: {output_dir}")

    return True


def get_text_from_input():
    """
    Determines whether the provided input is a file path or a direct string.
    If it's a file path, it reads and returns the file's content.
    Otherwise, it treats the input as a direct string and returns it.
    """
    # Get the input data from the user
    input_data = input("Enter the text or path to the text file: ")

    # Check if the input is a valid file path
    if os.path.isfile(input_data):
        try:
            # Read the file content and return it
            with open(input_data, "r") as file:
                content = file.read()
                print("File content extracted for analysis.")
                return content
        except IOError:  # Handle file reading errors
            print(f"An error occurred while trying to read the file '{input_data}'.")
            return None
    else:  # Treat the input as a direct string
        print(f"The file '{input_data}' does not exist.")
        print("Input treated as a direct string for analysis.")
        return input_data


def check_input_conditions(prompt):
    while True:
        try:
            num = int(input(prompt))
            # Check if the number is positive.
            if num > 0:
                return num
            raise ValueError
        # Handle invalid input, should input a positive integer.
        except ValueError:
            print("Invalid input, should input a positive integer. Please try again.")


# Helper Function for loading encrypted code
def get_encrypted_text(file_path, sample_text=""):
    """
    A helper function to get encrypted code by either:
    - Manually inputting
    - Loading from a file
    - Using a sample text

    :param file_path: Path to the file where encrypted code may be stored.
    :param sample_text: The predefined sample text to use as an alternative.
    :return: The encrypted code as a string.
    """
    print("\nSelect an option to load the encrypted code:")
    print("1. Input manually")
    print("2. Load from a file")
    print("3. Use sample encrypted text")
    while True:
        option = input("Select an option: ")

        if option == "1":
            return input("Enter the encrypted text: ")
        elif option == "2":
            if os.path.exists(file_path):
                with open(file_path, "r") as file:
                    content = file.read()
                    print(f"\nUsing sample encrypted text:\n{content}")
                    return content
            else:
                print("\nNo encrypted file found.")
                return ""
        elif option == "3":
            print(f"\nUsing sample encrypted text:\n{sample_text}")
            return sample_text
        else:
            print("Invalid option selected.")
