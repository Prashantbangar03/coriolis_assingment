from  pallindrom_version import is_Palindrome


def palidrome_file(filepath):
    file = open(filepath)
    for line in file.read().split("\n"):
        if is_Palindrome(line)=="Pallindrom":
           print(line)
            



palidrome_file("17.pallindrom_version.py")
