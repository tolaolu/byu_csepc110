from datetime import datetime
import math
from pathlib import Path

# section 1, gathering input from the user
tireWidthInput = int(input("Enter the width of the tire in mm (ex 205): "))
while tireWidthInput < 145 or tireWidthInput > 355:
    print("Please enter a width between 145 and 355 mm.")
    tireWidthInput = int(input("Enter the width of the tire in mm (ex 205): "))

tireAspectRatioInput = int(input("Enter the aspect ratio of the tire (ex 60): "))
while tireAspectRatioInput < 10 or tireAspectRatioInput > 90:
    print("Please enter an aspect ratio between 10 and 90.")
    tireAspectRatioInput = int(input("Enter the aspect ratio of the tire (ex 60): "))

tireDiameterInput = int(input("Enter the diameter of the wheel in inches (ex 15): "))
while tireDiameterInput < 10 or tireDiameterInput > 25:
    print("Please enter a wheel diameter between 10 and 25 inches.")
    tireDiameterInput = int(input("Enter the diameter of the wheel in inches (ex 15): "))


# section 2, calculating the volume of the tire
tireVolume = (
    math.pi
    * (tireWidthInput) ** 2
    * (tireAspectRatioInput)
    * (
        tireWidthInput* tireAspectRatioInput
        + 2540 * tireDiameterInput
    )
) / 10000000000
print(f"The approximate volume is {tireVolume:.2f} liters.")

# section 3, logging data to file on my desktop
current_time = datetime.now().strftime("%Y-%m-%d")

# Path.home() finds my home directory, then I add the Desktop and tire_log.txt to the directory
log_file_path = Path.home() / "Desktop" / "volumes.txt"

try:
    with open(log_file_path, "a") as file:
        file.write(f"Timestamp: {current_time}\n")
        file.write(f"Width: {tireWidthInput} mm\n")
        file.write(f"Aspect Ratio: {tireAspectRatioInput}\n")
        file.write(f"Diameter: {tireDiameterInput} inches\n")
        file.write(f"Calculated Volume: {tireVolume:.2f} liters\n")
        file.write("-" * 30 + "\n")
    print(f"Data successfully logged to your Desktop as 'volumes.txt'.")

except OSError as e:
    print(f"Could not write file due to a system error: {e}")