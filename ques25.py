def copyfile(source_file, destination_file):
    try:
        with open(source_file, 'r') as source:
            with open(destination_file, 'w') as dest:
                dest.write(source.read())
        print(f"File '{source_file}' has been copied to '{destination_file}' successfully.")
    except FileNotFoundError:
        print("Error: One or both files not found.")


source_file = input("Enter the path of the source file: ")
destination_file = input("Enter the path of the destination file: ")

copyfile(source_file, destination_file)