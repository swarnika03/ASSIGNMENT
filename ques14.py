def readlines():
    lines = []
    print("Enter your lines of text (press Enter on an empty line to finish):")
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    return lines

def printlines(lines):
    print("\nYou entered:")
    for line in lines:
        print(line)

# Main program
lines = readlines()
printlines(lines)