import glob  # unix shell style pathname pattern expansion

myfiles = glob.glob("files/*.txt")

for filepath in myfiles:
    with open(filepath, "r") as file:
        print(file.read())