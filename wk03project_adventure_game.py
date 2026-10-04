story = "you wake up inside an abandoned research spaceship. " + \
        "The emergency alarms are flashing red, and you have just enough strength to press " + \
        "a single button before the main computer locks down. In front of you are " + \
        "three glowing buttons: ENGINEERING, BIOLAB, or the BRIDGE."

print("Welcome to the Adventure Game!")
userNameInput = input("What is your name? ")
modifiedUserNameInput = userNameInput.capitalize()
print(f"Cool! {modifiedUserNameInput}!! Let's begin your adventure...")
print (f"{modifiedUserNameInput}, {story}")
userFirstBttnPressed = input(f"{modifiedUserNameInput}, Which of these 3 buttons would you press? (ENGINEERING, BIOLAB, or BRIDGE) ")
userFirstDecision = userFirstBttnPressed.upper()

if userFirstDecision == "ENGINEERING":
    print(f"{modifiedUserNameInput}, you have chosen to go to the ENGINEERING section of the spaceship. " +
          "You find a room filled with tools and machinery. Suddenly, the lights flicker and you hear a strange noise coming from the corner of the room. " +
          "Do you want to investigate the noise or leave the room? (INVESTIGATE or LEAVE)")
    userSecondBttnPressed = input(f"{modifiedUserNameInput}, What would you like to do? (INVESTIGATE, LEAVE or DISSAPEAR) ")
    userSecondDecision = userSecondBttnPressed.upper()
    if userSecondDecision == "INVESTIGATE":
        print(f"{modifiedUserNameInput}, you cautiously approach the noise and discover a small alien creature trapped under a piece of machinery. " +
              "You manage to free it, and it seems grateful. The creature leads you to a hidden compartment containing valuable resources. " +
              "You have successfully completed your adventure in the ENGINEERING section!")
    elif userSecondDecision == "LEAVE":
        print(f"{modifiedUserNameInput}, you decide to leave the room and continue your exploration. " +
              "As you exit, the lights go out completely, and you find yourself in total darkness. " +
              "You stumble around and eventually find your way back to the main corridor, but you feel a sense of unease. " +
              "Your adventure in the ENGINEERING section ends here.")
    elif userSecondDecision == "DISSAPEAR":
        print(f"{modifiedUserNameInput}, you choose to disappear into the shadows, leaving the ENGINEERING section behind. " +
              "As you vanish, you feel a strange sensation, and when you reappear, you find yourself in an unknown part of the spaceship. " +
              "You have successfully completed your adventure in the ENGINEERING section by taking a mysterious path :-)")
elif userFirstDecision == "BIOLAB":
    print(f"{modifiedUserNameInput}, you have chosen to go to the BIOLAB section of the spaceship. " +
          "You find a laboratory filled with strange plants and experimental equipment. Suddenly, you hear a loud crash from the other side of the room. " +
          "Do you want to investigate the crash or leave the lab? (INVESTIGATE, LEAVE or DISSAPEAR) ")
    userSecondBttnPressed = input(f"{modifiedUserNameInput}, What would you like to do? (INVESTIGATE, LEAVE or DISSAPEAR) ")
    userSecondDecision = userSecondBttnPressed.upper()
    if userSecondDecision == "INVESTIGATE":
        print(f"{modifiedUserNameInput}, you cautiously approach the source of the crash and discover a group of mutated plants that have overgrown their containment area. " +
              "You manage to contain them and find a hidden stash of research data that could be valuable. " +
              "You have successfully completed your adventure in the BIOLAB section!")
    elif userSecondDecision == "LEAVE":
        print(f"{modifiedUserNameInput}, you decide to leave the lab and continue your exploration. " +
              "As you exit, you notice that some of the plants have started to grow rapidly, blocking your path. " +
              "You manage to find an alternate route back to the main corridor, but you feel a sense of urgency. " +
              "Your adventure in the BIOLAB section ends here.")
    elif userSecondDecision == "DISSAPEAR":
        print(f"{modifiedUserNameInput}, you choose to disappear into the shadows, leaving the BIOLAB section behind. " +
              "As you vanish, you feel a strange sensation, and when you reappear, you find yourself in an unknown part of the spaceship. " +
              "You have successfully completed your adventure in the BIOLAB section by taking a mysterious path :-)")
elif userFirstDecision == "BRIDGE":
    print(f"{modifiedUserNameInput}, you have chosen to go to the BRIDGE section of the spaceship. " +
          "You find a control room filled with blinking lights and complex instruments. Suddenly, the main computer starts to malfunction, and alarms blare throughout the room. " +
          "Do you want to try to fix the computer or leave the bridge? (FIX, LEAVE or DISSAPEAR)")
    userSecondBttnPressed = input(f"{modifiedUserNameInput}, What would you like to do? (FIX, LEAVE or DISSAPEAR) ")
    userSecondDecision = userSecondBttnPressed.upper()
    if userSecondDecision == "FIX":
        print(f"{modifiedUserNameInput}, you quickly assess the situation and manage to stabilize the main computer. " +
              "The alarms stop, and you gain access to critical navigation data that could help you escape the spaceship. " +
              "You have successfully completed your adventure in the BRIDGE section!")
    elif userSecondDecision == "LEAVE":
        print(f"{modifiedUserNameInput}, you decide to leave the bridge and continue your exploration. " +
              "As you exit, you notice that the malfunctioning computer has caused a power surge, making it difficult to navigate through the corridors. " +
              "You manage to find your way back to the main corridor, but you feel a sense of frustration. " +
              "Your adventure in the BRIDGE section ends here.")
    elif userSecondDecision == "DISSAPEAR":
        print(f"{modifiedUserNameInput}, you choose to disappear into the shadows, leaving the BRIDGE section behind. " +
              "As you vanish, you feel a strange sensation, and when you reappear, you find yourself in an unknown part of the spaceship. " +
              "You have successfully completed your adventure in the BRIDGE section by taking a mysterious path :-)")
else:
    print(f"{modifiedUserNameInput}, you have chosen an invalid option. " +
          "Please restart the game and choose one of the available buttons: ENGINEERING, BIOLAB, or BRIDGE.")
