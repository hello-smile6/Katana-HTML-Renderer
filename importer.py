import parser
#fileName = "test.html"
fileName = input("Enter HTML file: ")

#convert the file to a list for parsing

def parse(toParse):
    i = 0
    parseValue = ""
    while (i < len(toParse)):
        if i > 0:
            parseValue += toParse[i]
        if toParse[i] == ">":
            input.append(parseValue)
            parseValue = ""
        i+=1

#Import the HTML file to parse
def read():
    with open(fileName, "r") as file:
        readline=file.read().split("\n")
    parser.parse(readline)
read()
