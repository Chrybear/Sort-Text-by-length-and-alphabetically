# Author: Charles Ryan Barrett
# Date: 3/7/2021
# Description: A simple python program that takes in a text files of names/words and sorts them alphabetically
# and by length. It also gives the option to save the sorted words into a new text file.

import os.path


# Method to sort text file
def sortText(filename):
    # Get the words as a list
    text = getWords(filename)
    # Sort the text alphabetically
    text.sort()
    # Sort the text by length in ascending order
    text.sort(key=len, reverse=False)
    return text     # Return the sorted text list


# Method to turn text file into a list of words
def getWords(filename):
    text = []   # Placeholder list to hold the words from the text file
    # Open the text file to be sorted
    with open(filename, "r") as words:
        # Add each word from the textfile into the list
        for word in words:
            text.append(word.strip())   # Remove any spaces or new line tags
    return text     # return the words as a list


def main():
    # Loop while user gives inputs
    while True:
        # Get user input file name. Program only designed for .txt files, so must be strict with the file type
        uInput = input("\nPlease enter the filename of the txt file you wish to be sorted *Exclude file extension*:")
        # Check if file exists
        if os.path.isfile(uInput+'.txt'):
            text = sortText(uInput+'.txt')  # Send file to be sorted
            print(text)  # Print out the sorted file

            if input("\nWould you like to save the sorted file? Y/N:").lower() == 'y':
                with open(uInput+'_sorted.txt', 'w') as x:
                    for word in text:
                        x.write(word+'\n')

            # Ask user if they want to enter another file
            if input("\nWould you like to enter another txt file? Y/N:").lower() == 'n':
                print("So long!")
                break   # Break out of the loop and exit the program
        else:   # File name entered did not exist in directory/location sortLenAlph.py does
            print("Error: no file named '"+uInput+".txt'. Please make sure it exists and/or is spelt correctly\n")


if __name__ == '__main__':
    main()