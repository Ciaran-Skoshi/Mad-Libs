import os

def main():
    madLibsDir = "madLibs"
    madLibsFiles = []
    selectedMadLib = ""
    fillInWords = []
    filledInWords = []
    print('Checking "MadLibs"...')
    madLibsFiles = getMadLibs(madLibsDir)
    if len(madLibsFiles) < 0:
        print(f'No files found in "{madLibsDir}"! please put your MadLibs in the {madLibsDir} folder and make sure they have the ".txt" extension.')
        return
    selectedMadLib = selectMadLib(madLibsFiles)
    fillInWords = getFillInWords(selectedMadLib)
    if len(fillInWords) < 0:
        print(f"No words to be filled in detected! words to be filled need to be incased in [] e.g. [Adjective], [Noun (plural)], [Verb ending in ing], etc.")
        return
    filledInWords = playMadLib(fillInWords)
    showMadLib(selectedMadLib, fillInWords, filledInWords)

def getMadLibs(dir :str) -> list:
    madList = []
    for file in os.scandir(dir):
        if file.name.endswith(".txt"):
            madList.append(file)
    return madList

def selectMadLib(files :list) -> str:
    x = 1
    for filename in files:
        print(f"{x}. {filename.name}")
        x += 1
    while True:
        select = input("Please select the number of the Mad Lib you want: ")
        try:
            select = int(select)
            break
        except:
            print('Please enter a vaild string/number (The number you see before the ".")')
    select -= 1
    with open(os.path.join(files[select]), "r") as f:
        content = f.read()
    return content

def getFillInWords(content :str) -> list:
    words = []
    currWord = ""
    inBrackets = False
    for c in content:
        if c == "[":
            inBrackets = True
        elif c == "]":
            inBrackets = False
            words.append(currWord)
            currWord = ""
        elif inBrackets:
            currWord += c
    return words

def playMadLib(fillInWords :list) -> list:
    filledInWords = []
    for x in fillInWords:
        filledInWords.append(input(f"Please enter a(n) {x}: "))
    return filledInWords

def showMadLib(madLib :str, fillInWords: list, filledInWords :list):
    for x in range(len(filledInWords)):
        if filledInWords[x] == "":
            filledInWords[x] = "Word Not Entered"
        madLib = madLib.replace("[" + fillInWords[x] + "]", filledInWords[x], 1)
    print("Mad Lib: ", madLib)

if __name__ == "__main__":
    main()
