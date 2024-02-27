# Create a class for creating and writing data to a text file. The class must have __enter__ and __exit__
# defined.
# __enter__ must use the built in `open` to open the file and set the file pointer to self.
# __exit__ must close the file pointer on exit.
# If the user entered text contains the word 'bug' then __exit__ must delete the file on exiting.
# Or if any exception has occurred, then also __exit__ must delete the file.(remember to close file
# before deleting)
# Use a `with` block to execute the logic

import os

class FileHandler:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.file = open(self.filename, 'w')
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()
        if exc_type is not None or self.contains_bug():
            os.remove(self.filename)

    def contains_bug(self):
        with open(self.filename, 'r') as f:
            for line in f:
                if 'bug' in line:
                    return True
        return False

filename = "file.txt"

try:
    with FileHandler(filename) as file:
        text = input("Enter text: ")
        file.write(text)
except Exception as e:
    print("An error occurred:", e)
 