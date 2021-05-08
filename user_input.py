# asks the user how many people are in their dinner group.  
# If the answer is more than eight, print a message saying they’ll have to wait for a table. Otherwise, report that their table is ready.
dinner_group = "How many people are there in your dinner group? "
query = input(dinner_group)
query = int(query)
if query<=8:
	print("Your table is ready.")
else:
	print("You have to wait for a table.")