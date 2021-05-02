digit_list = list(range(1,10))
print(digit_list)
for digit in digit_list:
	if digit == 1:
		print(f"It is the {digit}st digit")
	elif digit == 2:
		print(f"It is the {digit}nd digit")
	elif digit==3:
		print(f"It is the {digit}rd digit")
	else:
		print(f"It is the {digit}th digit")
		