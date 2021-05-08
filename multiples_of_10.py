# This program Asks the user for a number, and then report whether the number is a multiple of 10 or not.
number = input("Plese enter a number you want to check? ")
number = int(number)
if number % 10 == 0:
	print(f"The given number '{number}' is multiple of 10.")
else:
	print(f"The given number '{number}' is not multiple of 10.")