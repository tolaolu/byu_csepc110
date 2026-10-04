
childMealPriceInput = float(input("What is the price of a child's meal? "))
adultMealPriceInput = float(input("What is the price of an adult's meal? "))
numberOfChildrenInput = int(input("How many children are there? "))
numberOfAdultsInput = int(input("How many adults are there? "))

subtotal = (childMealPriceInput * numberOfChildrenInput) + (adultMealPriceInput * numberOfAdultsInput)
print(f"Subtotal is: ${subtotal:.2f}")

salesTaxRateInput = float(input("What is the sales tax rate (as a percentage)? "))
salesTax = subtotal * (salesTaxRateInput / 100)
totalPrice = subtotal + salesTax

print(f"Sales tax is: ${salesTax:.2f}")
print(f"Total price of meal is: ${totalPrice:.2f}")

paymentAmountInput = float(input("What is the payment amount? "))
change = paymentAmountInput - totalPrice
print(f"Change is: ${change:.2f}")