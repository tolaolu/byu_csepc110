# declarations
secretWord = "mend"  # Hardcoded secret word for testing

greeting = "Welcome to the word guessing game!"
promptMessage = "What is your guess? "
nosOfGuesses = 0  # Counter for total valid guesses made by the user

# initial hint filled with underscores matching the secret word length
generateHintMessage = "Your hint is: " + " ".join("_" for i in range(len(secretWord)))

# --- game running logic ---
gameStarted = True
print(greeting)
print("")  # Empty line for spacing

# Display the initial all-underscore hint before the first guess loop
print(generateHintMessage)

while gameStarted:
    # capturing user's guess:
    userGuessInput = input(promptMessage).lower().strip()
    
    # checking if the guess length matches the secret word length
    if len(userGuessInput) != len(secretWord):
        print(f"Sorry, the guess must be {len(secretWord)} letters long.")
        print("")  # extra newline for spacing 
        continue  # Skip calculation and loop back to request input without counting the guess

    # increment the valid guess counter
    nosOfGuesses += 1  
    
    # check for win condition
    if userGuessInput == secretWord:
        print("Congratulations! You guessed it!")
        print(f"It took you {nosOfGuesses} guesses.")
        gameStarted = False  # Break the loop to end the game safely
        
    # generate the dynamic hints if incorrect
    else:
        hint_letters = []
        for i in range(len(userGuessInput)):
            # rule A: correct letter in the exact correct position displays uppercase
            if userGuessInput[i] == secretWord[i]:
                hint_letters.append(userGuessInput[i].upper())
            # rule B: letter is present somewhere else in the word displays lowercase
            elif userGuessInput[i] in secretWord:
                hint_letters.append(userGuessInput[i].lower())
            # rule C: letter is not present in the secret word at all displays underscore
            else:
                hint_letters.append("_")
        
        generateHintMessage = "Your hint is: " + " ".join(hint_letters)
        print(generateHintMessage)
