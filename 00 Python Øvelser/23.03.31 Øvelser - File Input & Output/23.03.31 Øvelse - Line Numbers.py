# Write a program that asks the user for a name of a file.
# The program should display the contents of the file
# with each line preceded with a line number followed by a colon.
# The line numbering should start at 1.


def main():
    #createFile()

    #writeToFile("bajs.txt")            # Wrote "1 2 3" to the file
    #writeToFile("bajs.txt")            # Wrote "4 5 6" to the file
    #writeToFile("bajs.txt")            # Wrote "7 8 9" to the file
    #openFile("bajs.txt")
    line1 = readlineContent("bajs.txt")
    print(line1)

    #deleteContent("bajs.txt")


# This function prompts the user for a name
# and creates a file with that name
def createFile():
    userFileName = open(input("What would you like to name your file?\n"), "w")



# This function takes an argument (the name of a file),
# prompts the user for what they want to write to the file
# and then appends the content to the file
def writeToFile(fileName):
    openFile = open(fileName, "a")
    openFile.write(input("What would like to write to the file?\n") + " ")
    openFile.close()


# This file loads a file into memory
# and displays the contents
def openFile(fileName):
    openFile = open(fileName)
    fileContent = openFile.read()
    openFile.close()
    print(fileContent)


# This function takes an argument (the name of a file)
# and then deletes the content of the file
def deleteContent(fileName):
    open(fileName, "w").close()

def listContent(fileName):
    openFile = open(fileName, "r")
    listName = openFile.readlines()
    openFile.close()
    print(listName)

def readlineContent(fileName):
    openFile = open(fileName, "r")
    lineRead = openFile.readline()
    openFile.close()
    return lineRead



main()