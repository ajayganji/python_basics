# This program shows how to modify lists using while loop. 
# It takes input data from the customer and saves it in a list. 
sandwitch_orders = []
choice = ("\nPlease enter the sandwitches you want.")
choice += ("\nYou can enter only one sandwitch at a time.")
choice += ("\nEnter 'save' to submit your order.\n") 
active = True
while active:
	user_choice = input(choice)
	if user_choice=='save':	
		print("\nSubmitting your order----")
		active = False
	else:
		print(f"Adding {user_choice} to your list.")
		sandwitch_orders.append(user_choice)
print("Here is your ordered list:")
for sandwitch in sandwitch_orders:
	print(f"\t{sandwitch}")