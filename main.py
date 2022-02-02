import json
import re
 
# Opening JSON file
words_file = open('words.json')
 
#  Load all possible words into the array
words = json.load(words_file)

# Closing file
words_file.close()

lettersRegex = [
    ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'], 
    ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'], 
    ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'], 
    ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'], 
    ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
]

while True:
    wordCount = len(words)
    print(f"Available Words: {wordCount}")
    if(wordCount < 10):
        # List possible words
        print("Possible Words: " + ", ".join(words))

    # Input word
    print('Legend: X = Green, ? = Yellow, _ = N/A')
    wordResult = input("Enter your word and the result (e.g ZOBB - X__?): ")

    # Parse Input
    tempArray = wordResult.split(" - ")
    letters = list(tempArray[0])
    pattern = list(tempArray[1])

    for i in range(5):
        if(pattern[i] == '_'):
            # Excluded
            # Loop through 'lettersRegex' and remove character from all arrays (if it is there)
            for letterRegex in lettersRegex:
                if letters[i] in letterRegex:
                    letterRegex.remove(letters[i])
        elif pattern[i] == 'X':
            # mark letterRegex position as only this character
            lettersRegex[i] = [letters[i]]
        elif pattern[i] == '?':
            # mark letterRegex position has this character excluded
            if letters[i] in lettersRegex[i]:
                lettersRegex[i].remove(letters[i])

    # Filter Word List
    # _ - excluded
    # ? - Any position but green and current position
    # X - MUST MATCH THIS POSITION AND LETTER

    # Build regex for filtering
    regex = ""
    for letterRegex in lettersRegex:
        regex += "["
        regex += ",".join(letterRegex)
        regex += "]"


    # Loop through word list and filter
    filteredList = []
    for word in words:
        if re.match(regex.lower(), word):
            filteredList.append(word)
    words = filteredList
    




