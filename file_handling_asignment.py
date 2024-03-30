# file_handling_assignment.py

def create_file():
    try:
        # Create a new text file named "my_file.txt" in write mode ('w')
        with open("my_file.txt", "w") as file:
            file.write("Hello, this is line 1.\n")
            file.write("12345 is a number.\n")
            file.write("Python is awesome!\n")
        print("File 'my_file.txt' created successfully.")
    except FileNotFoundError:
        print("Error: File not found.")
    except PermissionError:
        print("Error: Permission denied.")

def read_and_display():
    try:
        # Read the contents of "my_file.txt" and display them on the console
        with open("my_file.txt", "r") as file:
            content = file.read()
            print("Contents of 'my_file.txt':\n", content)
    except FileNotFoundError:
        print("Error: File not found.")
    except PermissionError:
        print("Error: Permission denied.")

def append_to_file():
    try:
        # Append three additional lines of text to the existing content
        with open("my_file.txt", "a") as file:
            file.write("Appending line 1.\n")
            file.write("Appending line 2.\n")
            file.write("Appending line 3.\n")
        print("Content appended to 'my_file.txt'.")
    except FileNotFoundError:
        print("Error: File not found.")
    except PermissionError:
        print("Error: Permission denied.")

if __name__ == "__main__":
    create_file()
    read_and_display()
    append_to_file()