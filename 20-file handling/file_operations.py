"""
File Operations in Python

Examples of reading, writing, appending, updating, and managing files
and directories in Python.
"""

# ============================================================
# 1. Opening and Reading Files
# ============================================================

# Create a new file using "x" mode.
# with open("Files/demo.txt", "x", encoding="utf-8") as file:
#     pass

# Open a file in read mode.
# file = open("Files/demo.txt", "r", encoding="utf-8")

# Read the file line by line.
# print(file.readline())
# print(file.readline())

# Read the entire file.
# print(file.read())

# Avoid extra spaces between printed lines.
# print(file.readline(), end="")

# Read all lines using a for loop.
# for line in file:
#     print(line, end="")

# Close the file.
# file.close()

# Read all lines and return them as a list.
# print(file.readlines())

# Access a specific line from the list.
# lines = file.readlines()
# print(lines[2])

# Iterate through the list of lines.
# for line in file.readlines():
#     print(line, end="")


# ============================================================
# 2. File Pointer: seek() and tell()
# ============================================================

# Change the file pointer position using seek().
# with open("Files/demo.txt", "r", encoding="utf-8") as file:
#     print(file.read(10))
#     print("---------")
#     file.seek(0)
#     print(file.read())

# Check whether a file is closed.
# file = open("Files/demo.txt", "r", encoding="utf-8")
# print(file.closed)
# file.close()
# print(file.closed)

# Reading from a closed file would raise an error.
# print(file.read())

# Using "with" automatically closes the file after the block finishes.
# with open("Files/demo.txt", "r", encoding="utf-8") as file:
#     print(file.read())

# tell() returns the current position of the file pointer.
# with open("Files/demo.txt", "r", encoding="utf-8") as file:
#     print(file.read(10))
#     print(file.tell())
#     print(file.read(10))
#     print(file.tell())


# ============================================================
# 3. Reading Files with "with"
# ============================================================

# Read the entire file using a for loop.
# with open("Files/demo.txt", "r", encoding="utf-8") as file:
#     for line in file:
#         print(line, end="")

# Read the file line by line.
# with open("Files/demo.txt", "r", encoding="utf-8") as file:
#     print(file.readline(), end="")
#     print(file.readline(), end="")
#     print(file.readline(), end="")

# Read all lines and iterate through them.
# with open("Files/demo.txt", "r", encoding="utf-8") as file:
#     for line in file.readlines():
#         print(line, end="")


# ============================================================
# 4. File Methods
# ============================================================

# readable() checks whether the file can be read.
# with open("Files/demo.txt", "r", encoding="utf-8") as file:
#     print(file.readable())

# A file opened with "x" mode is not readable.
# with open("Files/newfile.txt", "x", encoding="utf-8") as file:
#     print(file.readable())

# seekable() checks whether the file supports changing
# the file pointer position.
# with open("Files/demo.txt", "r", encoding="utf-8") as file:
#     print(file.seekable())

# Move the file pointer to a specific position.
# with open("Files/demo.txt", "r", encoding="utf-8") as file:
#     file.seek(53)
#     print(file.read())

# truncate() can be used to resize a file.
# with open("Files/demo.txt", "r+", encoding="utf-8") as file:
#     file.truncate(20)


# ============================================================
# 5. Writing to Files
# ============================================================

# "w" mode writes to a file.
# If the file already exists, its previous content is overwritten.
# with open("Files/newfile.txt", "w", encoding="utf-8") as file:
#     file.write("How is it going?\n")

# Read the written content.
# with open("Files/newfile.txt", "r", encoding="utf-8") as file:
#     print(file.read())

# writelines() writes multiple strings to a file.
# fruits = ["grape\n", "strawberry\n", "fig\n", "banana\n"]

# with open("Files/newfile.txt", "w", encoding="utf-8") as file:
#     file.writelines(fruits)

# with open("Files/newfile.txt", "r", encoding="utf-8") as file:
#     print(file.read())


# ============================================================
# 6. Appending to Files
# ============================================================

# "a" mode adds new content without deleting existing content.
# with open("Files/newfile.txt", "a", encoding="utf-8") as file:
#     file.write("\nThis line was added later!")

# with open("Files/newfile.txt", "r", encoding="utf-8") as file:
#     print(file.read())


# ============================================================
# 7. Reading and Writing Modes
# ============================================================

# "w+" allows both writing and reading.
# Existing content is overwritten when the file is opened.
# with open("Files/newfile.txt", "w+", encoding="utf-8") as file:
#     file.write("New Content!")
#     file.seek(0)
#     print(file.read())

# "a+" allows appending and reading.
# with open("Files/newfile.txt", "a+", encoding="utf-8") as file:
#     file.write("Append mode\n")
#     file.seek(0)
#     print(file.read())

# "r+" allows both reading and writing without automatically
# deleting the existing content.
# with open("Files/newfile.txt", "r+", encoding="utf-8") as file:
#     print("Original Content:")
#     print(file.read())
#
#     file.seek(0)
#     file.write("Updated")
#
#     file.seek(0)
#     print("\nUpdated Content:")
#     print(file.read())


# ============================================================
# 8. Deleting Files
# ============================================================

# Use os.remove() to delete a file.
# import os
#
# if os.path.exists("Files/newfile.txt"):
#     os.remove("Files/newfile.txt")
# else:
#     print("The file does not exist.")


# ============================================================
# 9. Working with Directories
# ============================================================

# import os

# Remove an empty directory.
# os.rmdir("NewFolder")

# List files and directories in the current directory.
# print(os.listdir())

# Create a new directory.
# os.mkdir("NewFolder")

# Check the directory contents after creating it.
# print(os.listdir())

# Remove the directory.
# os.rmdir("NewFolder")


# ============================================================
# 10. Updating File Content
# ============================================================

# Add new content to the beginning of a file.
# with open("Files/demo.txt", "r+", encoding="utf-8") as file:
#     content = file.read()
#     content = "1-Python\n" + content
#
#     file.seek(0)
#     file.write(content)
#     file.truncate()
#
#     file.seek(0)
#     print(file.read())


# ============================================================
# 11. Inserting Content into a File
# ============================================================

# Insert a new line at a specific position.
# with open("Files/demo.txt", "r+", encoding="utf-8") as file:
#     lines = file.readlines()
#     lines.insert(3, "4-Java\n")
#
#     file.seek(0)
#     file.writelines(lines)
#     file.truncate()
#
#     file.seek(0)
#     print(file.read())
