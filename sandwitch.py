# This program shows how to modify lists using while loop.
sandwitch_orders = []
finished_sandwitches = []
while sandwitch_orders:
	for sandwitch in sandwitch_orders:
		if sandwitch=='cheese sandwitch':
			print("We are out of cheese sandwitch")
			while 'cheese sandwitch' in sandwitch_orders:
				sandwitch_orders.remove('cheese sandwitch')
		else:
			prepared_sandwitch = sandwitch_orders.pop()
			finished_sandwitches.append(prepared_sandwitch)
			print(f"I prepared your {prepared_sandwitch}.")
print("\nThe prepared sandwitchs are: \n")
for sandwitch in finished_sandwitches:
	print(sandwitch.title())
print()
