user_age = " "
while user_age:
	prompt = "Hi, please enter your age: "
	user_age = input(prompt)
	print(f"your age is {user_age}")
	if user_age=='quit':
		break
	else:
		user_age = int(user_age)
		if user_age<=3:
			print("you are eligible for free ticket.")
		elif user_age>3 and user_age<=12:
			print("The ticket price is $10.")		
		else:
			print("The ticket price is $15")
		print("If you want to quit, please enter 'quit'.")
