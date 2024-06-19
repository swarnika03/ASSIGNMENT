def read_and_print_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except IOError:
        print(f"Error: Could not read the file '{file_path}'.")


file_path = input("Enter the path of the text file: ")
read_and_print_file(file_path)