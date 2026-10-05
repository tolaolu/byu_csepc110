# First, prompt for the year of interest:
yearPromptValue = int(input("Please enter the year of interest: "))

# Initialize overall tracking variables
maxLifeExpectancy = 0.0
maxCountry = ""
maxYear = ""

minLifeExpectancy = 999.0  # Start high so the first actual number drops it down
minCountry = ""
minYear = ""

# Initialize variables for the specific prompted year
maxLifeExpectancyForYear = 0.0
maxCountryForYear = ""

minLifeExpectancyForYear = 999.0
minCountryForYear = ""

totalLifeExpectancyForYear = 0.0
countForYear = 0

# Open the file:
with open("/Users/omotolabello/Downloads/life-expectancy.csv") as file:
    
    # using next() skip the header row cos of column titles
    next(file, None) 
    
    # Reading the file line by line:
    for line in file:
        # use strip to remove spaces after each word in the line and then split by comma
        eachLineInSplit = line.strip().split(",")
        
        country = eachLineInSplit[0]
        countryAcronym = eachLineInSplit[1]
        year = int(eachLineInSplit[2])          # Convert to integer for math comparison
        lifeExpectancy = float(eachLineInSplit[3]) # Convert to float for math comparison
        
        # --- Section 1: Overall Logic ---
        # Checking for overall maximum
        if lifeExpectancy > maxLifeExpectancy:
            maxLifeExpectancy = lifeExpectancy
            maxCountry = country
            maxYear = year
            
        # Checking for overall minimum
        if lifeExpectancy < minLifeExpectancy:
            minLifeExpectancy = lifeExpectancy
            minCountry = country
            minYear = year
            
        # --- Section 2: Specific Year Logic ---
        if year == yearPromptValue:
            # Add to total and count to calculate average later
            totalLifeExpectancyForYear += lifeExpectancy
            countForYear += 1
            
            # Checking for max in that specific year
            if lifeExpectancy > maxLifeExpectancyForYear:
                maxLifeExpectancyForYear = lifeExpectancy
                maxCountryForYear = country
                
            # Checking for min in that specific year
            if lifeExpectancy < minLifeExpectancyForYear:
                minLifeExpectancyForYear = lifeExpectancy
                minCountryForYear = country

# --- Section 3: Calculate the Average ---
# Guard against division by zero in case the user types a year not in the file
if countForYear > 0:
    averageLifeExpectancy = totalLifeExpectancyForYear / countForYear
else:
    averageLifeExpectancy = 0.0

# --- Section 4:Print the results ---
print(f"The overall max life expectancy is: {maxLifeExpectancy} from {maxCountry} in {maxYear}")
print(f"The overall min life expectancy is: {minLifeExpectancy} from {minCountry} in {minYear}")
print("")
print(f"For the year {yearPromptValue}:")
if countForYear > 0:
    print(f"The average life expectancy across all countries was {averageLifeExpectancy:.2f}")
    print(f"The max life expectancy was in {maxCountryForYear} with {maxLifeExpectancyForYear}")
    print(f"The min life expectancy was in {minCountryForYear} with {minLifeExpectancyForYear}")
else:
    print("No data found for that year.")
