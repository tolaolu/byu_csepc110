greeting = "Please enter the following information: "
askFirstName = input("What is your first name? ")
askLastName = input("What is your last name? ")
askEmailAddress = input("What is your email address? ")
askPhoneNumber = input("What is your phone number? ")
askJobTitle = input("What is your job title? ")
askIdNumber = input("What is your ID number? ")
dashLine = "----------------------------------------"
goal1 = f"{askFirstName.upper()}, {askLastName.title()}\n {askJobTitle.title()}\n {askIdNumber.title()}"
goal2 = f" {askEmailAddress}\n {askPhoneNumber}"


print()
print(greeting)
print(f"First Name: {askFirstName.title()}")
print(f"Last Name: {askLastName.title()}")
print(f"Email: {askEmailAddress}")
print(f"Phone: {askPhoneNumber}")
print(f"Job Title: {askJobTitle.title()}")
print(f"ID Number: {askIdNumber}")
print()
print("The ID Card Is: ")
print(dashLine)
print(goal1)
print()
print(goal2)
print(dashLine)