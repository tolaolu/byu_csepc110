
# declaring variables and asking for user input:

greeting = "Please enter the following information: "
askAdjective = input("adjective: ") 
askAnimal = input("animal: ")
askVerb = input("verb: ")
askExclamation = input("exclamation: ")
askVerb1 = input("verb: ")
askVerb2 = input("verb: ")
animal = askAnimal.title()
story = f"Once upon a time, there was a {askAdjective} {animal} who loved to {askVerb}. One day, it decided to {askVerb1} and shouted '{askExclamation.capitalize()}!' as it continued to {askVerb2} through the forest."

# displaying the results

print("")
print(f"{greeting}")
print("")
print(f"adjective: {askAdjective}")
print(f"animal: {askAnimal}")
print(f"verb: {askVerb}")
print(f"exclamation: {askExclamation}")
print(f"verb: {askVerb1}")
print(f"verb: {askVerb2}")
print("")
print("Your story is: ")
print("")
print(story)