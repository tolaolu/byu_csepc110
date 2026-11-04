""""
For reusability of this program and to get points for going beyond the requirements, 
I would be importing the os module so this program uses dynamic file paths to the wordlist and toppasswords files.
This will allow the program to be run from any directory without having to worry about the location of the files.
"""

import os


# The constants that define 4 character lists required for the checks
LOWER=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
UPPER=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
DIGITS=["0","1","2","3","4","5","6","7","8","9"]
SPECIAL=["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", "'", "\"", ",", ".", "<", ">", "?", "/", "\\","`", "~"]

def word_in_file(word, filename, case_sensitive=False):
    """
    Reads a file where each line contains a single word.
    Returns True if the word is found, otherwise returns False.
    """
    
    with open(filename, "r", encoding="utf-8") as openedFile:
        for eachLine in openedFile:
            wordOnEachLine = eachLine.strip() # Clean the word on the current line of spaces before n after it.
            
            if case_sensitive:
                # Case-sensitive comparison
                if wordOnEachLine == word:
                    return True
            else:
                # Case-insensitive comparison
                if wordOnEachLine.lower() == word.lower():
                    return True
                    
    return False # meaning the word inputed was not found anywhere in the file

#func to check if a word has any character from a given character list
def word_has_character(word, character_list):
    for everyCharacter in character_list:
        if everyCharacter in word:
            return True
    return False

# The password complexity determination function 
def word_complexity(word):
    # Start the complexity rating at 0
    complexity_rating = 0
    
    # Check for lowercase letters
    if word_has_character(word, LOWER):
        complexity_rating += 1
        
    # Check for uppercase letters
    if word_has_character(word, UPPER):
        complexity_rating += 1
        
    # Check for digits
    if word_has_character(word, DIGITS):
        complexity_rating += 1
        
    # Check for special characters
    if word_has_character(word, SPECIAL):
        complexity_rating += 1
        
    return complexity_rating

def password_strength(password, min_length=10, strong_length=16):
    # Checking minimum password length requirement
    if len(password) < min_length:
        print("Password fails minimum length requirements.")
        return 0

    # Checking dictionary and known-password files 
    IsWordInToppasswordsListFile = word_in_file(password, os.path.join(os.path.dirname(__file__), "toppasswords.txt"), case_sensitive=False)
    IsWordInWordlistFile = word_in_file(password, os.path.join(os.path.dirname(__file__), "wordlist.txt"), case_sensitive=False)
    
    if IsWordInToppasswordsListFile or IsWordInWordlistFile:
        print("Your password is found in the Top Passwords or Wordlist files. Please choose a different password.")
        return 1

    # Calling the word_complexity function to get the complexity score of the password
    complexity = word_complexity(password)
    
    # Determine strength score (2 to 5) based on complexity and strong_length
    if complexity < 3:
        print("Password is too weak!.")
        return 2
        
    elif complexity == 3 and len(password) < strong_length:
        print("Password is moderate but could be longer or more complex.")
        return 3
        
    elif complexity >= 3 and len(password) >= strong_length:
        # A score of 4 requires meeting the strong length threshold with solid complexity
        if complexity == 4:
            print("Password is exceptionally strong!")
            return 5
        else:
            print("Password is strong.")
            return 4
    else:
        print("Password meets standard security requirements.")
        return 4
    
# main function to run the password strength program:
def main():
    print("--- Password Strength Program ---")
    print("Enter 'q' or 'Q' at any time to quit.\n")
    
    while True:
        # Prompt the user for input
        user_password = input("Enter a password to test: ")
        
        # Check if user wants to exit the program
        if user_password == 'q' or user_password == 'Q':
            print("Quitting program. Goodbye!")
            break  # Exit the while loop entirely
            
        # If they user does not want to exit the program, then evaluate the password
        score = password_strength(user_password)
        print(f"Final Strength Score: {score}/5\n")

if __name__ == "__main__":
    main()