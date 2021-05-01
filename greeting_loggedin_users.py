# this is basic program to greet loggid in users using list, if-else and for loops
loggedin_users = ['user1','user2','user3','admin']
if loggedin_users:
	for user in loggedin_users:
		if user == 'admin':
			print(f"Hello {user}, Would you like to see a status report")
		else:
			print(f"Hello {user}, thank you for logging in again")
else:
	print("We have to find some users")
	