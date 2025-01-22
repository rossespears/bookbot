def main():
    fileContents = ""
    bookFile = "books/frankenstein.txt"
    wordCount = 0
    fileContents = getBooksText(bookFile)
    wordCount = getWordCount(fileContents)
    eachLetter = getLetterCounts(fileContents)
    print(f"Book Report for ", bookFile, "\n")
    print(wordCount ,"words are in the document")
    listedLetters = list(eachLetter.items())
    listedLetters.sort()
    for letter in listedLetters:
        if(letter[0].isalpha()):
            print(f"The '{letter[0]}' character was found {letter[1]} times")



def getBooksText(book):
    with open(book) as f:
        fileContents = f.read()
    return fileContents

def getWordCount(Text):
    listOfWords = Text.split()
    return len(listOfWords)

def getLetterCounts(Text):
    loweredText = Text.lower()
    letterDic = {}
    for character in loweredText:
        if(character in letterDic):
            letterDic[character] += 1
        else:
            letterDic[character] = 1
    return letterDic


main()