# Reads a file and returns a list of words
def readFile(file):
    f = open(file, "r")
    words = []
    for line in f:
        words.append(line.strip())
    f.close()
    return words

# Gets the specific letters from an array with a specific colour
def getSpecificLetters(array,colour):
    if(colour=='g' or colour=='grey'):
        return array[0]
    elif(colour=='y' or colour=='yellow'):
        return array[1]
    elif(colour=='g' or colour=='green'):
        return array[2]
    else:
        print("ERROR getSpecificLetters(). Could not find letters with keyword",colour,". Please ensure you use: 'grey' , 'yellow' , 'green'")

# Enforces the user input 5 characters each time
def validateInput(letters):
    while(len(letters) != 5 or letters.isdigit()):
        print("Error. Must contain exactly 5 characters (no digits). Use the underscore '_' to represent the absence of a letter. Please enter the 5 digits:")
        letters = input()
    return letters

# Gets the grey,yellow,green letters.
def promptUserForInputs():
    letters = []
    prompts = [
        "Please input grey letters:",
        "Please input yellow letters:",
        "Please input green letters:"
        ]

    for prompt in prompts:
        print(prompt)
        userLetters = validateInput(input())
        letters.append(userLetters)
    return letters

# Just displays game instructions to user
def displayInstructions():
    print()
    print("     +==========================+")
    print("     | WELCOME TO WORDLE SOLVER |")
    print("     +==========================+")
    print("        ~  Created by: Josh  ~  ")
    print()
    print("     +--------------------------+")
    print("     |       INSTRUCTIONS       |")
    print("     +-------------------------=+")
    print(" 1. You will input your letters you get in 3 different categories:")
    print("   - Grey Letters")
    print("   - Yellow Letters")
    print("   - Green Letters")
    print(" 2. Use the underscore [ _ ] to indicate no letter, otherwise use the letter given.")
    print(" 3. Must use lowercase characters only, and no spaces!")
    print()
    print("     Example: ")
    print("         Input grey letters:    l _ n _ s  ")
    print("         Input yellow letters:  _ i _ e _  ")
    print("         Input green letters:   _ _ _ _ _  ")
    print()
    print(" Goodluck! And remember, you have 6 attempts if you're playing the standard version.")

# Calculates how many words are in a list
def getNumberOfWords(wordList):
    numberOfWords = 0
    for i,w in enumerate(wordList):
        numberOfWords = i
    return numberOfWords

# Calculates a good guess from a list of possible words
def findRecommendedGuess(wordList):
    # TODO - Just a sample word, will have to complete later.
    return 'N/A'

# Checks a list, to determine if there are any letters
def containsLetters(list):
    foundLetter = False
    for x in list:
        if(x != '_'):
            foundLetter = True
    return foundLetter

# Goes through the wordList removing words using the greyLetters
def modifyListUsingGreyLetters(wordList,greyList,greenList):
    for i,greyLetter in enumerate(greyList):
        if(greyLetter != "_"):
            for word in wordList:
                if(greyLetter in word):
                    if(greyLetter != greenList[i]):
                        if(greyLetter not in greenList):
                            if(word in wordList):
                                wordList.remove(word)
    return wordList

def modifyListUsingGreenLetters(wordList,greenList):
    for i,greenLetter in enumerate(greenList):
        if(greenLetter != "_"):
            for word in wordList:
                if(greenLetter != word[i]):
                        wordList.remove(word)
    return wordList

def modifyListUsingYellowLetters(wordList,yellowList,greenList):
    for i,yellowLetter in enumerate(yellowList):
        for word in wordList:
            if(yellowLetter != "_"):
                if(yellowLetter not in greenList):
                    if(yellowLetter == word[i]):
                        if(word in wordList):
                            wordList.remove(word)
                    if(yellowLetter not in word):
                        if(word in wordList):
                            wordList.remove(word)
    return wordList
                
def updateWordList(wordList,greyList,yellowList,greenList,numberOfLoops):
    
    # Find words that contain the exact letter in it's exact position (GREEN)
    if(containsLetters(greenList)):
        for x in range(numberOfLoops):
            wordList = modifyListUsingGreenLetters(wordList,greenList)

    # Find words that don't contain the grey letters
    if(containsLetters(greyList)):
        for x in range(numberOfLoops):
            wordList = modifyListUsingGreyLetters(wordList,greyList,greenList)

    # Find words that contain yellow letters, but not in their current position
    if(containsLetters(greyList)):
        for x in range(numberOfLoops):
            wordList = modifyListUsingYellowLetters(wordList,yellowList,greenList)

    return wordList

def play(wordList):
    currentAttempt = 1
    letters = []

    displayInstructions()
    
    # While they have attempts remaining, and there is 2 or more possible answers
    while(currentAttempt <= MAX_ATTEMPTS and getNumberOfWords(wordList)>1):
        
        # Get input from the user (grey,yellow,green letters)
        letters = promptUserForInputs()
        
        # Put the inputted letters into a list
        greyLetters = list(getSpecificLetters(letters,'grey'))
        yellowLetters = list(getSpecificLetters(letters,'yellow'))
        greenLetters = list(getSpecificLetters(letters,'green'))

        wordList = updateWordList(wordList,greyLetters,yellowLetters,greenLetters,30)
        currentAttempt += 1

        print()
        print("Remaining words:",wordList)
        print("+-------------------------------------------------------")
        print("|    Grey   ",greyLetters)
        print("|    Yellow ",yellowLetters)
        print("|    Green  ",greenLetters)
        print("|    # of attempts remaining:",MAX_ATTEMPTS-(currentAttempt-1),"(out of",MAX_ATTEMPTS,")")
        print("|    # of possible words:",getNumberOfWords(wordList))
        print("|    Try using:",findRecommendedGuess(wordList))
        print("+-------------------------------------------------------\n")
        print()

    print("Game finished. Good job!")
    print("Number of Remaining Words",getNumberOfWords(wordList))
    print("Final remaining words:",wordList)

#------------------------------------------------#
wordList = readFile("updatedWords.txt")
wordList.sort()
MAX_ATTEMPTS = 6

# Plays the game
play(wordList)