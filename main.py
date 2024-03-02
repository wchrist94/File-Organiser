import os
import shutil

# Ask for the path to the folder
path = input("Enter the path to the folder: ")

files = os.listdir(path)

for file in files:
    filename, file_extension = os.path.splitext(file)
    file_extension = file_extension[1:]

    if os.path.exists(path + '/' + file_extension):
        shutil.move(path + '/' + file, path + '/' + file_extension + '/' + file)

    else:
        os.makedirs(path + '/' + file_extension)
        shutil.move(path + '/' + file, path + '/' + file_extension + '/' + file)
