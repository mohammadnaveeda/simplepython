#App that converts Feet into Metres
print("Ft to Mt Convertor App")
print("just scroll down")
 
#Python function to make it done.

def feet_to_meters(feet):
    meters = feet * 0.3048
    return meters

# Prompt the user to enter a value in feet
feet_input = float(input("Enter a value in feet: "))

# Call the feet_to_meters function and store the result
meters_result = feet_to_meters(feet_input)

# Print the result
print(f"{feet_input} feet is equal to {meters_result} meters.")
 