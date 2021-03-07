# Author: Charles Ryan Barrett
# Date: 3/7/2021
# Description: A simple python program that takes in a text files of names/words and sorts them alphabetically
# and by length

# Method to read textfile and sort
def sortText(filename):
    text = getWords(filename)
    # Sort the text alphabetically
    text.sort()
    # Sort the text by length in ascending order
    text.sort(key=len, reverse=False)
    return text     # Return the sorted text list


# Method to turn textfile into a list of words
def getWords(filename):
    text = []   # Placeholder list to hold the words from the text file
    # First, open the text file to be sorted
    with open(filename, "r") as words:
        # Add each word from the textfile into the list
        for word in words:
            text.append(word.strip())   # Remove any spaces or new line tags
    return text     # return the words as a list


def main():
    # Enter filename of text we wish to sort
    filename = "Sort Me.txt"
    # Get the file sorted
    text = sortText(filename)
    # Print out the newly sorted list of words
    print(text)


if __name__ == '__main__':
    main()